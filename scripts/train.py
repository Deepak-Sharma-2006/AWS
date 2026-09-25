#!/usr/bin/env python3
"""
TurboER: Fast Scalable LightGBM Model Trainer
Amazon ML Challenge 2026 — Business Entity Resolution

Pipeline:
1. Streams training partitions (US & India) from train_source1/2/3.tsv and train_ground_truth.tsv.
2. Generates balanced positive & hard-negative candidate pairs via MultiAttributeCountryIndex.
3. Computes the 12-dimensional SIMD feature vector per candidate pair.
4. Trains an asymmetric LightGBM Classifier (scale_pos_weight=0.35 for precision heavy F_0.5).
5. Tunes decision threshold theta directly against official macro-averaged F_0.5.
6. Persists model to models/lgbm_entity_resolver.txt and models/model_config.json.
"""
import os
import sys
import gc
import json
import time
import re
import unicodedata
from collections import defaultdict, Counter
from typing import Dict, List, Tuple, Optional
import numpy as np
import lightgbm as lgb
from rapidfuzz import fuzz
from rapidfuzz.distance import JaroWinkler

STOPWORDS = {
    "pvt", "ltd", "pvtltd", "limited", "private", "road", "street", "st", "rd",
    "india", "france", "state", "city", "co", "inc", "corp", "corporation", "company",
    "llc", "llp", "sa", "sas", "sarl", "the", "and", "of", "in", "for", "near", "opp",
    "floor", "cross", "main", "nagar", "block", "sector", "lane"
}

