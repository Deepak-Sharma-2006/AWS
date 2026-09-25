import time
import os

def audit():
    t0 = time.time()
    
    # Dynamically resolve TSV paths (supports both CWD and output/ directory)
    fc_path = "output/candidate_pairs.tsv" if os.path.exists("output/candidate_pairs.tsv") else "candidate_pairs.tsv"
    fm_path = "output/matching_results.tsv" if os.path.exists("output/matching_results.tsv") else "matching_results.tsv"
    
    # Dynamically resolve test_source1.tsv
    s1_candidates = [
        "AWS_dataset/student_resource/dataset/test/test_source1.tsv",
        "student_resource/dataset/test/test_source1.tsv",
        "dataset/test/test_source1.tsv"
    ]
    test_s1_path = next((p for p in s1_candidates if os.path.exists(p)), None)

    print("=" * 70)
    print("      DEEP AUDIT OF EXTRACTED SUBMISSION TSV FILES")
    print("=" * 70)

    # 1. File existence and sizes
    for p in [fc_path, fm_path]:
        sz_mb = os.path.getsize(p) / (1024 * 1024)
        print(f"File: {p} -> Size: {sz_mb:.2f} MB")

    # 2. Header and First 5 rows
    with open(fc_path, "r", encoding="utf-8") as fc, open(fm_path, "r", encoding="utf-8") as fm:
        h_c = fc.readline().rstrip("\r\n").split("\t")
        h_m = fm.readline().rstrip("\r\n").split("\t")
        print(f"\n[HEADERS]")
        print(f"  candidate_pairs.tsv : {h_c}")
        print(f"  matching_results.tsv: {h_m}")

        print(f"\n[SAMPLE ROWS 1-5]")
        for i in range(5):
            pc = fc.readline().rstrip("\r\n").split("\t")
            pm = fm.readline().rstrip("\r\n").split("\t")
            c_text = pc[1][:60] + "..." if len(pc) > 1 and len(pc[1]) > 60 else (pc[1] if len(pc) > 1 else "")
            m_text = pm[1] if len(pm) > 1 else ""
            print(f"  Row {i+1}: ID={pc[0]} | Candidates=[{c_text}] | Matches=[{m_text}]")

    # 3. Full Invariant and Statistical Audit
    print(f"\n[FULL STREAMING VERIFICATION ACROSS ALL ENTITIES]")
    total_rows = 0
    m_subset_c_violations = 0
    id_mismatches = 0
    order_mismatches_with_s1 = 0

    total_cands = 0
    total_matches = 0
    cand_dist = {0: 0, "1-3": 0, "4-6": 0, "7-9": 0, "10-12": 0, "12+": 0}
    match_dist = {0: 0, 1: 0, 2: 0, "3+": 0}

    # Also compare ordering against test_source1.tsv if present
    s1_file = open(test_s1_path, "r", encoding="utf-8") if os.path.exists(test_s1_path) else None
    if s1_file:
        s1_file.readline() # skip header

    with open(fc_path, "r", encoding="utf-8") as fc, open(fm_path, "r", encoding="utf-8") as fm:
        next(fc)
        next(fm)
        for line_idx, (lc, lm) in enumerate(zip(fc, fm), start=2):
            total_rows += 1
            pc = lc.rstrip("\r\n").split("\t")
            pm = lm.rstrip("\r\n").split("\t")

            s1_id = pc[0]
            if s1_id != pm[0]:
                id_mismatches += 1
                if id_mismatches <= 3:
                    print(f"  [!] ID Mismatch at line {line_idx}: Cand ID={s1_id}, Match ID={pm[0]}")

            if s1_file:
                s1_line = s1_file.readline()
                if s1_line:
                    expected_id = s1_line.split("\t")[0]
                    if s1_id != expected_id:
                        order_mismatches_with_s1 += 1
                        if order_mismatches_with_s1 <= 3:
                            print(f"  [!] Order Mismatch with test_source1 at line {line_idx}: got {s1_id}, expected {expected_id}")

            c_set = set(pc[1].split(",")) if len(pc) > 1 and pc[1] else set()
            m_set = set(pm[1].split(",")) if len(pm) > 1 and pm[1] else set()

            if not m_set.issubset(c_set):
                m_subset_c_violations += 1
                if m_subset_c_violations <= 3:
                    print(f"  [!] M ⊆ C Violation at {s1_id}: M={m_set} not in C={c_set}")

            n_c = len(c_set)
            n_m = len(m_set)
            total_cands += n_c
            total_matches += n_m

            if n_c == 0:
                cand_dist[0] += 1
            elif n_c <= 3:
                cand_dist["1-3"] += 1
            elif n_c <= 6:
                cand_dist["4-6"] += 1
            elif n_c <= 9:
                cand_dist["7-9"] += 1
            elif n_c <= 12:
                cand_dist["10-12"] += 1
            else:
                cand_dist["12+"] += 1

            if n_m == 0:
                match_dist[0] += 1
            elif n_m == 1:
                match_dist[1] += 1
            elif n_m == 2:
                match_dist[2] += 1
            else:
                match_dist["3+"] += 1

    if s1_file:
        s1_file.close()

    print(f"\n[VERIFICATION RESULTS]")
    print(f"  • Total Rows Evaluated            : {total_rows:,} (Expected: 1,732,544)")
    print(f"  • Row Count Match Status          : {'✓ PERFECT MATCH' if total_rows == 1732544 else 'FAILED'}")
    print(f"  • File Alignment (Cand vs Match)  : {'✓ 100% ALIGNED' if id_mismatches == 0 else f'FAILED ({id_mismatches} mismatches)'}")
    print(f"  • Source 1 Sequence Order Match   : {'✓ 100% IDENTICAL' if order_mismatches_with_s1 == 0 else f'FAILED ({order_mismatches_with_s1} mismatches)'}")
    print(f"  • M ⊆ C Subsumption Constraint    : {'✓ 100% COMPLIANT (0 VIOLATIONS)' if m_subset_c_violations == 0 else f'FAILED ({m_subset_c_violations} violations)'}")

    print(f"\n[CANDIDATE COVERAGE & RETRIEVAL DENSITY]")
    cands_covered = total_rows - cand_dist[0]
    print(f"  • Total Candidate Pairs Generated : {total_cands:,}")
    print(f"  • Average Candidates per Query    : {total_cands / total_rows:.2f}")
    print(f"  • Queries with ≥ 1 Candidate      : {cands_covered:,} ({cands_covered / total_rows * 100:.2f}%)")
    print(f"  • Candidate Distribution Breakdown:")
    for bucket, count in cand_dist.items():
        print(f"      - [{bucket:>5}] candidates: {count:>10,} ({count / total_rows * 100:5.2f}%)")

    print(f"\n[MATCH RESOLUTION & PRECISION DENSITY]")
    queries_matched = total_rows - match_dist[0]
    print(f"  • Total Matched Entities          : {total_matches:,}")
    print(f"  • Queries Resolved to Match       : {queries_matched:,} ({queries_matched / total_rows * 100:.2f}%)")
    print(f"  • Single-Target Matches (1-to-1)  : {match_dist[1]:,} ({match_dist[1] / max(queries_matched, 1) * 100:.2f}% of matched)")
    print(f"  • Multi-Target Matches (1-to-N)   : {match_dist[2] + match_dist['3+']:,} ({(match_dist[2] + match_dist['3+']) / max(queries_matched, 1) * 100:.2f}% of matched)")
    print(f"  • Zero Match Queries (Singletons) : {match_dist[0]:,} ({match_dist[0] / total_rows * 100:.2f}%)")
    print(f"  • Match Distribution Breakdown:")
    for bucket, count in match_dist.items():
        print(f"      - [{bucket} matches]: {count:>10,} ({count / total_rows * 100:5.2f}%)")

    print(f"\nAudit completed in {time.time() - t0:.2f} seconds.")
    print("=" * 70)

if __name__ == '__main__':
    audit()
