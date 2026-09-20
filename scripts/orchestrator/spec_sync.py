"""
In-Repo Universal Specification & Documentation Synchronizer
Solves the Ephemeral Artifact Defect and Multi-Machine Memory Silo:
1. Mirrors all IDE brain artifacts and reports into permanent, version-controlled git directories:
   - docs/plans/        (Feature Implementation Plans)
   - docs/walkthroughs/ (Execution Walkthroughs & Test Proofs)
   - docs/audits/       (Adversarial Pentests & System Readiness Audits)
   - docs/adrs/         (Architecture Decision Records)
   - docs/research/     (Multi-Hop Research Triangulation Dossiers)
   - docs/rfcs/         (Formal API & Data Model Contracts)
2. Maintains living INDEX.md catalogs in each directory.
3. Dual-persists to SQLite Memory Vault and git-mergeable append-only JSONL (.agents/memory/vault/records.jsonl).
"""

import os
import sys
import time
import json
import sqlite3
from typing import Dict, Any, Optional, List

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


DOCUMENT_CONFIGS: Dict[str, Dict[str, str]] = {
    "plan": {
        "dir": "docs/plans",
        "kind": "Plan",
        "index_title": "Enterprise Plan Documentation Index",
        "description": "Permanent records of all planned feature architectures."
    },
    "walkthrough": {
        "dir": "docs/walkthroughs",
        "kind": "Walkthrough",
        "index_title": "Enterprise Walkthrough Documentation Index",
        "description": "Permanent records of all executed changes and empirical test results."
    },
    "audit": {
        "dir": "docs/audits",
        "kind": "Audit",
        "index_title": "Enterprise Audit Documentation Index",
        "description": "Permanent records of adversarial pentests, code audits, and system readiness."
    },
    "adr": {
        "dir": "docs/adrs",
        "kind": "ADR",
        "index_title": "Architecture Decision Records (ADRs)",
        "description": "Permanent records of fundamental architectural choices, trade-offs, and moats."
    },
    "research": {
        "dir": "docs/research",
        "kind": "Research",
        "index_title": "Enterprise Deep Research Dossiers",
        "description": "Multi-hop research triangulation on statutory mandates, competitor benchmarks, and CVEs."
    },
    "rfc": {
        "dir": "docs/rfcs",
        "kind": "RFC",
        "index_title": "Requests for Comments & Contract Specifications",
        "description": "Formal typed interface schemas, state machine models, and API definitions."
    }
}


