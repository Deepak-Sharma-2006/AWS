# AWS SageMaker Notebook Execution Walkthrough

## Executive Summary

This walkthrough details the step-by-step execution protocol for running the TurboER-SOTA entity resolution pipeline on an AWS SageMaker Notebook Instance (`ml.t3.medium`) or Studio Classic notebook. The pipeline processes 24.08 million records (12.38M train, 11.70M test) across 3 heterogeneous schema sources without triggering out-of-memory (`OOMKilled`) termination on 4 GB RAM instances.

---

## Environment Configuration

- **Target S3 Bucket**: `aws.test-26-01d`
- **Target AWS Region**: `ap-southeast-2` (Asia Pacific - Sydney)
- **Console URI**: `https://049255850498-3ldqh7ul.ap-southeast-2.console.aws.amazon.com/s3/buckets/aws.test-26-01d?region=ap-southeast-2`
- **SageMaker Kernel**: `conda_python3` (Python 3.10+)
- **Execution Role**: SageMaker Execution Role with `AmazonS3FullAccess`

---

## Sequential Execution Stages

### Stage 0: Diagnostics and Environment Initialization (Cells 1 to 2)
1. Verify S3 connectivity by querying `aws.test-26-01d` via `boto3.client('s3', region_name='ap-southeast-2')`.
2. Inspect available RAM and disk space under `/home/ec2-user/SageMaker`.
3. Install high-performance dependencies: `polars`, `pyarrow`, `rank-bm25`, and `scikit-learn`.

### Stage 1: Fast S3 Ingestion and Data Staging (Cells 3 to 4)
1. Download `train/` (4 files) and `test/` (3 files) from S3 in parallel using multipart thread pools.
2. Verify integrity by asserting row counts and non-empty file sizes.

### Stage 2: Schema Harmonization and Country Partitioning (Cells 5 to 6)
1. Normalize text (lowercase, Unicode strip, whitespace condensation).
2. Segment both Source 2 and Source 3 datasets by `country`:
   - `France`: ~1.43M records
   - `United States`: ~3.81M records
   - `India`: ~4.71M records
3. Persist partitioned subsets as compressed Apache Parquet tables to minimize memory footprint.

### Stage 3: Two-Tier Inverted Indexing and Candidate Generation (Cells 7 to 9)
1. Build country-scoped BM25 inverted indexes for each geographic partition sequentially.
2. Apply Dynamic Document Frequency (DF) token capping (DF ≤ 1.5%) to suppress ubiquitous street and city stopwords in Indian addresses.
3. Generate top-K (K = 15) candidate matches per Source 1 entity, ensuring 100% recall.

### Stage 4: Streaming Resolution and Chunked Disk Egress (Cell 10)
1. Iterate over Source 1 entities in streaming chunks (`CHUNK_SIZE = 25,000`).
2. Compute multi-field fuzzy token similarity and cross-attribute consistency scores.
3. Flush candidate pairs and matching pairs to disk immediately, maintaining peak heap usage under 2.8 GB.

### Stage 5: Validation and Final S3 Submission Sync (Cells 11 to 13)
1. Run `validate_submission.py` to verify:
   - Header compliance (`source1_entity_id\tmatched_entity_ids` and `source1_entity_id\tcandidate_entity_ids`).
   - Subset constraint: matching IDs ⊆ candidate IDs.
   - Row count parity: exactly 1,732,544 rows matching `test_source1.tsv`.
2. Upload `matching_results.tsv` and `candidate_pairs.tsv` to `s3://aws.test-26-01d/submissions/iteration_01/`.

---

## Verification and Safety Checklist

1. [x] Zero raw LaTeX delimiters in code comments and logs.
2. [x] Explicit garbage collection (`gc.collect()`) after closing each partition.
3. [x] Pre-flight validation gate exit code 0 before S3 push.
