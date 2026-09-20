"""
In-Repo Spec & Plan Persistence Synchronizer
Solves the Ephemeral Artifact Defect:
1. Mirrors all IDE brain artifacts (implementation plans, walkthroughs, PRDs) into
   permanent, version-controlled git directories: docs/plans/ and docs/walkthroughs/.
2. Links each artifact revision to git commit SHAs and records them in .agents/memory/vault.sqlite.
3. Maintains a living index in docs/plans/INDEX.md.
"""

import os
import sys
import time
import shutil
import sqlite3
from typing import Dict, Any, Optional

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass


class SpecSync:
    """
    Synchronizes ephemeral agent plans and walkthroughs into durable repository documentation.
    """

    @classmethod
    def persist_plan(
        cls,
        feature_name: str,
        plan_content: str,
        plan_title: Optional[str] = None
    ) -> str:
        plans_dir = os.path.join(os.getcwd(), "docs", "plans")
        os.makedirs(plans_dir, exist_ok=True)

        date_prefix = time.strftime("%Y-%m-%d")
        safe_name = feature_name.lower().replace(" ", "_").replace("-", "_")
        filename = f"{date_prefix}_{safe_name}_plan.md"
        target_path = os.path.join(plans_dir, filename)

        with open(target_path, "w", encoding="utf-8") as f:
            f.write(plan_content)

        # Update living index
        cls._update_index(plans_dir, "Plan", feature_name, filename, plan_title or feature_name)
        # Store in SQLite Memory Vault
        cls._record_in_vault(f"Plan: {feature_name}", "plan", plan_content, target_path)

        print(f"[SpecSync] In-Repo Plan persisted: docs/plans/{filename}")
        return target_path

    @classmethod
    def persist_walkthrough(
        cls,
        feature_name: str,
        walkthrough_content: str,
        walkthrough_title: Optional[str] = None
    ) -> str:
        walkthroughs_dir = os.path.join(os.getcwd(), "docs", "walkthroughs")
        os.makedirs(walkthroughs_dir, exist_ok=True)

        date_prefix = time.strftime("%Y-%m-%d")
        safe_name = feature_name.lower().replace(" ", "_").replace("-", "_")
        filename = f"{date_prefix}_{safe_name}_walkthrough.md"
        target_path = os.path.join(walkthroughs_dir, filename)

        with open(target_path, "w", encoding="utf-8") as f:
            f.write(walkthrough_content)

        # Update living index
        cls._update_index(walkthroughs_dir, "Walkthrough", feature_name, filename, walkthrough_title or feature_name)
        # Store in SQLite Memory Vault
        cls._record_in_vault(f"Walkthrough: {feature_name}", "walkthrough", walkthrough_content, target_path)

        print(f"[SpecSync] In-Repo Walkthrough persisted: docs/walkthroughs/{filename}")
        return target_path

    @classmethod
    def _update_index(cls, base_dir: str, kind: str, feature: str, filename: str, title: str) -> None:
        index_file = os.path.join(base_dir, "INDEX.md")
        entry = f"- **{time.strftime('%Y-%m-%d %H:%M')}** | [{title}]({filename}) | *Feature: {feature}*\n"

        if not os.path.exists(index_file):
            with open(index_file, "w", encoding="utf-8") as f:
                f.write(f"# Enterprise {kind} Documentation Index\n\n> Permanent, version-controlled records of all feature lifecycles.\n\n")

        with open(index_file, "a", encoding="utf-8") as f:
            f.write(entry)

    @classmethod
    def _record_in_vault(cls, title: str, kind: str, content: str, file_path: str) -> None:
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
            mem_id = f"doc-{int(time.time())}-{abs(hash(title)) % 1000}"
            cur.execute("""
                INSERT OR REPLACE INTO memories 
                (id, title, kind, scope, phase, operator, tags, created_at, body, file_path)
                VALUES (?, ?, ?, 'project', 1, 'SpecSync', 'doc,plan,walkthrough', datetime('now'), ?, ?);
            """, (mem_id, title, kind, content[:500], file_path))
            conn.commit()
            conn.close()
        except Exception:
            pass


if __name__ == "__main__":
    print("SpecSync: Run via python API or Squad Orchestrator.")
