# Antigravity Universal Multi-Agent System — Master Command Cheat Sheet

> **Quick Navigation**: Use this guide to assign tasks directly to the Antigravity agent or execute CLI commands in PowerShell / terminal.  
> **System Status**: Fully Operational & 100% Green (53/53 Backend Pytest with 95% Coverage + 2/2 Headless Playwright E2E Suites + Bandit SAST Clean + 80/80 Multi-Agent Python Suites + 6/6 Master Audit Trail Gates)  

---

## 0. Human Operator Quick-Start: Fresh Project Usage Guide

When cloning this repository as a starter template for new projects:

### 1. Clone & Initialize
```bash
git clone https://github.com/Deepak-Sharma-2006/AWS.git my-new-project
cd my-new-project
npm install
```

### 2. Verify Dual-Scope Scale
```bash
npm run project:scale
# Output: 🟢 SMALL (<5k LOC) based on your src/ files
```

### 3. Check Active Context & Headroom
```bash
npm run context:check
# Displays active post-compaction context tokens and compaction headroom
```

### 4. Synchronize Brain Artifacts (Zero Background Overhead)
```bash
npm run docs:sync
# Sub-second turn-egress mirroring from IDE brain to docs/ catalogs
```

### 5. Start Fresh Chat Sessions Confidently
Start each major feature phase in a new chat. The agent reads `docs/*/INDEX.md` and the latest walkthrough (~2,000 tokens) to re-ground immediately without re-ingesting stale conversation transcripts.

---

## 1. Core Task Execution Commands

### Task 1: Solution Formulation, White-Space Moat & Cloud Unit Economics
Deconstructs a problem statement, conducts multi-hop live research triangulation (statutory regulations, live competitors, CVE failure paths), benchmarks commercial prior-art, designs a 10x technical moat, generates native visual architecture diagrams, models real cloud COGS (AWS/GCP/tokens at ≥ 75% gross margin), and records decisions to SQLite Memory Vault and git-mergeable records.

```bash
# Basic Problem Prompt (Dynamic first-principles synthesis)
python -m scripts.orchestrator.task_dispatcher --task solution --prompt "Autonomous satellite wildfire early detection"

# Detailed Problem Statement with Title & Domain
python -m scripts.orchestrator.task_dispatcher --task solution --title "PRAVAH Flood Intelligence" --prompt "Synthetic Aperture Radar flash flood forecasting" --domain "Hydrology & Disaster AI"
```
*Outputs: Automatically persisted and cataloged in:*
- `docs/plans/` & `docs/plans/INDEX.md` (Implementation Plan & Solution Dossier)
- `docs/decisions/` & `docs/decisions/INDEX.md` (Architecture Decision Record)
- `docs/research/` & `docs/research/INDEX.md` (Multi-Hop Research Triangulation Dossier)
- Dual-persisted to SQLite Memory Vault (`.agents/memory/vault.sqlite`) and JSONL (`.agents/memory/vault/records.jsonl`).

---

### Task 2: Code Implementation, Sandbox Jail & Multi-File TDD Self-Healing
Authors deterministic unit tests and extreme edge cases first (empty, null, boundary, malformed, race conditions), generates clean idiomatic code, runs tests inside the Sandbox Process Jail (Option A: 30s timeout, credential scrubbing; Option B: Docker container), auto-patches failures up to 5 passes until 100% green with transactional rollback protection, and emits benchmark metrics.

```bash
# Execute TDD self-healing loop on a specific module
python -m scripts.orchestrator.task_dispatcher --task code --module "catchment_hydraulics"
```
*Outputs: Production code in `src/`, test suites in `tests/`, benchmark metrics in `specs/benchmark_metrics.json`, and Memory Vault commit.*

---

### Task 3: Presentation Pitch Synthesis (OmniDeck Engine)
Translates technical solution dossiers and benchmarks into championship-winning presentation pitch decks using 2D Flex/Grid solvers, vector graphics, and high-fidelity UI mockups (browser chrome, mobile HUD, and 2x2 Gartner quadrant matrix).