def strip_accents(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    return "".join(c for c in normalized if not unicodedata.combining(c))

def normalize_text(text: str) -> str:
    if not text or not isinstance(text, str):
        return ""
    t = re.sub(r"https?://\S+|www\.\S+", "", text)
    t = strip_accents(t).lower()
    t = re.sub(r"[^\w\s]", " ", t)
    return re.sub(r"\s+", " ", t).strip()

INDIAN_LEGAL_MAP = [
    (re.compile(r"\b(pvt\.?\s*ltd\.?|private\s+limited|pvt\s+ltd)\b"), "pvtltd"),
    (re.compile(r"\b(ltd\.?|limited)\b"), "ltd"),
    (re.compile(r"\b(llp|limited\s+liability\s+partnership)\b"), "llp"),
    (re.compile(r"&"), " and ")
]

US_LEGAL_MAP = [
    (re.compile(r"\b(corp\.?|corporation)\b"), "corp"),
    (re.compile(r"\b(inc\.?|incorporated)\b"), "inc"),
    (re.compile(r"\b(llc)\b"), "llc"),
    (re.compile(r"\b(llp)\b"), "llp"),
    (re.compile(r"\b(co\.?|company)\b"), "co"),
    (re.compile(r"&"), " and ")
]

def canonicalize(text: str, country: str = "US") -> str:
    if not text:
        return ""
    t = normalize_text(text)
    mapping = INDIAN_LEGAL_MAP if country == "India" else US_LEGAL_MAP
    for pattern, rep in mapping:
        t = pattern.sub(rep, t)
    return re.sub(r"\s+", " ", t).strip()

def extract_postal(address: str, country: str = "US") -> Tuple[Optional[str], Optional[str]]:
    if not address:
        return None, None
    for tok in address.split():
        if country == "India" and len(tok) == 6 and tok.isdigit():
            return tok, None
        elif country in ("France", "US") and len(tok) == 5 and tok.isdigit():
            return tok, tok[:2]
    return None, None

def extract_12_features(
    q_name: str, q_addr: str, q_post: Optional[str], q_pref: Optional[str],
    c_name: str, c_addr: str, c_post: Optional[str], c_pref: Optional[str],
    country: str
) -> List[float]:
    """Computes the 12-dimensional feature vector for a candidate pair."""
    # 1-4: Name similarities
    jw_name = float(JaroWinkler.similarity(q_name, c_name))
    tset_name = fuzz.token_set_ratio(q_name, c_name) / 100.0
    tsort_name = fuzz.token_sort_ratio(q_name, c_name) / 100.0
    part_name = fuzz.partial_ratio(q_name, c_name) / 100.0

    # 5-6: Address similarities
    jw_addr = float(JaroWinkler.similarity(q_addr, c_addr)) if (q_addr and c_addr) else 0.0
    tset_addr = fuzz.token_set_ratio(q_addr, c_addr) / 100.0 if (q_addr and c_addr) else 0.0

    # 7-8: Spatial Postal Code features
    postal_exact = 1.0 if (q_post and c_post and q_post == c_post) else 0.0
    if q_pref and c_pref:
        postal_pref = 1.0 if q_pref == c_pref else -1.0
    else:
        postal_pref = 0.0

    # 9-10: Token structural properties
    max_len = max(len(q_name), len(c_name), 1)
    len_diff = abs(len(q_name) - len(c_name)) / max_len

    q_toks = set(t for t in q_name.split() if len(t) >= 3 and t not in STOPWORDS)
    c_toks = set(t for t in c_name.split() if len(t) >= 3 and t not in STOPWORDS)
    common_toks = float(len(q_toks & c_toks))

    # 11-12: Country indicators
    c_us = 1.0 if country == "US" else 0.0
    c_ind = 1.0 if country == "India" else 0.0

    return [
        jw_name, tset_name, tsort_name, part_name,
        jw_addr, tset_addr, postal_exact, postal_pref,
        len_diff, common_toks, c_us, c_ind
    ]

def train_model(sample_train_size: int = 15000, val_size: int = 2000):
    candidate_paths = [
        "AWS_dataset/student_resource/dataset/train",
        "dataset/train",
        "../dataset/train"
    ]
    train_dir = None
    for p in candidate_paths:
        if os.path.exists(os.path.join(p, "train_source1.tsv")):
            train_dir = p
            break

    if not train_dir:
        print("[!] Error: train_source1.tsv not found.", flush=True)
        sys.exit(1)

    models_dir = "models"
    os.makedirs(models_dir, exist_ok=True)

    print(f"=== TurboER: LightGBM Model Training Pipeline ===", flush=True)
    print(f"  • Training Directory : {train_dir}", flush=True)
    print(f"  • Models Directory   : {models_dir}", flush=True)

    # 1. Load Ground Truth mapping
    print("  • Loading ground truth...", flush=True)
    gt_map = {}
    with open(os.path.join(train_dir, "train_ground_truth.tsv"), "r", encoding="utf-8") as f:
        f.readline()
        for line in f:
            p = line.rstrip("\r\n").split("\t")
            if len(p) > 1 and p[1]:
                gt_map[p[0]] = set(p[1].split(","))
            else:
                gt_map[p[0]] = set()

    # 2. Select Sample Queries
    s1_samples = []
    with open(os.path.join(train_dir, "train_source1.tsv"), "r", encoding="utf-8") as f:
        f.readline()
        for line in f:
            p = line.rstrip("\r\n").split("\t")
            if len(p) >= 4:
                s1_samples.append(p)
                if len(s1_samples) >= (sample_train_size + val_size):
                    break

    train_queries = s1_samples[:sample_train_size]
    val_queries = s1_samples[sample_train_size:sample_train_size + val_size]
    print(f"  • Selected {len(train_queries):,} train queries and {len(val_queries):,} validation queries.", flush=True)

    # 3. Stream Target entities from S2 & S3 into compact pool
    needed_ids = set()
    for q in s1_samples:
        needed_ids.update(gt_map.get(q[0], set()))

    target_pool = {}
    name_token_idx = defaultdict(list)
    postal_idx = defaultdict(list)

    def index_target_file(fname):
        count = 0
        with open(os.path.join(train_dir, fname), "r", encoding="utf-8") as f:
            f.readline()
            for line in f:
                p = line.rstrip("\r\n").split("\t")
                if len(p) >= 4:
                    e_id, b_name, b_addr, country = p[0], p[1], p[2], p[3]
                    # Index if in ground truth or for first 300,000 to form hard negatives
                    if e_id in needed_ids or count < 300000:
                        c_name = canonicalize(b_name, country)
                        c_addr = normalize_text(b_addr)
                        p_code, p_pref = extract_postal(b_addr, country)
                        target_pool[e_id] = (c_name, c_addr, p_code, p_pref, country)

                        if p_code and len(postal_idx[p_code]) < 200:
                            postal_idx[p_code].append(e_id)

                        for t in c_name.split():
                            if len(t) >= 4 and t not in STOPWORDS and len(name_token_idx[t]) < 500:
                                name_token_idx[t].append(e_id)
                        count += 1

    print("  • Indexing target entities from train_source2 & train_source3...", flush=True)
    index_target_file("train_source2.tsv")
    index_target_file("train_source3.tsv")
    print(f"    ✓ Indexed {len(target_pool):,} target entities in memory pool.", flush=True)

    # 4. Extract 12-D Training Pairs (Positives + Hard Negatives)
    print("  • Extracting 12-dimensional training feature vectors...", flush=True)
    X_train = []
    y_train = []

    for q in train_queries:
        s1_id, b_name, b_addr, country = q[0], q[1], q[2], q[3]
        q_name = canonicalize(b_name, country)
        q_addr = normalize_text(b_addr)
        q_post, q_pref = extract_postal(b_addr, country)

        true_matches = gt_map.get(s1_id, set())

        # Retrieve hard negative candidates
        cand_scores = Counter()
        if q_post and q_post in postal_idx:
            for cid in postal_idx[q_post]:
                cand_scores[cid] += 3

        tokens = [t for t in q_name.split() if len(t) >= 4 and t not in STOPWORDS and t in name_token_idx]
        tokens.sort(key=lambda t: len(name_token_idx[t]))
        for t in tokens[:3]:
            for cid in name_token_idx[t]:
                cand_scores[cid] += 5

        # Include all true positives present in target pool
        for m_id in true_matches:
            if m_id in target_pool:
                cand_scores[m_id] += 100

        top_cands = [c for c, _ in cand_scores.most_common(15)]
        for cid in top_cands:
            c_info = target_pool.get(cid)
            if not c_info or c_info[4] != country:
                continue
            feats = extract_12_features(
                q_name, q_addr, q_post, q_pref,
                c_info[0], c_info[1], c_info[2], c_info[3],
                country
            )
            label = 1 if cid in true_matches else 0
            X_train.append(feats)
            y_train.append(label)

    X_train = np.array(X_train, dtype=np.float32)
    y_train = np.array(y_train, dtype=np.int32)
    pos_count = int(np.sum(y_train))
    neg_count = len(y_train) - pos_count
    print(f"    ✓ Extracted {len(X_train):,} training pairs (Pos: {pos_count:,}, Neg: {neg_count:,}).", flush=True)

    # 5. Train LightGBM Classifier
    print("  • Training Asymmetric LightGBM Classifier...", flush=True)
    clf = lgb.LGBMClassifier(
        objective="binary",
        metric="binary_logloss",
        boosting_type="gbdt",
        scale_pos_weight=0.35,  # Heavy false-positive penalty for F_0.5
        n_estimators=250,
        learning_rate=0.08,
        num_leaves=31,
        min_child_samples=20,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        n_jobs=-1,
        verbose=-1
    )
    clf.fit(X_train, y_train)
    print("    ✓ LightGBM training complete!", flush=True)

    # 6. Threshold Calibration on Validation Split for Macro F_0.5
    print("  • Tuning decision threshold on validation queries...", flush=True)
    thresholds = [0.50, 0.60, 0.70, 0.75, 0.80, 0.85, 0.90]
    best_th = 0.75
    best_f05 = 0.0

    # Pre-extract validation features
    val_data = []
    for q in val_queries:
        s1_id, b_name, b_addr, country = q[0], q[1], q[2], q[3]
        q_name = canonicalize(b_name, country)
        q_addr = normalize_text(b_addr)
        q_post, q_pref = extract_postal(b_addr, country)
        true_m = gt_map.get(s1_id, set()) & set(target_pool.keys())

        cand_scores = Counter()
        if q_post and q_post in postal_idx:
            for cid in postal_idx[q_post]:
                cand_scores[cid] += 3
        for t in q_name.split():
            if len(t) >= 4 and t not in STOPWORDS and t in name_token_idx:
                for cid in name_token_idx[t]:
                    cand_scores[cid] += 5

        cands = [c for c, _ in cand_scores.most_common(15)]
        feat_list = []
        cand_ids = []
        for cid in cands:
            c_info = target_pool.get(cid)
            if c_info and c_info[4] == country:
                feat_list.append(extract_12_features(
                    q_name, q_addr, q_post, q_pref,
                    c_info[0], c_info[1], c_info[2], c_info[3],
                    country
                ))
                cand_ids.append(cid)
        probs = clf.predict_proba(np.array(feat_list, dtype=np.float32))[:, 1] if feat_list else np.array([])
        val_data.append((true_m, cand_ids, probs))

    for th in thresholds:
        scores = []
        for true_m, cand_ids, probs in val_data:
            pred_set = set(cid for cid, p in zip(cand_ids, probs) if p >= th)
            if not true_m and not pred_set:
                scores.append(1.0)
            elif not true_m and pred_set:
                scores.append(0.0)
            elif true_m and not pred_set:
                scores.append(0.0)
            else:
                tp = len(pred_set & true_m)
                p = tp / len(pred_set)
                r = tp / len(true_m)
                f05 = (1.25 * p * r) / (0.25 * p + r) if (0.25 * p + r) > 0 else 0.0
                scores.append(f05)
        mean_f05 = float(np.mean(scores))
        print(f"    - Threshold theta={th:.2f} -> Validation Macro F_0.5 = {mean_f05:.4f}", flush=True)
        if mean_f05 > best_f05:
            best_f05 = mean_f05
            best_th = th

    print(f"  ★ Optimal Decision Threshold: theta = {best_th:.2f} (Macro F_0.5 = {best_f05:.4f})", flush=True)

    # 7. Persist Model & Config
    model_txt_path = os.path.join(models_dir, "lgbm_entity_resolver.txt")
    clf.booster_.save_model(model_txt_path)
    print(f"  ✓ Saved LightGBM booster model to: {model_txt_path}", flush=True)

    config_path = os.path.join(models_dir, "model_config.json")
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump({
            "optimal_threshold": best_th,
            "validation_macro_f05": best_f05,
            "feature_names": [
                "jw_name", "token_set_name", "token_sort_name", "partial_ratio_name",
                "jw_addr", "token_set_addr", "postal_exact", "postal_pref",
                "name_len_diff", "common_toks", "country_us", "country_india"
            ]
        }, f, indent=2)
    print(f"  ✓ Saved configuration to: {config_path}", flush=True)
    print(f"=== Training Complete! ===", flush=True)

if __name__ == "__main__":
    train_model(sample_train_size=10000, val_size=1500)
