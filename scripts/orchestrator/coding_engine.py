"""
Task 2: Autonomous TDD & Self-Healing Coding Engine
Implements the closed-loop engineering workflow:
1. Contracts first (TDD test authoring).
2. Business logic implementation (zero lazy placeholders).
3. Test execution with automated traceback capture.
4. Autonomous error self-healing loop (up to 5 passes) until 100% green.
5. Emits empirical benchmark logs and persists results to SQLite Memory Vault.
"""

import os
import sys
import json
import time
import sqlite3
import subprocess
from typing import Dict, Any, List, Optional, Callable

from scripts.orchestrator.sandbox_bridge import SandboxBridge, SandboxResult


class CodingEngine:
    """
    Autonomous engineering engine that writes, tests, and self-heals software code
    inside an isolated sandbox jail with zero human hand-holding.
    """

    @classmethod
    def execute_tdd_loop(
        cls,
        module_name: str,
        test_file_path: str,
        test_code: str,
        impl_file_path: str,
        impl_code_generator: Callable[[int, Optional[str]], str],
        max_healing_passes: int = 5,
        sandbox_timeout: int = 30
    ) -> Dict[str, Any]:
        """
        Executes an autonomous TDD self-healing loop inside the Sandbox Process Jail:
        1. Writes test file.
        2. Writes initial implementation.
        3. Runs test runner through SandboxBridge.
        4. If failing, passes traceback to impl_code_generator and re-patches until exit code 0.
        """
        return cls.execute_multi_file_tdd_loop(
            module_name=module_name,
            test_file_path=test_file_path,
            test_code=test_code,
            multi_file_generator=lambda it, err: {impl_file_path: impl_code_generator(it, err)},
            max_healing_passes=max_healing_passes,
            sandbox_timeout=sandbox_timeout
        )

    @classmethod
    def execute_multi_file_tdd_loop(
        cls,
        module_name: str,
        test_file_path: str,
        test_code: str,
        multi_file_generator: Callable[[int, Optional[str]], Dict[str, str]],
        max_healing_passes: int = 5,
        sandbox_timeout: int = 30
    ) -> Dict[str, Any]:
        """
        Executes multi-file dependency-aware TDD self-healing:
        Atomically patches cross-module source files, tests against contracts,
        and heals errors with rollback protection.
        """
        os.makedirs(os.path.dirname(os.path.abspath(test_file_path)), exist_ok=True)

        # 1. Write TDD test file
        with open(test_file_path, "w", encoding="utf-8") as f:
            f.write(test_code)

        iteration = 1
        last_error = None
        start_time = time.time()
        success = False
        last_sandbox_res: Optional[SandboxResult] = None
        patched_files_list: List[str] = []

        # Snapshots for rollback protection
        snapshots: Dict[str, Optional[str]] = {}

        while iteration <= max_healing_passes:
            current_files = multi_file_generator(iteration, last_error)
            patched_files_list = list(current_files.keys())

            # Take snapshot before first modification
            for fpath in current_files.keys():
                if fpath not in snapshots:
                    if os.path.exists(fpath):
                        with open(fpath, "r", encoding="utf-8") as f_snap:
                            snapshots[fpath] = f_snap.read()
                    else:
                        snapshots[fpath] = None

            # Transactional write
            for fpath, fcontent in current_files.items():
                os.makedirs(os.path.dirname(os.path.abspath(fpath)), exist_ok=True)
                with open(fpath, "w", encoding="utf-8") as f:
                    f.write(fcontent)

            # Determine runner (Python unittest vs Node test)
            if test_file_path.endswith(".py"):
                cmd = [sys.executable, "-m", "unittest", test_file_path]
            elif test_file_path.endswith(".ts") or test_file_path.endswith(".js"):
                cmd = ["node", "--experimental-strip-types", "--test", test_file_path]
            else:
                cmd = [sys.executable, test_file_path]

            print(f"[CodingEngine] Iteration {iteration}/{max_healing_passes} [Sandbox Jail]: Running {' '.join(cmd)}...")
            res = SandboxBridge.execute(cmd, timeout_seconds=sandbox_timeout)
            last_sandbox_res = res

            if res.returncode == 0:
                print(f"[CodingEngine] SUCCESS! 100% Green on iteration {iteration} in {res.duration_seconds}s!")
                success = True
                break
            else:
                if res.timed_out:
                    last_error = f"Execution timed out after {res.duration_seconds}s (Host Process Jail protection limit reached)."
                else:
                    last_error = res.stderr or res.stdout
                print(f"[CodingEngine] Warning: Iteration {iteration} failed (code {res.returncode}). Triggering self-healing patch...")
                iteration += 1

        duration_sec = round(time.time() - start_time, 3)

        if not success:
            # Rollback snapshots if failed all iterations
            print("[CodingEngine] Rolling back files to pre-patch state due to unresolvable errors...")
            for fpath, orig_content in snapshots.items():
                if orig_content is None:
                    if os.path.exists(fpath):
                        os.remove(fpath)
                else:
                    with open(fpath, "w", encoding="utf-8") as f_orig:
                        f_orig.write(orig_content)

            raise RuntimeError(
                f"CodingEngine failed to self-heal code after {max_healing_passes} iterations. "
                f"Last error:\n{last_error}"
            )

        # 2. Emit Empirical Benchmark Metrics
        metrics_path = "specs/benchmark_metrics.json"
        os.makedirs(os.path.dirname(os.path.abspath(metrics_path)), exist_ok=True)
        benchmark_payload = {
            "module": module_name,
            "patched_files": patched_files_list,
            "test_file": test_file_path,
            "healing_iterations_needed": iteration,
            "execution_duration_sec": duration_sec,
            "sandbox_mode": last_sandbox_res.sandbox_mode if last_sandbox_res else "process_jail",
            "status": "VERIFIED_GREEN",
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        with open(metrics_path, "w", encoding="utf-8") as f:
            json.dump(benchmark_payload, f, indent=2)

        # 3. Persist to Memory Vault
        cls._record_in_memory_vault(
            title=f"TDD Implementation Verified: {module_name}",
            kind="fact",
            body=f"Engine verified {module_name} 100% green in {duration_sec}s across {iteration} iterations via {benchmark_payload['sandbox_mode']}.",
            file_path=patched_files_list[0] if patched_files_list else test_file_path
        )

        return benchmark_payload

    @classmethod
    def _record_in_memory_vault(cls, title: str, kind: str, body: str, file_path: str) -> None:
        """Stores verification fact directly in .agents/memory/vault.sqlite."""
        db_dir = os.path.join(os.getcwd(), ".agents", "memory")
        os.makedirs(db_dir, exist_ok=True)
        db_path = os.path.join(db_dir, "vault.sqlite")

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
            mem_id = f"mem-{int(time.time())}-{abs(hash(title)) % 1000}"
            cur.execute("""
                INSERT OR REPLACE INTO memories 
                (id, title, kind, scope, phase, operator, tags, created_at, body, file_path)
                VALUES (?, ?, ?, 'project', 1, 'CodingEngine', 'code,tdd,verified', datetime('now'), ?, ?);
            """, (mem_id, title, kind, body, file_path))
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"[CodingEngine] Memory vault recording notice: {e}")
