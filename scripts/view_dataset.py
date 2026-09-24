"""
Zero-Copy High-Performance TSV Dataset Viewer for IDE & Terminal.
Enables clean, column-aligned viewing and interactive inspection of
AWS_dataset/student_resource/dataset/ without modifying or duplicating any files.
"""

import os
import sys
import csv
import argparse
from typing import List, Dict, Optional, Tuple

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

DATASET_ROOT = os.path.join("AWS_dataset", "student_resource", "dataset")

TSV_FILES = {
    "train_source1": os.path.join(DATASET_ROOT, "train", "train_source1.tsv"),
    "train_source2": os.path.join(DATASET_ROOT, "train", "train_source2.tsv"),
    "train_source3": os.path.join(DATASET_ROOT, "train", "train_source3.tsv"),
    "train_ground_truth": os.path.join(DATASET_ROOT, "train", "train_ground_truth.tsv"),
    "test_source1": os.path.join(DATASET_ROOT, "test", "test_source1.tsv"),
    "test_source2": os.path.join(DATASET_ROOT, "test", "test_source2.tsv"),
    "test_source3": os.path.join(DATASET_ROOT, "test", "test_source3.tsv"),
}


def format_table(headers: List[str], rows: List[List[str]], max_col_widths: Optional[Dict[str, int]] = None) -> str:
    """Renders a clean, Unicode-aligned table suitable for IDE terminals and text editors."""
    if not rows and not headers:
        return "(empty dataset)"

    if max_col_widths is None:
        max_col_widths = {
            "entity_id": 16,
            "source1_entity_id": 18,
            "country": 8,
            "business_name": 32,
            "business_address": 50,
            "matched_entity_ids": 45,
            "candidate_entity_ids": 45,
        }

    # Calculate actual column widths
    widths = []
    for i, h in enumerate(headers):
        limit = max_col_widths.get(h.lower(), 40)
        max_w = len(h)
        for r in rows:
            if i < len(r):
                max_w = max(max_w, len(str(r[i])))
        widths.append(min(max_w, limit))

    def truncate_cell(val: str, w: int) -> str:
        s = str(val).replace("\t", " ").replace("\n", " ").replace("\r", "")
        if len(s) > w:
            return s[:w - 3] + "..."
        return s.ljust(w)

    # Box-drawing elements
    sep_top = "┌" + "┬".join("─" * (w + 2) for w in widths) + "┐"
    sep_mid = "├" + "┼".join("─" * (w + 2) for w in widths) + "┤"
    sep_bot = "└" + "┴".join("─" * (w + 2) for w in widths) + "┘"

    header_line = "│ " + " │ ".join(truncate_cell(h, widths[i]) for i, h in enumerate(headers)) + " │"

    lines = [sep_top, header_line, sep_mid]
    for r in rows:
        row_cells = [truncate_cell(r[i] if i < len(r) else "", widths[i]) for i in range(len(headers))]
        lines.append("│ " + " │ ".join(row_cells) + " │")
    lines.append(sep_bot)
    return "\n".join(lines)


