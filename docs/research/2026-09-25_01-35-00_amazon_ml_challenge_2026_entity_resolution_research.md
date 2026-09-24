# Deep Research Dossier: Amazon ML Challenge 2026 — Business Entity Resolution

> **Problem Scope**: Multi-Source Entity Resolution across 3 Independent Data Sources  
> **Evaluation Metric**: Macro-Averaged F_0.5 Score (Precision-Heavy, Singletons Included)  
> **Lead Persona**: Deep Research Specialist  
> **Fair-Play Constraints**: Strictly ZERO external lookups, geocoding APIs, or data augmentation; Model ≤ 8B params, MIT/Apache 2.0  

---

## 1. Executive Problem Deconstruction & Forensic Evidence

### 1.1 Source Topography & Mathematical Formulation
- **Source 1 (Reference)**: `train_source1.tsv` (2,206,823 rows, 200.3 MB), `test_source1.tsv` (1,732,546 rows, 166.9 MB).
  - Source 1 is already deduplicated internally. Every entity in Source 1 represents a unique real-world business anchor.
- **Source 2 (Target 1)**: `train_source2.tsv` (5,034,618 rows, 466.6 MB), `test_source2.tsv` (5,142,392 rows, 485.9 MB).
- **Source 3 (Target 2)**: `train_source3.tsv` (5,142,392 rows, 480.4 MB), `test_source3.tsv` (5,034,618 rows, 482.6 MB).
- **Ground Truth**: `train_ground_truth.tsv` (2,206,823 rows, 121.1 MB).
- **Cartesian Scale Physics**:
  - Full naive cross-product: 1.73 × 10⁶ (S1) × [5.14 × 10⁶ (S2) + 5.03 × 10⁶ (S3)] ≈ 1.76 × 10¹³ potential candidate pairs.
  - At 1 microsecond per pairwise comparison, brute-force evaluation would require ~203 days of continuous compute.
  - Hence, **Stage 1 Blocking (Candidate Generation) is mathematically the single most critical architectural bottleneck**, determining both the recall upper bound and computational tractability.

### 1.2 Ground-Truth Forensic Empirical Noise Patterns
Inspection of ground-truth matches (e.g. entity `S1-965667`) reveals 6 distinct empirical noise vectors:
1. **Name Typo Perturbations**: "Maure Williams" → "Maure Wilblims" (edit distance = 1).
2. **Legal Suffix Inconsistency & Dropping**: "Colombier Inc" → "Colombier", "Pvt Ltd" → "Private Limited", "LLC" → omitted.
3. **DBA / Trade Name Disjunction**: Reference entity `S1-965667` ("Maure Williams Colombier Inc") matches `S3-775321672` named "Dréxkor" based entirely on high-fidelity address matching.
4. **Digital Presence Artifacts**: Business names recorded as domain URLs ("maurewilliamscolombier.com").
5. **Address Truncation & Component Reordering**: Street, City, State ordering swapped; missing postal codes; municipal landmarks ("Near Fortis Hospital").
6. **Missing Address Fields**: Records with zero address tokens requiring pure high-confidence name/legal-entity resolution.

### 1.3 Out-of-Distribution Open-Set Country Shift: France
- Training datasets only contain `US` and `India`.
- Test datasets contain `US`, `India`, and `France` (e.g. `S1-156285671` in Bordeaux, Nouvelle-Aquitaine).
- Any hardcoding or static one-hot encoding restricted to `{US, India}` causes immediate catastrophic failure on test data.
- French address conventions (e.g. "Boulevard du Président Franklin Roosevelt", 5-digit French postal codes, CEDEX) require language-agnostic tokenizers and country-conditional routing.

---

## 2. Evaluation Metric Dynamics & Mathematical Optimization

### 2.1 The Macro-Averaged F_0.5 Objective
The competition is evaluated on macro-averaged F_0.5 across all Source 1 entities:

```
F_0.5 = (1.25 × Precision × Recall) / (0.25 × Precision + Recall)
```

- Precision is weighted 2× over Recall (β = 0.5).
- In Entity Resolution, **false merges (false positives) destroy scores twice as fast as missed links (false negatives)**.
- **The Singleton Phenomenon**:
  - A Source 1 entity with zero true matches scores **1.0** if and only if predicted as an empty string `""`.
  - Predicting even a single false-positive candidate on a singleton collapses its score to **0.0**.
  - With hundreds of thousands of singletons in the dataset, conservative high-thresholding on singletons is mandatory.

---

## 3. Competitive Technical Moat & SOTA Architecture

### 3.1 Multi-Tier Candidate Generation (Blocking)
To achieve ≥ 97% recall while keeping candidates per S1 entity capped at K ≤ 30:
1. **Country Partitioning**: Hard partition by country (`US` → `US`, `India` → `India`, `France` → `France`).
2. **MinHash Locality Sensitive Hashing (LSH)**: 3-gram character shingles across concatenated `business_name` + `business_address`.
3. **BM25 Sparse Lexical Retrieval**: S2 and S3 indexed into an in-memory sparse inverted index; S1 queries executed with BM25 scoring.
4. **Phonetic & Soundex Key Blocking**: Double Metaphone on primary name token.
5. **Exact Match High-Speed Pass**: Normalized name hashes for instant high-confidence indexing.

### 3.2 Feature Engineering Topology
For each candidate pair `(S1, S2/S3)`:
- **String Distance Vector**:
  - Jaro-Winkler (name and address)
  - Levenshtein ratio and normalized edit distance
  - Damerau-Levenshtein transposition distance
  - Monge-Elkan token similarity
  - Character 3-gram Jaccard overlap
  - Token Sort Ratio & Token Set Ratio
- **Component-Specific Normalization**:
  - Legal suffix matching (regex dictionary of global company suffixes)
  - Postal code exact match (6-digit India PIN, 5/9-digit US ZIP, 5-digit France postal code)
  - State/City fuzzy alignment
  - Domain extraction (detecting `.com`, `.in`, `.fr`, `www.` in name strings)
- **Graph & Context Features**:
  - Source origin indicator (S2 vs S3)
  - Blocking pass origin (LSH rank, BM25 score, exact match flag)
  - Token length ratio and missing-address indicator flags

### 3.3 Two-Stage Model Pipeline
1. **LightGBM / XGBoost Ranker**:
   - Highly parallel, sub-millisecond scoring per candidate pair.
   - Directly optimized for precision with custom cost matrix penalizing false positives 2.5× over false negatives.
2. **Targeted Neural Cross-Encoder (Apache 2.0 / MIT ≤ 8B)**:
   - For ambiguous candidate pairs with GBDT confidence between 0.40 and 0.75, evaluate using a compact quantized Transformer (`bge-small-en-v1.5` or `MiniLM-L6`).

### 3.4 Strict Fair-Play & Submission Compliance
- 100% self-contained Python stdlib and pinned open-source libraries.
- Zero network requests during inference.
- Output validation verified via `utils/validate_submission.py`.