```bash
# Stage 1: Fast PPTX Compilation (< 0.2s) - Default 6 Championship Slides
python -m scripts.orchestrator.task_dispatcher --task presentation --prompt "Sovereign Defense AI" --theme "cyber_dark_terminal" --slides 6

# Stage 1: Extended & Custom Slide Themes (sih_official_light, modern_saas_glass, deep_navy_executive)
python -m scripts.orchestrator.task_dispatcher --task presentation --prompt "Sovereign Defense AI" --theme "sih_official_light" --slides 8

# Stage 2: Gated PDF Export (Supports PowerPoint COM, headless LibreOffice, and headless Chrome fallback)
python -m scripts.orchestrator.task_dispatcher --task presentation --prompt "Sovereign Defense AI" --theme "cyber_dark_terminal" --export-pdf
```
*Outputs: Native PowerPoint deck in `specs/presentations/deck_dispatcher_output.pptx` (and PDF if `--export-pdf` passed).*

---

### Task 4 / Enterprise Product Squad: 6+1 Pillar Autonomous Squad Run
Simulates the full enterprise product team across the 9-phase SDLC: Deep Research Specialist, Product Manager, System Architect, Adversarial SDET, Core Engineer, Mutation Auditor, and Technical Writer.

```bash
# Execute end-to-end squad workflow on a target feature (PM auto-triggers pre-flight research)
python -m scripts.orchestrator.task_dispatcher --task squad --feature case_state_manager

# View live mode status (Solo vs Dual-Lead 50/50)
npm run mode:status
```

---

### Task 5: Multi-Hop Deep Research & Post-Production Impact Analysis
Executes the Deep Research Specialist across 4 modes (EXPLORATION, FEASIBILITY, DIAGNOSTIC, IMPACT) with a minimum 120-second deliberation window, keyless search connectors, Jina Reader (`r.jina.ai`) markdown parsing, and automatic living catalog persistence in `docs/research/`.