def stream_tsv_rows(file_path: str, offset: int = 0, limit: int = 10, country_filter: Optional[str] = None) -> Tuple[List[str], List[List[str]], int]:
    """Streams rows directly from TSV without loading large files into memory."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    headers = []
    rows = []
    total_matched = 0

    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        reader = csv.reader(f, delimiter="\t")
        try:
            headers = next(reader)
        except StopIteration:
            return [], [], 0

        country_idx = -1
        for idx, h in enumerate(headers):
            if h.strip().lower() == "country":
                country_idx = idx
                break

        current_idx = 0
        for line in reader:
            if not line:
                continue

            # Country filter check
            if country_filter and country_idx != -1 and len(line) > country_idx:
                if line[country_idx].strip().lower() != country_filter.strip().lower():
                    continue

            if current_idx >= offset and len(rows) < limit:
                rows.append(line)

            total_matched += 1
            current_idx += 1

            # Early break when we have enough rows and don't need exact full count
            if not country_filter and len(rows) >= limit:
                break

    return headers, rows, total_matched


def find_entity_by_id(file_path: str, target_id: str) -> Optional[Tuple[List[str], List[str]]]:
    """Scans TSV for a specific entity ID without loading file into memory."""
    if not os.path.exists(file_path):
        return None

    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        reader = csv.reader(f, delimiter="\t")
        try:
            headers = next(reader)
        except StopIteration:
            return None

        target_clean = target_id.strip().lower()
        for row in reader:
            if row and row[0].strip().lower() == target_clean:
                return headers, row

    return None


def show_overview():
    """Prints a verified summary table of all dataset TSV files in the workspace."""
    print("=" * 88)
    print("   AWS ML CHALLENGE 2026: VERIFIED TSV DATASET SUMMARY (ZERO-COPY READ-ONLY)")
    print("=" * 88)

    summary_headers = ["Dataset Key", "Split", "File Name", "Size (MB)", "Status"]
    summary_rows = []

    for key, path in TSV_FILES.items():
        split = "train" if "train" in key else "test"
        filename = os.path.basename(path)
        if os.path.exists(path):
            size_mb = f"{os.path.getsize(path) / (1024 * 1024):.1f} MB"
            status = "Verified Present (TSV)"
        else:
            size_mb = "N/A"
            status = "Missing"
        summary_rows.append([key, split, filename, size_mb, status])

    print(format_table(summary_headers, summary_rows))
    print("\nSample Preview: 'train_source1.tsv' (First 5 records):")
    h, r, _ = stream_tsv_rows(TSV_FILES["train_source1"], offset=0, limit=5)
    print(format_table(h, r))


def run_interactive_html_viewer(port: int = 8080):
    """Launches a local zero-copy HTTP viewer for visual IDE table browsing."""
    from http.server import HTTPServer, BaseHTTPRequestHandler
    import urllib.parse

    html_template = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8"/>
<title>AWS Dataset TSV Viewer</title>
<style>
  :root {
    --bg: #0d1117; --panel: #161b22; --border: #30363d;
    --text: #c9d1d9; --accent: #58a6ff; --accent-glow: #1f6feb;
    --highlight: #238636;
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, monospace;
    background: var(--bg); color: var(--text); margin: 0; padding: 20px;
  }
  .header { display: flex; align-items: center; justify-content: space-between; border-bottom: 1px solid var(--border); padding-bottom: 14px; margin-bottom: 16px; }
  h1 { font-size: 18px; margin: 0; color: var(--accent); }
  .controls { display: flex; gap: 10px; align-items: center; flex-wrap: wrap; }
  select, input, button {
    background: var(--panel); border: 1px solid var(--border); color: var(--text);
    padding: 6px 12px; border-radius: 6px; font-size: 13px; font-family: inherit;
  }
  button { background: var(--accent-glow); color: #fff; cursor: pointer; border: none; font-weight: 600; }
  button:hover { opacity: 0.9; }
  .table-container { overflow-x: auto; background: var(--panel); border: 1px solid var(--border); border-radius: 8px; margin-top: 12px; }
  table { width: 100%; border-collapse: collapse; font-size: 12px; }
  th { background: #21262d; color: var(--accent); text-align: left; padding: 10px 14px; border-bottom: 1px solid var(--border); font-weight: 600; white-space: nowrap; }
  td { padding: 9px 14px; border-bottom: 1px solid var(--border); white-space: nowrap; max-width: 450px; overflow: hidden; text-overflow: ellipsis; }
  tr:hover { background: #1f242c; }
  .badge { display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 11px; font-weight: bold; background: #388bfd33; color: #58a6ff; }
  .badge-india { background: #d2992233; color: #e3b341; }
  .badge-us { background: #3fb95033; color: #3fb950; }
  .badge-france { background: #bc8cff33; color: #d2a8ff; }
  .footer { margin-top: 12px; font-size: 12px; color: #8b949e; display: flex; justify-content: space-between; }
</style>
</head>
<body>
<div class="header">
  <h1>⚡ AWS Dataset TSV Grid Explorer</h1>
  <div class="controls">
    <form method="GET" style="display: flex; gap: 8px;">
      <select name="file" onchange="this.form.submit()">
        {file_options}
      </select>
      <input type="text" name="country" placeholder="Country filter..." value="{current_country}" size="10"/>
      <input type="number" name="offset" placeholder="Offset" value="{current_offset}" style="width: 70px;"/>
      <input type="number" name="limit" placeholder="Limit" value="{current_limit}" style="width: 60px;"/>
      <button type="submit">Filter Rows</button>
    </form>
  </div>
</div>

<div class="table-container">
  <table>
    <thead><tr>{table_headers}</tr></thead>
    <tbody>{table_rows}</tbody>
  </table>
</div>

<div class="footer">
  <div>Showing rows {current_offset} to {row_end} from <code>{current_file_name}</code></div>
  <div>Read-only stream directly from <code>AWS_dataset/</code> (Zero file duplication)</div>
</div>
</body>
</html>"""

    class ViewerHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            parsed = urllib.parse.urlparse(self.path)
            query = urllib.parse.parse_qs(parsed.query)

            file_key = query.get("file", ["train_source1"])[0]
            country = query.get("country", [""])[0]
            try:
                offset = int(query.get("offset", [0])[0])
            except ValueError:
                offset = 0
            try:
                limit = int(query.get("limit", [50])[0])
            except ValueError:
                limit = 50

            target_path = TSV_FILES.get(file_key, TSV_FILES["train_source1"])
            headers, rows, _ = stream_tsv_rows(target_path, offset=offset, limit=limit, country_filter=country or None)

            # Build options
            opts = []
            for k in TSV_FILES.keys():
                sel = 'selected="selected"' if k == file_key else ""
                opts.append(f'<option value="{k}" {sel}>{k}.tsv</option>')
            file_options = "\n".join(opts)

            # Headers
            th_cells = "".join(f"<th>{h}</th>" for h in headers)

            # Rows
            tb_rows = []
            for r in rows:
                tds = []
                for idx, cell in enumerate(r):
                    val = str(cell)
                    if idx < len(headers) and headers[idx].lower() == "country":
                        cls_b = "badge-india" if val == "India" else "badge-us" if val == "US" else "badge-france"
                        tds.append(f'<td><span class="badge {cls_b}">{val}</span></td>')
                    else:
                        tds.append(f"<td>{val}</td>")
                tb_rows.append(f"<tr>{''.join(tds)}</tr>")
            table_rows = "\n".join(tb_rows) if tb_rows else "<tr><td colspan='10' style='text-align:center;'>No matching records</td></tr>"

            content = html_template.format(
                file_options=file_options,
                current_country=country,
                current_offset=offset,
                current_limit=limit,
                table_headers=th_cells,
                table_rows=table_rows,
                row_end=offset + len(rows),
                current_file_name=os.path.basename(target_path),
            )

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(content.encode("utf-8"))

        def log_message(self, format, *args):
            return  # Suppress console noise

    server = HTTPServer(("127.0.0.1", port), ViewerHandler)
    print(f"\n🚀 [Interactive Web Grid Viewer Live] http://127.0.0.1:{port}")
    print("   Open this URL in your IDE browser or web browser for full visual spreadsheet exploration.")
    print("   Press Ctrl+C to terminate the viewer.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nViewer stopped.")


