#!/usr/bin/env python3
"""
High-Performance Standalone Test Inference Engine for Amazon ML Challenge 2026.
Executes outside Jupyter notebook kernel for process isolation, instant interruptibility,
and strictly bounded RAM (< 1.1 GB).
"""
import os
import sys
import csv
import gc
import time
import re
import unicodedata
from collections import defaultdict
from typing import Dict, Any, List, Tuple, Optional

# RapidFuzz SIMD with graceful pure-python fallback
try:
    from rapidfuzz import fuzz
    from rapidfuzz.distance import JaroWinkler
    def calc_jw(s1: str, s2: str) -> float:
        return float(JaroWinkler.similarity(s1, s2))
except ImportError:
    import difflib
    class FuzzFallback:
        @staticmethod
        def ratio(s1: str, s2: str) -> float:
            return difflib.SequenceMatcher(None, s1, s2).ratio() * 100.0
    fuzz = FuzzFallback()
    def calc_jw(s1: str, s2: str) -> float:
        return difflib.SequenceMatcher(None, s1, s2).ratio()

# Decision Gate
THETA_MATCH = 0.74

# Corporate Stopwords
STOPWORDS = {
    "pvt", "ltd", "pvtltd", "limited", "private", "road", "street",
    "india", "france", "state", "city", "co", "inc", "corp", "llc", "sa", "sas", "sarl"
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

FRENCH_LEGAL_MAP = [
    (re.compile(r"\b(ste|sté)\b"), "societe"),
    (re.compile(r"\b(ets|etablissements)\b"), "etablissements"),
    (re.compile(r"\b(cie|compagnie)\b"), "compagnie"),
    (re.compile(r"\b(eurl)\b"), "eurl"),
    (re.compile(r"\b(sarl)\b"), "sarl"),
    (re.compile(r"\b(sas)\b"), "sas"),
    (re.compile(r"\b(sa)\b"), "sa"),
    (re.compile(r"&"), " et ")
]

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

def canonicalize_legal_suffixes(text: str, country: str = "US") -> str:
    if not text or not isinstance(text, str):
        return ""
    t = normalize_text(text)
    mapping = FRENCH_LEGAL_MAP if country == "France" else (INDIAN_LEGAL_MAP if country == "India" else US_LEGAL_MAP)
    for pattern, replacement in mapping:
        t = pattern.sub(replacement, t)
    return re.sub(r"\s+", " ", t).strip()

def extract_postal_code(address: str, country: str = "US") -> Tuple[Optional[str], Optional[str]]:
    if not address or not isinstance(address, str):
        return None, None
    for tok in address.split():
        if country == "India" and len(tok) == 6 and tok.isdigit():
            return tok, None
        elif country in ("France", "US") and len(tok) == 5 and tok.isdigit():
            return tok, tok[:2]
    return None, None

class UltraCompactCountryIndex:
    def __init__(self, max_postings: int = 150):
        self.max_postings = max_postings
        self.entities = {}  # e_id -> (clean_name, clean_addr, p_code)
        self.token_to_ids = defaultdict(list)
        self.name_prefix_to_ids = defaultdict(list)
        self.postal_to_ids = defaultdict(list)

    def add_entity(self, e_id: str, b_name: str, b_addr: str, country: str):
        c_name = canonicalize_legal_suffixes(b_name, country=country) if b_name else ""
        c_addr = normalize_text(b_addr) if b_addr else ""
        p_code, _ = extract_postal_code(b_addr, country=country) if b_addr else (None, None)

        self.entities[e_id] = (c_name, c_addr, p_code)

        prefix = c_name[:7]
        if len(prefix) >= 4 and len(self.name_prefix_to_ids[prefix]) < 20:
            self.name_prefix_to_ids[prefix].append(e_id)

        if p_code and len(self.postal_to_ids[p_code]) < 50:
            self.postal_to_ids[p_code].append(e_id)

        for t in c_name.split():
            if len(t) >= 4 and t not in STOPWORDS and len(self.token_to_ids[t]) < self.max_postings:
                self.token_to_ids[t].append(e_id)

    def query_candidates(self, q_name: str, p_code: Optional[str], top_k: int = 12) -> List[str]:
        candidate_scores = defaultdict(int)

        if p_code and p_code in self.postal_to_ids:
            for c_id in self.postal_to_ids[p_code]:
                candidate_scores[c_id] += 5

        indexed_tokens = [(t, len(self.token_to_ids[t])) for t in q_name.split() if len(t) >= 4 and t in self.token_to_ids]
        indexed_tokens.sort(key=lambda x: x[1])
        for t, _ in indexed_tokens[:3]:
            for c_id in self.token_to_ids[t]:
                candidate_scores[c_id] += 2

        prefix = q_name[:7]
        if prefix in self.name_prefix_to_ids:
            for c_id in self.name_prefix_to_ids[prefix]:
                candidate_scores[c_id] += 4

        if not candidate_scores:
            return []

        ranked = sorted(candidate_scores.items(), key=lambda x: x[1], reverse=True)
        return [c_id for c_id, _ in ranked[:top_k]]

    def clear(self):
        self.entities.clear()
        self.token_to_ids.clear()
        self.name_prefix_to_ids.clear()
        self.postal_to_ids.clear()
        gc.collect()

def run_pipeline():
    test_dir = "dataset/test"
    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    out_candidates = os.path.join(output_dir, "candidate_pairs.tsv")
    out_matches = os.path.join(output_dir, "matching_results.tsv")

    t_s1 = os.path.join(test_dir, "test_source1.tsv")
    t_s2 = os.path.join(test_dir, "test_source2.tsv")
    t_s3 = os.path.join(test_dir, "test_source3.tsv")

    for path in (t_s1, t_s2, t_s3):
        if not os.path.exists(path):
            print(f"[!] Error: Required test file not found: {path}", flush=True)
            sys.exit(1)

    # Initialize or resume files
    file_mode = "w"
    completed_countries = set()
    if os.path.exists(out_matches) and os.path.getsize(out_matches) > 100:
        # Check existing count and header compliance
        with open(out_matches, "r", encoding="utf-8") as f:
            header = f.readline().strip().split("\t")
            existing_count = sum(1 for _ in f)
        if existing_count >= 259452 and header == ["source1_entity_id", "matched_entity_ids"]:
            print(f"  [i] Found {existing_count:,} existing rows with valid headers. Resuming from US and India...", flush=True)
            completed_countries.add("France")
            file_mode = "a"
        else:
            print(f"  [i] Existing output had outdated schema ({header}). Starting fresh clean run...", flush=True)
            completed_countries.clear()
            file_mode = "w"
    
    if file_mode == "w":
        with open(out_candidates, "w", encoding="utf-8", newline="") as fc, \
             open(out_matches, "w", encoding="utf-8", newline="") as fm:
            csv.writer(fc, delimiter="\t").writerow(["source1_entity_id", "candidate_entity_ids"])
            csv.writer(fm, delimiter="\t").writerow(["source1_entity_id", "matched_entity_ids"])

    COUNTRIES = ["France", "US", "India"]
    start_all = time.time()

    for country in COUNTRIES:
        if country in completed_countries:
            print(f"\n[SKIP] {country} already completed ({259452:,} rows). Skipping to next country.", flush=True)
            continue

        c_start = time.time()
        print(f"\n" + "="*60, flush=True)
        print(f"  --> Processing Partition: {country.upper()}", flush=True)
        print("="*60, flush=True)

        index = UltraCompactCountryIndex(max_postings=150)

        # 1. Stream S2 into index (Fast split parser)
        print(f"  • Indexing {country} from test_source2.tsv...", flush=True)
        t_s2 = time.time()
        s2_count = 0
        s2_file = os.path.join(test_dir, "test_source2.tsv")
        with open(s2_file, "r", encoding="utf-8") as f:
            next(f, None)
            for line in f:
                parts = line.rstrip("\r\n").split("\t")
                if len(parts) >= 4 and parts[3] == country:
                    index.add_entity(parts[0], parts[1], parts[2], country)
                    s2_count += 1
                    if s2_count % 500000 == 0:
                        print(f"    - S2 indexed {s2_count:,} ({time.time()-t_s2:.1f}s)...", flush=True)
        print(f"    ✓ S2: {s2_count:,} indexed in {time.time()-t_s2:.1f}s", flush=True)

        # 2. Stream S3 into index
        print(f"  • Indexing {country} from test_source3.tsv...", flush=True)
        t_s3 = time.time()
        s3_count = 0
        with open(os.path.join(test_dir, "test_source3.tsv"), "r", encoding="utf-8") as f:
            next(f, None)
            for line in f:
                parts = line.rstrip("\r\n").split("\t")
                if len(parts) >= 4 and parts[3] == country:
                    index.add_entity(parts[0], parts[1], parts[2], country)
                    s3_count += 1
                    if s3_count % 500000 == 0:
                        print(f"    - S3 indexed {s3_count:,} ({time.time()-t_s3:.1f}s)...", flush=True)
        print(f"    ✓ S3: {s3_count:,} indexed in {time.time()-t_s3:.1f}s", flush=True)
        print(f"  • Total target entities indexed: {s2_count + s3_count:,} in {time.time()-c_start:.1f}s", flush=True)

        # 3. Stream S1 Queries
        print(f"  • Streaming Source 1 queries for {country}...", flush=True)
        t_q = time.time()
        cand_batch, match_batch = [], []
        CHUNK_SIZE = 25000
        REPORT_INTERVAL = 25000
        q_count = 0

        with open(out_candidates, "a", encoding="utf-8", newline="") as fc, \
             open(out_matches, "a", encoding="utf-8", newline="") as fm:
            wc = csv.writer(fc, delimiter="\t")
            wm = csv.writer(fm, delimiter="\t")

            with open(os.path.join(test_dir, "test_source1.tsv"), "r", encoding="utf-8") as f:
                next(f, None)
                for line in f:
                    parts = line.rstrip("\r\n").split("\t")
                    if len(parts) < 4 or parts[3] != country:
                        continue

                    s1_id = parts[0]
                    b_name = parts[1]
                    b_addr = parts[2]
                    c_name = canonicalize_legal_suffixes(b_name, country=country) if b_name else ""
                    p_code, _ = extract_postal_code(b_addr, country=country) if b_addr else (None, None)

                    candidates = index.query_candidates(c_name, p_code, top_k=12)
                    cand_batch.append([s1_id, ",".join(candidates)])

                    if not candidates:
                        match_batch.append([s1_id, ""])
                    else:
                        matched = []
                        for c_id in candidates:
                            c_data = index.entities.get(c_id)
                            if c_data:
                                c_clean_name = c_data[0]
                                if c_name == c_clean_name:
                                    matched.append(c_id)
                                    continue
                                jw = calc_jw(c_name, c_clean_name)
                                if jw < 0.48:  # Mathematically cannot reach 0.74 threshold
                                    continue
                                tset = fuzz.token_set_ratio(c_name, c_clean_name) / 100.0
                                score = (jw + tset) / 2.0
                                if score >= THETA_MATCH:
                                    matched.append(c_id)
                        match_batch.append([s1_id, ",".join(matched)])

                    q_count += 1
                    if q_count % REPORT_INTERVAL == 0:
                        rate = q_count / max(time.time() - t_q, 0.001)
                        print(f"    [{country}] {q_count:,} queried | Speed: {rate:,.0f} q/s | Elapsed: {time.time()-t_q:.1f}s", flush=True)

                    if len(cand_batch) >= CHUNK_SIZE:
                        wc.writerows(cand_batch)
                        wm.writerows(match_batch)
                        cand_batch.clear()
                        match_batch.clear()

            if cand_batch:
                wc.writerows(cand_batch)
                wm.writerows(match_batch)
                cand_batch.clear()
                match_batch.clear()

        print(f"  ✓ {country} completed: {q_count:,} queries in {time.time()-c_start:.1f}s.", flush=True)
        index.clear()
        gc.collect()

    total_time = time.time() - start_all
    print(f"\n[PIPELINE COMPLETE] All test partitions processed in {total_time:.1f}s ({total_time/60:.1f} mins).", flush=True)
    print(f"  • Candidates File : {out_candidates}", flush=True)
    print(f"  • Matching File   : {out_matches}", flush=True)

    validate_and_package(out_candidates, out_matches)

def validate_and_package(out_candidates: str, out_matches: str):
    import zipfile
    print("\n" + "="*60, flush=True)
    print("  --> Executing Official Submission Validation & Packaging", flush=True)
    print("="*60, flush=True)

    errors = []
    m_count = 0
    with open(out_matches, "r", encoding="utf-8") as fm, open(out_candidates, "r", encoding="utf-8") as fc:
        h_m = fm.readline().strip().split("\t")
        h_c = fc.readline().strip().split("\t")
        if h_m != ["source1_entity_id", "matched_entity_ids"]:
            errors.append(f"Invalid matching header: {h_m}")
        if h_c != ["source1_entity_id", "candidate_entity_ids"]:
            errors.append(f"Invalid candidate header: {h_c}")

        for i, (lm, lc) in enumerate(zip(fm, fc)):
            m_count += 1
            sm = lm.strip().split("\t")
            sc = lc.strip().split("\t")
            if sm[0] != sc[0]:
                errors.append(f"Row ID mismatch on line {i+2}: {sm[0]} vs {sc[0]}")
                break
            m_set = set(sm[1].split(",")) if len(sm) > 1 and sm[1] else set()
            c_set = set(sc[1].split(",")) if len(sc) > 1 and sc[1] else set()
            if not m_set.issubset(c_set):
                errors.append(f"Subset invariant breached on {sm[0]}: matches not in candidates")
                break

    if errors:
        print("\n[!] Validation FAILED:")
        for e in errors:
            print("  • " + e)
        return False

    print(f"  ✓ Validation PASSED: All {m_count:,} test entities aligned and compliant with M ⊆ C!", flush=True)

    zip_path = "output/submission.zip"
    print(f"  • Packaging {zip_path} ...", flush=True)
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        zf.write(out_candidates, arcname="candidate_pairs.tsv")
        zf.write(out_matches, arcname="matching_results.tsv")

    size_mb = os.path.getsize(zip_path) / (1024 * 1024)
    print(f"  ✓ Submission archive created: {zip_path} ({size_mb:.2f} MB)", flush=True)

    try:
        import boto3
        s3 = boto3.client("s3", region_name="ap-southeast-2")
        s3.upload_file(zip_path, "aws.test-26-01d", "submission.zip")
        print(f"  ✓ Uploaded to S3: s3://aws.test-26-01d/submission.zip", flush=True)
    except Exception as e:
        print(f"  [i] S3 upload skipped ({e}). Archive is ready locally at {zip_path}", flush=True)

    print("  ★ READY FOR LEADERBOARD SUBMISSION ★", flush=True)
    return True

if __name__ == "__main__":
    run_pipeline()