```bash
# Pre-Flight Statutory, Competitive SOTA & CVE Exploration
python -m scripts.orchestrator.task_dispatcher --task research --title "Quantum Crypto Ingestion" --domain "Cyber Defense" --research-mode EXPLORATION

# Post-Production Empirical Impact Analysis (Playwright, Pytest, Mutation, SAST metrics)
python -m scripts.orchestrator.task_dispatcher --task impact --title "Production Platform" --domain "Enterprise AI"
```
*Outputs: Deep Research Dossier in `docs/research/` and updated [`docs/research/INDEX.md`](file:///docs/research/INDEX.md).*
*Outputs: Execution proof, walkthrough dossier in `docs/walkthroughs/`, and updated living index.*

---

## 2. In-Repo Living Documentation Architecture (6 Document Classes)

Every system artifact is permanently version-controlled under `docs/` and tracked in living `INDEX.md` catalogs.

| Document Class | Directory | Living Catalog | Purpose & Contents |
| :--- | :--- | :--- | :--- |
| **Implementation Plans** | `docs/plans/` | [`docs/plans/INDEX.md`](file:///docs/plans/INDEX.md) | Feature PRDs, phase roadmaps, and execution plans |
| **Walkthroughs** | `docs/walkthroughs/` | [`docs/walkthroughs/INDEX.md`](file:///docs/walkthroughs/INDEX.md) | End-of-turn execution records, test proof, and diffs |
| **System Audits** | `docs/audits/` | [`docs/audits/INDEX.md`](file:///docs/audits/INDEX.md) | System readiness probes, adversarial red-team DAST |
| **Architecture Decisions** | `docs/decisions/` | [`docs/decisions/INDEX.md`](file:///docs/decisions/INDEX.md) | Architectural trade-offs, moats, and non-negotiables |
| **Research Dossiers** | `docs/research/` | [`docs/research/INDEX.md`](file:///docs/research/INDEX.md) | Multi-hop statutory, competitive, and CVE research |
| **Formal Specifications & Contracts** | `docs/specifications/` | [`docs/specifications/INDEX.md`](file:///docs/specifications/INDEX.md) | API schemas, data contracts, and state machines |

```bash
# Synchronize and re-index all 6 documentation catalogs
python -c "from scripts.orchestrator.spec_sync import SpecSync; print(SpecSync.get_all_indexes())"
```

---

## 3. Mutation Testing & Fail-Closed Frontend Verification

### Deterministic AST Mutation Testing (≥ 80% Kill Rate Gate)
Injects 4 fault classes (Boundary Inversions, Boolean/Logical flips, Arithmetic mutations, and Return Overrides) with atomic `.bak` rollback on abort or signal interrupts.

```bash
# Python Native AST Mutation Testing
python -m scripts.orchestrator.python_mutation_tester src/my_service.py "python -m unittest tests/test_my_service.py"

# TypeScript AST Mutation Testing
npm run test:mutation
```

### Fail-Closed Headless Playwright Verification (Maximum Elemental Accuracy)
Strictly rejects builds with exit code `1` if frontend files exist and browser tests are missing or failing. Executes against Chrome DevTools Protocol (CDP) with 100% element assertions across tabs, modals, and reactive stores.

```bash
# Run all headless Playwright E2E browser test suites
npm run test:e2e
npx playwright test

# Run Project CHAKRA National Operations E2E suite (All 5 stages, 5-tier RBAC, 0 console errors)
npm run test:e2e:chakra

# Run Project BHEDAK NTRO Sovereign Workbench E2E suite
npm run test:e2e:bhedak
```

### Master Backend Testing & Branch Coverage Suite
Executes unit, contract, and integration tests across all microservices and FastAPI endpoints with statement and branch coverage via `pytest-cov`.

```bash
# Run full backend test suite with coverage report (53/53 passed, 95% total statement coverage)
npm run test:backend
pytest demo/ --cov=demo -q

# Run backend test suite for Project CHAKRA
npm run test:backend:chakra

# Run backend test suite for Project BHEDAK
npm run test:backend:bhedak
```

### Static Application Security Testing (AppSec SAST)
Scans Python AST for security vulnerabilities, insecure interface bindings (e.g. CWE-605 `0.0.0.0`), unescaped calldata injection, and weak crypto via Bandit.

```bash
# Run Bandit SAST security audit across all demo backends
npm run audit:sast
bandit -r demo/ -ll -q
```

### Operator Empirical Proof & Squad Attestation Ledger
Provides cryptographic proof that the 6-Persona enterprise agentic workflow executed genuine tools for a prompt, recording provenance hashes to SQLite Memory Vault.

```bash
# Verify latest cryptographic execution receipts in SQLite Memory Vault (.agents/memory/vault.sqlite)
npm run attest:verify
python -m scripts.orchestrator.squad_attestation --verify

# Generate and record a manual attestation for an ad-hoc operator prompt
python -m scripts.orchestrator.squad_attestation --prompt "Your task description"
```

---


## 4. Memory Vault, Audits & Security Commands

### SQLite Memory Vault & Plain-Text JSONL Dual-Persistence
```bash
# Search indexed architectural decisions and lessons
python -m scripts.orchestrator.task_dispatcher --task memory --query "Satellite"

# Verify Memory Vault integrity
npm run memory:doctor
```

### Real-Time Documentation Synchronization & Watcher Daemon
Automatically synchronizes IDE brain conversation artifacts (implementation plans, walkthroughs, diagnostic audits) into in-repo catalogs with real-time timestamps (min & sec).

```bash
# 1. Real-time background watcher daemon (monitors active brain folder continuously)
npm run docs:watch
python -m scripts.orchestrator.realtime_docs_watcher

# 2. One-shot synchronous mirror of active brain artifacts
npm run docs:sync
python -m scripts.orchestrator.spec_sync --sync-brain

# 3. Print living documentation catalog status across all 6 document classes
python -m scripts.orchestrator.spec_sync --all-indexes
```

### Pre-Commit Secret Scanning & AppSec Red-Teaming
```bash
# Scan all staged git files for leaked secrets/tokens before committing
npm run check:secrets:staged

# Scan entire repository for secrets
npm run check:secrets

# Run Strix AI DAST Red-Team Penetration Testing
npm run pentest
```

### Case B: Audit & Remediate an Existing Project
Ingests a completed or existing project directory, runs the 5-pillar enterprise diagnostic (Architecture/Types, Edge-Case Tests, AppSec/Secrets, Financial Economics, Anti-Tamper), and optionally auto-heals P0 critical flaws.

```bash
# Audit-only (diagnostic report, no changes)
python -m scripts.orchestrator.task_dispatcher --task audit --target ./my_existing_project/

# Audit + Auto-Heal (remediate P0 critical stubs and broken tests)
python -m scripts.orchestrator.task_dispatcher --task audit --target ./my_existing_project/ --auto-heal

# Audit a standalone solution blueprint markdown file
python -m scripts.orchestrator.task_dispatcher --task audit --target docs/architecture/production_architecture_blueprint.md
```
*Outputs: Diagnostic dossier at `docs/audits/remediation_audit.md` with health score, flaw matrix, and prioritized remediation plan.*

### Case C: Onboard & Continue an In-Progress Project
Hybrid workflow: first runs Case B (audit + heal existing baseline), then continues building unimplemented modules via TDD.

```bash
# Onboard a cloned/unzipped in-progress repo and continue building
python -m scripts.orchestrator.task_dispatcher --task continue --target ./cloned_repo/
```
*Outputs: Stabilized baseline + newly implemented modules with 100% green TDD verification.*

---

## 5. Test Suites & System Health Verification

```bash
# Run all unit, adversarial, and orchestrator test suites (80/80 passing across 13 suites)
python -m unittest discover -s tests -p "test_*.py"

# Run individual specialized test suites
python -m unittest tests/test_sandbox_bridge.py          # Process Jail & Multi-File TDD
python -m unittest tests/test_cost_estimator.py          # Cloud Unit Economics (COGS)
python -m unittest tests/test_ui_mockup_primitives.py    # OmniDeck High-Fidelity UI Mockups
python -m unittest tests/test_orchestrator.py            # Universal Task Dispatcher
python -m unittest tests/test_project_auditor.py         # Case B/C Audit & Remediation
python -m unittest tests/test_contrarian_moats.py        # 4-Moat Matrix & Council Hardening
python -m unittest tests/test_peav_and_sync.py           # PEAV & Universal SpecSync Verification

# Run Node.js enterprise test suites
npm run test:unit
npm run test:adversarial

# Run Anti-Hallucination Package Guard (AST import scanner)
npm run check:hallucinations

# Run Master Audit Trail (Verifies 6/6 enterprise gates)
npm run audit:trail
```

---

## 6. Distributed Domain Lease Locking & N-Person Team Mesh (Hackathons & Multi-Device)

Supports three operating modes: **Solo Mode** (`npm run mode:solo`), **Dual Mode** (`npm run mode:dual`), and **Team Mesh Mode** (`npm run mode:team`) for arbitrary N-developer teams across multiple laptops.

```bash
# Toggle between operating modes
npm run mode:solo                # Single Dev / Autonomous Squad (bypasses multi-host locks)
npm run mode:dual                # 2-Person 50/50 Dual-Lead Rotation (Computer 1 Alpha <-> Computer 2 Beta)
npm run mode:team                # N-Person Team Mesh Mode (Arbitrary parallel domain leases)

# Inspect active team roster, machines, and domain leases across all laptops
npm run team:status

# Acquire exclusive domain lease (any developer, any domain)
node --experimental-strip-types scripts/lock-manager.ts acquire --domain auth --operator Alice --role DomainLead
node --experimental-strip-types scripts/lock-manager.ts acquire --domain frontend --operator Bob --role DomainLead

# Release or transfer domain lease
node --experimental-strip-types scripts/lock-manager.ts release --domain auth --operator Alice
node --experimental-strip-types scripts/lock-manager.ts transfer --domain auth --from Alice --to Charlie

# Launch zero-dependency local LAN synchronization server (for offline hackathons)
npm run lan:start                # Runs on port 4040; teammates point $env:LOCK_WEBHOOK_URL="http://<IP>:4040"
```

---

## 7. Brownfield Ingestion & In-Progress Resumption Engine

Audits existing completed projects across 5 enterprise pillars or onboards half-built codebases, repairing stubs and resuming feature delivery via TDD without regressions.

```bash
# 1. Audit an existing/completed project (Scenario A: 5-pillar health audit & improvement matrix)
npm run audit:project -- --target <path_to_project>
python -m scripts.orchestrator.task_dispatcher --task audit --target src/

# 2. Audit and auto-heal broken stubs (raise NotImplementedError, TODOs, failing tests)
python -m scripts.orchestrator.task_dispatcher --task audit --target <path> --auto-heal

# 3. Onboard an in-progress project and continue feature development (Scenario B: Delta WBS)
npm run continue:project -- --target <path>
python -m scripts.orchestrator.task_dispatcher --task continue --target <path>
```
*Outputs: Executive diagnostic dossiers in `docs/audits/` and Delta WBS plans in `docs/plans/` indexed via SpecSync.*

---

## 8. Universal Multi-Harness Instruction Sync & Standard MCP Server

Ensures 100% operational rule parity across all AI agent tools (Claude Code, Cursor, Windsurf, Copilot, Codex) and exposes orchestrator tools via standard Model Context Protocol.

```bash
# Compile and synchronize AGENTS.md rules into all 6 agent harness configurations
npm run harness:sync
# Outputs: CLAUDE.md, .cursorrules, .cursor/rules/agentic-workflow.mdc, .windsurfrules, .github/copilot-instructions.md, CODEX.md

# Start standard Model Context Protocol (MCP) server for Claude Desktop, Cursor, and Windsurf
npm run mcp:start

# Install 3-gate pre-commit barrier (.git/hooks/pre-commit: Secrets + Zero-LaTeX + Anti-Hallucination)
npm run hooks:install
```

---

## 9. Key Documentation & Reference Artifacts

- **Living Document Indexes**:
  - Implementation Plans: [`docs/plans/INDEX.md`](file:///docs/plans/INDEX.md)
  - Walkthroughs: [`docs/walkthroughs/INDEX.md`](file:///docs/walkthroughs/INDEX.md)
  - System Audits: [`docs/audits/INDEX.md`](file:///docs/audits/INDEX.md)
  - Architecture Decisions: [`docs/decisions/INDEX.md`](file:///docs/decisions/INDEX.md)
  - Research Dossiers: [`docs/research/INDEX.md`](file:///docs/research/INDEX.md)
  - Specifications & Contracts: [`docs/specifications/INDEX.md`](file:///docs/specifications/INDEX.md)
- **Master Production Architecture Blueprint**: [`docs/architecture/production_architecture_blueprint.md`](file:///docs/architecture/production_architecture_blueprint.md)
- **Latest Comprehensive Audit**: [`docs/audits/remediation_audit.md`](file:///docs/audits/remediation_audit.md)

---

## 10. Zero-Process Documentation Lifecycle & Living Index Reconciler

Eliminates persistent background daemon overhead while ensuring sub-second brain artifact mirroring and conflict-free Git branch merges across N teammates.

```bash
# 1. Zero-Process Turn-Egress Sync (Synchronously mirrors brain artifacts to docs/ and exits)
npm run docs:sync
python -m scripts.orchestrator.spec_sync --sync-brain

# 2. Daemon Lifecycle Management (Optional background watcher with PID tracking)
npm run docs:start     # Launch background daemon and save PID to .agents/state/docs-watcher.pid
npm run docs:status    # Inspect active watcher status, PID, and memory footprint
npm run docs:stop      # Gracefully terminate background watcher without orphaned processes

# 3. Team Mesh Living Index Reconciliation & Merge Driver
npm run docs:reconcile # Deterministically rebuild all living catalogs sorted by timestamp descending
npm run docs:indexes   # Re-index all 6 living catalog classes via SpecSync
```

---

## 11. Real-Time Context Window Telemetry & Codebase Scale Guards

Monitors active conversation memory saturation, tracks remaining headroom before IDE auto-compaction, and autonomously applies large-project scaling policies.

```bash
# 1. Inspect Active Chat Context Window & Compaction Headroom
npm run context:check  # Measures live post-compaction context tokens, headroom, and saturation
npm run context:status # Alias for context check

# 2. Detect Codebase Scale (Small <5k LOC, Medium 5k-50k LOC, Large >50k LOC)
npm run project:scale  # Scans repository LOC and outputs autonomous execution directives

# 3. Intelligent Mutation Testing with Auto-Scoping
npm run test:mutation             # Tests fault injection on active product domain (auto-enforces --diff on large projects)
npm run test:mutation -- --diff    # Explicitly scopes fault injection to git-modified source files

# 4. Set Workspace Model Profile (Updates model ceiling and rate calculations)
npm run token:set-model gemini-3.8-flash-high # Locks active model to Gemini 3.8 Flash High (1M ceiling)
npm run token:models                          # Lists all supported Antigravity frontier models
npm run token:budget                          # Displays token budget usage and saturation directives
```

---

## 12. Amazon ML Challenge 2026 & Unstop Submission Commands

Production ML pipeline commands for large-scale Business Entity Resolution (1.73M entities) and Unstop platform browser submission automation.

```bash
# 1. Execute Iteration 2 Multi-Attribute Test Inference (Joint Name + Address, 1.73M entities)
python scripts/run_test_inference.py
# Generates matching_results.tsv and candidate_pairs.tsv with spatial guardrails & singleton protection

# 2. Verify Output TSV Format & Subsumption Invariant
python scripts/verify_matching_tsv_format.py
# Asserts: 1,732,544 rows, correct tab delimiter, M ⊆ C subset invariant, zero duplicates

# 3. Execute Official Amazon ML Challenge Validation Suite
python AWS_dataset/student_resource/utils/validate_submission.py
# Asserts: Official competition rules, duplicate checks, format correctness (PASS status)

# 4. Unstop Browser Submission Hotfix (Bypasses Windows TSV empty MIME type & Angular crash)
# Source file: scripts/unstop_submission_hotfix.js
# Usage: Paste into browser DevTools Console (F12) on https://unstop.com/.../play/code
```