def main():
    parser = argparse.ArgumentParser(description="Zero-Copy TSV Dataset Viewer for IDE & Terminal")
    parser.add_argument("--file", help="Specific TSV dataset key (e.g. train_source1, test_source1, train_ground_truth)")
    parser.add_argument("--split", choices=["train", "test"], help="Dataset split (train or test)")
    parser.add_argument("--source", choices=["source1", "source2", "source3", "ground_truth"], help="Source identifier")
    parser.add_argument("--limit", type=int, default=10, help="Number of rows to display (default: 10)")
    parser.add_argument("--offset", type=int, default=0, help="Starting row offset (default: 0)")
    parser.add_argument("--country", help="Filter by country (e.g. US, India, France)")
    parser.add_argument("--id", help="Lookup a specific entity ID (e.g. S1-925783039)")
    parser.add_argument("--ground-truth", help="Lookup matching records for a Source 1 entity ID")
    parser.add_argument("--web", action="store_true", help="Launch interactive local web grid viewer on http://127.0.0.1:8080")
    parser.add_argument("--port", type=int, default=8080, help="Port for local web viewer")

    args = parser.parse_args()

    if args.web:
        run_interactive_html_viewer(port=args.port)
        return

    # Direct Entity Lookup
    if args.id:
        target_id = args.id.strip()
        print(f"\nSearching for entity: '{target_id}'...")
        found = False
        for key, path in TSV_FILES.items():
            if "ground_truth" in key:
                continue
            res = find_entity_by_id(path, target_id)
            if res:
                h, r = res
                print(f"Found in {key} ({path}):")
                print(format_table(h, [r]))
                found = True
                break
        if not found:
            print(f"Entity '{target_id}' not found in source files.")
        return

    # Ground Truth Lookup
    if args.ground_truth:
        s1_id = args.ground_truth.strip()
        gt_path = TSV_FILES["train_ground_truth"]
        res = find_entity_by_id(gt_path, s1_id)
        if not res:
            print(f"Source 1 ID '{s1_id}' not found in train_ground_truth.tsv")
            return
        h_gt, r_gt = res
        print(f"\n[Ground Truth Mapping for {s1_id}]")
        print(format_table(h_gt, [r_gt]))

        # Also fetch the S1 record
        s1_rec = find_entity_by_id(TSV_FILES["train_source1"], s1_id)
        if s1_rec:
            print("\n[Source 1 Reference Entity]:")
            print(format_table(s1_rec[0], [s1_rec[1]]))

        # Fetch matched records
        matched_ids = [x.strip() for x in r_gt[1].split(",") if x.strip()]
        if matched_ids:
            print(f"\n[Matched Target Entities ({len(matched_ids)} total)]:")
            for m_id in matched_ids:
                if m_id.startswith("S2-"):
                    m_rec = find_entity_by_id(TSV_FILES["train_source2"], m_id)
                elif m_id.startswith("S3-"):
                    m_rec = find_entity_by_id(TSV_FILES["train_source3"], m_id)
                else:
                    m_rec = None
                if m_rec:
                    print(format_table(m_rec[0], [m_rec[1]]))
        else:
            print("  (Singleton: No true matches in S2 or S3)")
        return

    # Specific file selection
    file_key = None
    if args.file:
        file_key = args.file
    elif args.split and args.source:
        file_key = f"{args.split}_{args.source}"

    if file_key:
        if file_key not in TSV_FILES:
            print(f"Invalid dataset key '{file_key}'. Available: {list(TSV_FILES.keys())}")
            sys.exit(1)
        path = TSV_FILES[file_key]
        print(f"\nDataset: {file_key} ({os.path.basename(path)}) | Offset: {args.offset} | Limit: {args.limit}")
        if args.country:
            print(f"Filter Country: {args.country}")
        h, r, total = stream_tsv_rows(path, offset=args.offset, limit=args.limit, country_filter=args.country)
        print(format_table(h, r))
        return

    # Default: Show summary and sample
    show_overview()


if __name__ == "__main__":
    main()
