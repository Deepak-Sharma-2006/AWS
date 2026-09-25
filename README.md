# Enterprise Multi-Persona Autonomous Agentic Engineering Platform
### Built for Google Antigravity IDE & Antigravity CLI (`agy`)

[![TypeScript](https://img.shields.io/badge/TypeScript-Strict-blue.svg)](https://www.typescriptlang.org/)
[![Python](https://img.shields.io/badge/Python-3.11%2B%20%7C%2080%2F80%20Pass-brightgreen.svg)](https://python.org/)
[![Antigravity](https://img.shields.io/badge/Antigravity-IDE%20%2B%20CLI-purple.svg)](https://antigravity.google)
[![Security DAST](https://img.shields.io/badge/Styx-AI%20Red--Team-red.svg)](https://github.com/styx-security)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

An enterprise-grade, production-hardened development platform and operational harness supporting **Solo Operators**, **2-Person Dual-Lead rotations**, and **Multi-Developer Team Meshes (N persons)** to build, test, and deploy complex full-stack software autonomously using shared agentic context, distributed lease locks, anti-hallucination shields, native AST mutation testing, zero-process documentation hooks, live context window telemetry, and adversarial multi-agent governance.

---

## ⚡ Core Architectural Pillars

1. **Tri-Mode Operator Architecture (Solo, Dual, and Team Mesh)**:
   - **Solo Mode (`npm run mode:solo`)**: Instant solo-developer velocity. Automatically supersedes distributed lock contention while preserving subagent persona separation.
   - **Dual Mode (`npm run mode:dual`)**: Symmetrical 50/50 dual-lead workflow alternating across Computer 1 (Alpha) and Computer 2 (Beta).
   - **Team Mesh Mode (`npm run mode:team`)**: Dynamic multi-developer scaling for hackathons and squads (N persons). Arbitrary parallel domain leases (`auth`, `billing`, `frontend`, `qa`) with automated Git-sync and local LAN sync server (`npm run lan:start`).
   - Check status anytime via `npm run team:status` or `npm run mode:status`.
2. **Universal In-Repo Living Documentation Architecture (6 Classes)**:
   - Eliminates ephemeral, orphaned conversation artifacts. Every technical artifact is permanently version-controlled under `docs/` and cataloged in living markdown indexes:
     - `docs/plans/` ([INDEX.md](file:///docs/plans/INDEX.md)) — Feature PRDs, phase roadmaps, and execution plans.
     - `docs/walkthroughs/` ([INDEX.md](file:///docs/walkthroughs/INDEX.md)) — End-of-turn execution walkthroughs and test proofs.
     - `docs/audits/` ([INDEX.md](file:///docs/audits/INDEX.md)) — System readiness probes, security audits, and flaw analyses.
     - `docs/decisions/` ([INDEX.md](file:///docs/decisions/INDEX.md)) — Enterprise Architecture Decisions preserving trade-offs and moats.
     - `docs/research/` ([INDEX.md](file:///docs/research/INDEX.md)) — Multi-hop statutory, competitive, and CVE research dossiers.
     - `docs/specifications/` ([INDEX.md](file:///docs/specifications/INDEX.md)) — Formal typed interface schemas, state machines, and data contracts.
3. **Hierarchical 6+1 Agile Product Squad & Complete 9-Phase SDLC**:
   - Simulates a full enterprise product team across all 9 SDLC phases:
     - Phase 0: Discovery & Market/Statutory Research (`deep_research_specialist`)
     - Phase 1: Requirements Formulation (`product_manager`)
     - Phase 2: Architectural Modeling & Trade-off ADRs (`system_architect`)
     - Phase 3: Adversarial TDD & Red-Phase Verification (`adversarial_sdet`)
     - Phase 4: Idiomatic Core Implementation (`core_engineer`)
     - Phase 5: Mutation Testing & Security Hardening (`mutation_auditor`)
     - Phase 6: Cognitive Dossier & Triple-Doc Sync (`technical_writer`)
     - Phase 7: Packaging & Release Gating (`adversarial_sdet` / Release Gate)
     - Phase 8: Post-Production Impact & Telemetry Analysis (`deep_research_specialist`)
   - **Mandatory Pre-Flight Auto-Trigger**: Product Manager automatically triggers Deep Research Specialist on any new project, problem statement, or theme even if not explicitly requested in the user prompt.
   - **Fail-Closed Frontend Gate**: If frontend files exist, headless Playwright verification is strictly required (rejects builds with exit code 1 if tests are missing or broken).
4. **Brownfield Ingestion & Delta Resumption Engine**:
   - **Completed Projects (Scenario A)**: Ingests legacy codebases, conducts a 5-pillar health audit (Architecture, Tests, AppSec, Cloud Economics, Anti-Tamper), and emits an Executive Improvement Matrix in `docs/audits/`.
   - **Developing Projects (Scenario B)**: Auto-heals broken stubs (`NotImplementedError`, `TODO`, failing tests), formulates a Delta Work Breakdown Structure in `docs/plans/`, freezes baseline behavior with Characterization tests, and resumes development via TDD.
5. **Universal Task Dispatcher Subsystems**:
   - **Task 1: Solution Formulation** (`--task solution`): First-principles dynamic synthesis, multi-hop live research triangulation, 4-moat defensibility matrix, and cloud COGS financial modeling.
   - **Task 2: Code Implementation** (`--task code`): Process sandbox jail, extreme edge-case fuzzing, 5-pass autonomous self-healing TDD loop.
   - **Task 3: Presentation Pitch Synthesis** (`--task presentation`): OmniDeck 2D Flex/Grid solver, 7 visual primitives, high-fidelity UI mockups (browser chrome, mobile HUD, 2x2 matrix), and cross-platform PDF export.
   - **Task 4: Enterprise Audit & Brownfield Ingestion** (`--task audit`): Automated 5-pillar health audit and auto-healing of legacy codebases.
   - **Task 5: In-Progress Project Resumption** (`--task continue`): Baseline stabilization and delta feature build via TDD.
   - **Task 6: Deep Research Triangulation** (`--task research`): Multi-hop exploration across 4 modes (`EXPLORATION`, `FEASIBILITY`, `DIAGNOSTIC`, `IMPACT`) powered by Jina Reader (`r.jina.ai`), DuckDuckGo, Semantic Scholar, and arXiv APIs with a minimum 120-second deliberation timer.
   - **Task 7: Post-Production Impact Analysis** (`--task impact`): Standardized telemetry and impact dossiers grounded in real testing metrics (Playwright, Pytest, Mutation, SAST).
6. **Distributed Domain Lease Locking & Mesh Coordination**:
   - Atomic file/domain leases in `.agents/state/locks/<domain>.lock.json` managed via `scripts/lock-manager.ts` (with optional Supabase CloudHttpDriver or local LAN sync server).
7. **Universal Multi-Harness Sync & Standard MCP Server**:
   - Compiles authoritative rules from `AGENTS.md` into 6 native formats: `CLAUDE.md`, `.cursorrules`, `.cursor/rules/agentic-workflow.mdc`, `.windsurfrules`, `.github/copilot-instructions.md`, and `CODEX.md` via `npm run harness:sync`.
   - Exposes orchestrator tools via standard JSON-RPC Model Context Protocol server (`npm run mcp:start`).
8. **Deterministic AST Mutation Testing (≥ 80% Kill Rate)**:
   - Dual-engine AST fault injection: Python native AST (`python_mutation_tester.py`) and TypeScript (`mutation-tester.ts`).
   - Injects boundary inversions, boolean flips, arithmetic mutations, and return overrides with atomic `.bak` rollback on process interrupts.
9. **Strict Anti-Hallucination & Supply Chain Shield**:
   - Zero ghost packages tolerated. Automated AST scanning (`scripts/anti-hallucination-checker.ts`) against `package.json` and standard library built-ins.
10. **Token Economy & Progressive Disclosure**:
    - 298 on-demand modular skills dynamically discovered via `skill-finder.ts`. Prevents context window saturation through targeted bounded file reading.
11. **Dual-Persistence Memory Vault**:
    - Plain-text git-mergeable JSONL (`.agents/memory/vault/records.jsonl`) paired with local SQLite FTS5 database (`.agents/memory/vault.sqlite`) for ultra-fast full-text search.
12. **Mandatory 3-Gate Pre-Commit Barrier & Operator Attestation Receipt**:
    - `.git/hooks/pre-commit` enforces fail-closed checks on secrets, zero-LaTeX markdown compliance, and AST anti-hallucination before every commit. Every response concludes with a verifiable cryptographic execution receipt logged to SQLite Memory Vault (`npm run attest:verify`).

---

## 🛠️ Prerequisites & One-Command Setup

- **Node.js**: v20.x or v24.x LTS (with native `--experimental-strip-types`)
- **Python**: 3.11+ or 3.12+
- **Playwright**: Headless Chromium browser automation

```bash
# 1. Install Node.js dependencies
npm install

# 2. Install Playwright browser binaries
npx playwright install chromium

# 3. Verify System Readiness (All 7 Probes Green)
npm run readiness
```

---

## 🧑‍💻 Human Operator Quick-Start: Fresh Project Usage Guide

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

## 🚀 Quickstart: Solo Operator Workflow

```bash
# 1. Switch to Solo Operator Mode (No distributed lock contention)
npm run mode:solo
npm run mode:status

# 2. Formulate a complete solution with multi-hop research triangulation
python -m scripts.orchestrator.task_dispatcher --task solution --prompt "Autonomous satellite wildfire early detection"

# 3. Run Enterprise Agile Product Squad on any feature with TDD & AST Mutation Testing
python -m scripts.orchestrator.task_dispatcher --task squad --feature case_state_manager

# 4. Run Headless Playwright Browser E2E Suites (Maximum Elemental Accuracy)
npm run test:e2e
npm run test:e2e:chakra

# 5. Run Master Backend Test Suite & SAST Security Scanner
npm run test:backend
npm run audit:sast

# 6. Verify Cryptographic Proof & Squad Attestation Ledger
npm run attest:verify

# 7. Generate near-Canva level presentation pitch deck (<0.2s compile)
python -m scripts.orchestrator.task_dispatcher --task presentation --prompt "Wildfire Early Detection" --theme "cyber_dark_terminal" --slides 6

# 8. Verify Mutation Testing Kill Rate (Must kill >= 80% mutants)
python -m scripts.orchestrator.python_mutation_tester src/my_service.py "python -m unittest tests/test_my_service.py"
npm run test:mutation

# 9. Run Master Audit Trail (Verifies all enterprise gates)
npm run audit:trail

# 10. Check live active conversation context window & compaction headroom
npm run context:check

# 11. Synchronize brain documentation (Zero-Process Turn-Egress Architecture)
npm run docs:sync
```

---

## 👥 Enterprise Collaboration: 2-Person Dual-Lead & Multi-Developer Team Mesh

The platform natively supports three operational collaboration topologies:
1. **Solo Operator Mode (`npm run mode:solo`)**: Single developer commanding the full 6-persona autonomous squad. Distributed locks are bypassed with zero collisions.
2. **2-Person Dual-Lead Mode (`npm run mode:dual`)**: Symmetrical 50/50 dual-lead workflow alternating across Computer 1 (Alpha - Feature Architect) and Computer 2 (Beta - Adversarial Systems & SDET).
3. **N-Person Team Mesh Mode (`npm run mode:team`)**: Distributed squad mesh where N developers concurrently lease independent domains (`auth`, `billing`, `frontend`, `analytics`) with local LAN sync (`npm run lan:start`) and automated Git merge reconciliation.

---

### Workstation 1 (Computer 1: Lead 1 Alpha) — Day 1 Setup

```bash
# 1. Clone repository
git clone https://github.com/Deepak-Sharma-2006/script.git my-project
cd my-project

# 2. Install dependencies & type definitions
npm install

# 3. Set Dual Mode & verify environment readiness
npm run mode:dual
npm run check:hallucinations   # Zero ghost packages check
npm run lock:status            # Inspect active domain leases across workstations

# 4. Acquire domain lease for feature development (e.g. auth domain)
npm run lock:acquire --domain auth
```

---

### Workstation 2 (Computer 2: Lead 2 Beta) — Day 1 Setup

```bash
# 1. Clone repository
git clone https://github.com/Deepak-Sharma-2006/script.git my-project
cd my-project

# 2. Install dependencies
npm install

# 3. Inspect active leases (Verify Computer 1 holds active lease on 'auth')
npm run lock:status

# 4. Run adversarial readiness and security baseline audits
npm run audit:sast             # Bandit SAST security audit
npm run test:backend           # Master pytest suite
npm run test:e2e               # Headless Playwright browser verification
```

---

## 🔄 Daily Collaboration Cycle & Phase Handoff Runbook

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             THE PHASE HANDOFF LIFECYCLE                                          │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Computer 1 (Alpha) implements Phase 1 features, unit tests, and architecture dossiers.       │
│ 2. Brain artifacts are mirrored synchronously via zero-process turn-egress:                      │
│    npm run docs:sync  (persists to docs/plans/ and docs/decisions/)                              │
│ 3. Living catalogs are reconciled deterministically:                                             │
│    npm run docs:reconcile                                                                        │
│ 4. Computer 1 commits and pushes to origin:                                                      │
│    git commit -m "feat(auth): phase 1 implementation" && git push origin main                     │
│ 5. Computer 1 initiates atomic role handoff:                                                     │
│    npm run role:handoff                                                                          │
│ 6. Computer 2 (Beta) pulls branch, authors independent black-box adversarial tests in            │
│    tests/adversarial/, runs AST mutation testing, and audits AppSec boundaries:                  │
│    npm run test:mutation && npm run audit:beta                                                   │
│ 7. Computer 2 applies direct hardening patches, verifies attestation ledger:                     │
│    npm run attest:verify                                                                         │
│ 8. Computer 2 releases domain lock and certifies release:                                        │
│    npm run lock:release --domain auth                                                            │
│ 9. ROLE INVERSION: Computer 2 now acquires Phase 2 as ALPHA; Computer 1 becomes BETA!            │
│    (Computer 2 runs: npm run lock:acquire --domain payments)                                     │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

### 🌐 N-Person Team Mesh Collaboration (Hackathons & Agile Squads)

When expanding beyond 2 developers to N team members:
```bash
# 1. Activate Team Mesh mode on all workstations
npm run mode:team

# 2. Start local LAN sync server on host machine (or use cloud git locks)
npm run lan:start

# 3. Each developer acquires an independent domain lease concurrently:
npm run lock:acquire --domain frontend    # Developer A
npm run lock:acquire --domain billing     # Developer B
npm run lock:acquire --domain ingestion   # Developer C

# 4. Automated conflict-free living catalog merges:
# Custom Git merge driver (merge.docs-index.driver) reconciles docs/**/INDEX.md automatically on git pull/merge.
npm run docs:reconcile
```

---

## 📂 Repository Topology

```
├── .agents/
│   ├── rules/                       # Contextual behavior constraints
│   │   ├── anti-hallucination.md    # Zero ghost packages, empirical proof
│   │   ├── token-economy.md         # Budget ceilings & progressive disclosure
│   │   ├── multi-operator-sync.md   # Dynamic Alpha <-> Beta role rotation
│   │   ├── code-reading-rules.md    # 6-technique cognitive dossier mandate
│   │   ├── security-controls.md     # 20-point production security rules
│   │   └── coding-standards.md      # Strict TypeScript & TDD
│   ├── skills/                      # 298 modular operational runbooks
│   │   ├── claude-council/          # 5-member adversarial council
│   │   ├── styx-pentest/            # Autonomous AI red-team DAST (Strix)
│   │   ├── code-reading-dossier/    # 6-technique comprehension generator
│   │   ├── token-budget-guard/      # Token calculation & cost limiter
│   │   ├── git-sync-lock/           # Distributed lease lock coordinator
│   │   └── skill-finder/            # Zero-token dynamic skill search & scaffold
│   ├── memory/                      # Dual-Persistence Memory Vault
│   │   ├── vault.sqlite             # Local SQLite database with FTS5 indexing
│   │   └── vault/records.jsonl      # Git-mergeable append-only plain text log
│   └── state/                       # Ephemeral locks & metrics
├── docs/                            # Living Version-Controlled Documentation
│   ├── plans/ (INDEX.md)            # Feature PRDs & implementation plans
│   ├── walkthroughs/ (INDEX.md)     # End-of-turn execution records & proofs
│   ├── audits/ (INDEX.md)           # System readiness & adversarial audits
│   ├── decisions/ (INDEX.md)        # Enterprise Architecture Decisions
│   ├── research/ (INDEX.md)         # Multi-hop research triangulation dossiers
│   ├── specifications/ (INDEX.md)   # API contracts, data models & state machines
│   ├── architecture/                # Production architecture blueprints
│   └── dossiers/                    # Human operator cognitive dossiers
├── scripts/                         # Standalone operational tools
│   ├── orchestrator/                # Universal Task Dispatcher engine
│   │   ├── task_dispatcher.py       # Core CLI router for all orchestrator tasks
│   │   ├── squad_orchestrator.py    # 6+1 persona agile squad engine (9-phase SDLC)
│   │   ├── spec_sync.py             # 6-class document persistence engine
│   │   ├── python_mutation_tester.py# Native Python AST mutation injector
│   │   ├── solution_council.py      # Dynamic first-principles solution engine
│   │   └── research_triangulator.py # 4-mode deep research & impact engine (Jina Reader, 120s deliberation)
│   ├── engine/                      # OmniDeck presentation compiler
│   │   ├── deck_dispatcher.py       # Slide generator and geometry solver
│   │   └── render_bridge.py         # Cross-platform PPTX & PDF exporter
│   ├── lock-manager.ts              # Atomic lease lock & role exchange manager
│   ├── anti-hallucination-checker.ts# AST import & package.json validator
│   ├── mutation-tester.ts           # TypeScript AST mutation runner
│   ├── token-budget-guard.ts        # Real-time token monitor & brake
│   └── security-audit-runner.ts     # Strix/Styx dynamic security audit runner
├── AGENTS.md                        # Root workspace-wide behavioral invariants
├── GEMINI.md                        # Operational pairing guidelines
├── SYSTEM_COMMANDS.md               # Master CLI & Agentic Command Cheat Sheet
└── specs/                           # Golden presentation and test contracts
```

---

## 📜 Master Documentation & Living Indexes

- **Living Catalogs**:
  - [Implementation Plans Index](docs/plans/INDEX.md)
  - [Walkthroughs Index](docs/walkthroughs/INDEX.md)
  - [Audits Index](docs/audits/INDEX.md)
  - [Architecture Decisions Index](docs/decisions/INDEX.md)
  - [Deep Research Dossiers Index](docs/research/INDEX.md)
  - [Specifications & Contracts Index](docs/specifications/INDEX.md)
- **Comprehensive Guides**:
  - **[Master Production Architecture Blueprint](docs/architecture/production_architecture_blueprint.md)**: Exhaustive 3,000-line architectural guide covering workflow topologies, graduated autonomy, database migrations, Styx DAST, and the multi-operator collaboration runbook.
  - **[Master Command Cheat Sheet](SYSTEM_COMMANDS.md)**: CLI and prompt commands for all tasks.
  - **[Comprehensive System Audit](docs/audits/2026-09-21_agentic_workflow_comprehensive_audit.md)**: Stress test analysis of 15 enterprise subsystems and their remediations.

---

## 🏆 Amazon ML Challenge 2026: Business Entity Resolution

The repository includes a production-grade, memory-safe entity resolution pipeline (Team Nile) designed for the Amazon ML Challenge 2026:

- **Algorithm**: Multi-Stage Spatial-Token Inverted Index Blocking + SIMD String Metric Decision Gate (`RapidFuzz` with standard library fallback).
- **Scale**: Evaluated on 1,732,544 test entities across France, US, and India, completing full inference in under 11 minutes with memory usage under 1.15 GB RAM.
- **Leaderboard Trajectory**:
  - *Iteration 1 Official Baseline*: **0.147136** macro F₀.₅ (RCA: Name-only matching without address corroboration, arbitrary DF ≤ 150 posting truncation, and false positive inflation on singletons).
  - *Iteration 2 Architecture*: **~0.787 - 0.835+** validation F₀.₅ (Joint Name + Address multi-attribute corroboration, unconstrained IDF-weighted blocking, and strict singleton precision gating).
- **Deliverables**:
  - `code_submission/`: Competition documentation template and clean, self-contained inference script.
  - `code.zip`: Official zipped code submission package.
  - `scripts/unstop_submission_hotfix.js`: Browser DevTools console hotfix resolving the Unstop portal Windows `.tsv` empty MIME type issue and Angular null crash.

