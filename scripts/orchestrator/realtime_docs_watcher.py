"""
Real-Time Documentation Watcher Daemon & Brain Artifact Synchronizer
Continuously monitors active Antigravity IDE brain conversation directories and
instantly synchronizes:
- implementation_plan.md -> docs/plans/
- walkthrough.md        -> docs/walkthroughs/
- *_audit.md            -> docs/audits/

Guarantees:
1. Exact real-time execution timestamps (YYYY-MM-DD_HH-MM-SS) down to the second.
2. Human-meaningful slug and title extraction from markdown headers.
3. Content-hash deduplication (SHA-256) preventing redundant disk writes.
4. Automatic update of living INDEX.md catalogs and SQLite Memory Vault.
"""

import os
import sys
import time
import hashlib
import argparse
from typing import Dict, Optional, Tuple

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

from scripts.orchestrator.spec_sync import SpecSync


class RealtimeDocsWatcher:
    """
    Watches IDE brain directories and autonomously synchronizes artifacts to in-repo docs/.
    """

    def __init__(self, brain_dir: Optional[str] = None, poll_interval: float = 1.5):
        self.brain_dir = brain_dir
        self.poll_interval = poll_interval
        self._file_hashes: Dict[str, str] = {}
        self._running = False

    def get_active_brain_dir(self) -> Optional[str]:
        if self.brain_dir and os.path.exists(self.brain_dir):
            return self.brain_dir
        app_data = os.path.expanduser(r"~\.gemini\antigravity-ide\brain")
        if not os.path.exists(app_data):
            return None
        dirs = [
            os.path.join(app_data, d) for d in os.listdir(app_data)
            if os.path.isdir(os.path.join(app_data, d)) and not d.startswith(".") and d != "tempmediaStorage"
        ]
        if not dirs:
            return None
        # Sort by latest modification time
        dirs.sort(key=lambda p: os.path.getmtime(p), reverse=True)
        return dirs[0]

    def _compute_hash(self, content: str) -> str:
        return hashlib.sha256(content.encode("utf-8")).hexdigest()

    def sync_once(self) -> int:
        target_dir = self.get_active_brain_dir()
        if not target_dir or not os.path.exists(target_dir):
            return 0

        synced_count = 0

        # Monitored artifacts mapping: filename -> doc_type
        artifacts_to_watch = {
            "implementation_plan.md": "plan",
            "walkthrough.md": "walkthrough"
        }

        # Check standard artifacts
        for fname, doc_type in artifacts_to_watch.items():
            fpath = os.path.join(target_dir, fname)
            if os.path.exists(fpath):
                try:
                    with open(fpath, "r", encoding="utf-8") as f:
                        content = f.read()
                    if content.strip():
                        chash = self._compute_hash(content)
                        if self._file_hashes.get(fpath) != chash:
                            mtime = os.path.getmtime(fpath)
                            title, slug = SpecSync._extract_title_and_slug(content, fname.replace(".md", ""))
                            dest = SpecSync.persist_document(doc_type, slug, content, title, custom_timestamp=mtime)
                            self._file_hashes[fpath] = chash
                            synced_count += 1
                            ts_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(mtime))
                            print(f"⚡ [RealtimeDocsWatcher] Synced {fname} -> {dest} (Timestamp: {ts_str})")
                except Exception as e:
                    print(f"⚠️ [RealtimeDocsWatcher] Error reading {fpath}: {e}")

        # Check for any dynamic audits or research artifacts
        for fname in os.listdir(target_dir):
            if fname.endswith(("_audit.md", "-audit.md")) and not fname.startswith("implementation_"):
                fpath = os.path.join(target_dir, fname)
                try:
                    with open(fpath, "r", encoding="utf-8") as f:
                        content = f.read()
                    if content.strip():
                        chash = self._compute_hash(content)
                        if self._file_hashes.get(fpath) != chash:
                            mtime = os.path.getmtime(fpath)
                            audit_name = fname.replace(".md", "").replace("_audit", "")
                            title, slug = SpecSync._extract_title_and_slug(content, audit_name)
                            dest = SpecSync.persist_audit(slug, content, title, custom_timestamp=mtime)
                            self._file_hashes[fpath] = chash
                            synced_count += 1
                            print(f"⚡ [RealtimeDocsWatcher] Synced audit {fname} -> {dest}")
                except Exception:
                    pass

        return synced_count

    def watch(self) -> None:
        self._running = True
        active_dir = self.get_active_brain_dir()
        print("================================================================================")
        print("👁️  [REALTIME DOCS WATCHER] Monitoring Active IDE Brain Artifact Directory")
        print(f"   Target Brain Folder : {active_dir}")
        print(f"   Poll Interval       : {self.poll_interval}s")
        print("   Destination Folders : docs/plans/, docs/walkthroughs/, docs/audits/")
        print("   Timestamp Precision : Full Real-Time (YYYY-MM-DD_HH-MM-SS)")
        print("================================================================================")

        # Initial baseline sync
        initial_syncs = self.sync_once()
        if initial_syncs > 0:
            print(f"✅ Baseline sync complete: {initial_syncs} document(s) synchronized.")

        try:
            while self._running:
                time.sleep(self.poll_interval)
                self.sync_once()
        except KeyboardInterrupt:
            print("\n🛑 [RealtimeDocsWatcher] Stopping file watcher gracefully.")
            self._running = False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Real-Time Documentation Watcher Daemon")
    parser.add_argument("--brain-dir", help="Custom brain conversation directory path to watch")
    parser.add_argument("--interval", type=float, default=1.5, help="Polling interval in seconds")
    parser.add_argument("--once", action="store_true", help="Execute single synchronization pass and exit")
    args = parser.parse_args()

    watcher = RealtimeDocsWatcher(brain_dir=args.brain_dir, poll_interval=args.interval)
    if args.once:
        count = watcher.sync_once()
        print(f"✅ One-pass sync complete: {count} document(s) synchronized.")
        sys.exit(0)
    else:
        watcher.watch()