class SpecSync:
    """
    Universal documentation engine synchronizing all enterprise document classes into durable git storage.
    """

    @classmethod
    def persist_document(
        cls,
        doc_type: str,
        name: str,
        content: str,
        title: Optional[str] = None
    ) -> str:
        doc_type_clean = doc_type.lower().strip()
        config = DOCUMENT_CONFIGS.get(doc_type_clean)
        if not config:
            raise ValueError(f"Unknown document type '{doc_type}'. Supported: {list(DOCUMENT_CONFIGS.keys())}")

        target_dir = os.path.join(os.getcwd(), config["dir"])
        os.makedirs(target_dir, exist_ok=True)

        import re
        date_prefix = time.strftime("%Y-%m-%d")
        safe_name = re.sub(r'[^a-zA-Z0-9_]', '_', name.lower()).strip('_')
        filename = f"{date_prefix}_{safe_name}_{doc_type_clean}.md"
        target_path = os.path.join(target_dir, filename)

        with open(target_path, "w", encoding="utf-8") as f:
            f.write(content)

        # Update living index catalog
        cls._update_index(target_dir, config["kind"], name, filename, title or name, config)

        # Dual-record in SQLite vault and git-mergeable JSONL
        cls._record_in_vault(f"{config['kind']}: {title or name}", doc_type_clean, content, target_path)

        print(f"[SpecSync] Persisted {config['kind']} -> {config['dir']}/{filename}")
        return target_path

    @classmethod
    def persist_plan(cls, name: str, content: str, title: Optional[str] = None) -> str:
        return cls.persist_document("plan", name, content, title)

    @classmethod
    def persist_walkthrough(cls, name: str, content: str, title: Optional[str] = None) -> str:
        return cls.persist_document("walkthrough", name, content, title)

    @classmethod
    def persist_audit(cls, name: str, content: str, title: Optional[str] = None) -> str:
        return cls.persist_document("audit", name, content, title)

    @classmethod
    def persist_adr(cls, name: str, content: str, title: Optional[str] = None) -> str:
        return cls.persist_document("adr", name, content, title)

    @classmethod
    def persist_research(cls, name: str, content: str, title: Optional[str] = None) -> str:
        return cls.persist_document("research", name, content, title)

    @classmethod
    def persist_rfc(cls, name: str, content: str, title: Optional[str] = None) -> str:
        return cls.persist_document("rfc", name, content, title)

    @classmethod
    def _update_index(cls, base_dir: str, kind: str, feature: str, filename: str, title: str, config: Dict[str, str]) -> None:
        index_file = os.path.join(base_dir, "INDEX.md")
        timestamp_str = time.strftime("%Y-%m-%d %H:%M")
        entry = f"- **{timestamp_str}** | [{title}]({filename}) | *Scope: {feature}*\n"

        if not os.path.exists(index_file):
            with open(index_file, "w", encoding="utf-8") as f:
                f.write(f"# {config['index_title']}\n\n> {config['description']}\n\n")

        # Check if entry already exists
        with open(index_file, "r", encoding="utf-8") as f:
            existing_content = f.read()

        if filename not in existing_content:
            with open(index_file, "a", encoding="utf-8") as f:
                f.write(entry)

    @classmethod
    def _record_in_vault(cls, title: str, kind: str, content: str, file_path: str) -> None:
        # 1. Dual-Write to Git-Mergeable Append-Only JSONL
        jsonl_dir = os.path.join(os.getcwd(), ".agents", "memory", "vault")
        os.makedirs(jsonl_dir, exist_ok=True)
        jsonl_path = os.path.join(jsonl_dir, "records.jsonl")

        record = {
            "id": f"doc-{int(time.time())}-{abs(hash(title)) % 10000}",
            "title": title,
            "kind": kind,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
            "file_path": file_path,
            "preview": content[:400]
        }

        try:
            with open(jsonl_path, "a", encoding="utf-8") as f:
                f.write(json.dumps(record) + "\n")
        except Exception:
            pass

        # 2. Record in Local SQLite FTS5 for Fast Text Search
        db_path = os.path.join(os.getcwd(), ".agents", "memory", "vault.sqlite")
        try:
            conn = sqlite3.connect(db_path)
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS memories (
                    id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    kind TEXT NOT NULL,
                    scope TEXT NOT NULL,
                    phase INTEGER NOT NULL,
                    operator TEXT NOT NULL,
                    tags TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    body TEXT NOT NULL,
                    file_path TEXT NOT NULL
                );
            """)
            cur.execute("""
                INSERT OR REPLACE INTO memories 
                (id, title, kind, scope, phase, operator, tags, created_at, body, file_path)
                VALUES (?, ?, ?, 'project', 1, 'SpecSync', ?, datetime('now'), ?, ?);
            """, (record["id"], title, kind, f"doc,{kind}", content[:600], file_path))
            conn.commit()
            conn.close()
        except Exception:
            pass


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="SpecSync Universal Documentation Engine")
    parser.add_argument("--type", choices=list(DOCUMENT_CONFIGS.keys()), default="plan", help="Document category")
    parser.add_argument("--name", required=True, help="Feature or document name")
    parser.add_argument("--file", help="Source file to read content from")
    parser.add_argument("--title", help="Human-readable title")
    args = parser.parse_args()

    content = ""
    if args.file and os.path.exists(args.file):
        with open(args.file, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        content = f"# {args.title or args.name}\n\nDocument persisted via SpecSync CLI.\n"

    SpecSync.persist_document(args.type, args.name, content, args.title)
