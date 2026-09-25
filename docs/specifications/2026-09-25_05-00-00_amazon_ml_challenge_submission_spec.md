# Amazon ML Challenge Submission Specification

## Overview

This specification formalizes the structural, relational, and schema invariants required by the official Amazon ML Challenge evaluation validator (`validate_submission.py`).

---

## 1. Output Deliverables and Header Invariants

Submissions must comprise exactly two tab-separated value (TSV) files placed in the submission directory:

### Deliverable A: `matching_results.tsv`
- **Exact TSV Header**: `source1_entity_id\tmatched_entity_ids`
- **Cardinality**: Exactly 1,732,544 rows (strict 1:1 row alignment with `test_source1.tsv`).
- **Field Description**:
  - `source1_entity_id`: Unique string identifier from `test_source1.tsv`.
  - `matched_entity_ids`: Comma-separated list of resolved entity IDs from Source 2 and Source 3 deemed to represent the exact same real-world entity. If no match is found, field is empty.

### Deliverable B: `candidate_pairs.tsv`
- **Exact TSV Header**: `source1_entity_id\tcandidate_entity_ids`
- **Cardinality**: Exactly 1,732,544 rows (strict 1:1 row alignment with `test_source1.tsv`).
- **Field Description**:
  - `source1_entity_id`: Unique string identifier from `test_source1.tsv`.
  - `candidate_entity_ids`: Comma-separated list of top-K candidate entity IDs considered during blocking.

---

## 2. Relational Invariants

1. **Subset Constraint**:
   Every entity ID present in `matched_entity_ids` must be an exact subset of the entity IDs listed in `candidate_entity_ids` for that same `source1_entity_id`:
   `matched_entity_ids ⊆ candidate_entity_ids`

2. **Row Order Consistency**:
   The row order of `source1_entity_id` in both files must align with `test_source1.tsv` to ensure deterministic linear evaluation.

3. **Character Encoding**:
   Standard UTF-8 encoding with UNIX line breaks (`\n`). No trailing empty lines or null byte characters.
