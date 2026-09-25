# Business Entity Resolution Pipeline - Amazon ML Challenge 2026

## Reproducibility Instructions

### 1. Environment Setup
```bash
pip install -r requirements.txt
```

### 2. Execution
Place the test dataset files in `dataset/test/`:
- `test_source1.tsv`
- `test_source2.tsv`
- `test_source3.tsv`

Execute the inference engine:
```bash
python src/run_test_inference.py
```

### 3. Generated Deliverables
- `output/matching_results.tsv` (Official Leaderboard Predictions)
- `output/candidate_pairs.tsv` (Blocking Stage Candidates)
- `output/submission.zip` (Submission Package)
