# Enterprise 2-Person / 2-Computer Autonomous Agentic Engineering Platform
### Built on Google Antigravity IDE & Antigravity CLI (`agy`)

[![TypeScript](https://img.shields.io/badge/TypeScript-Strict-blue.svg)](https://www.typescriptlang.org/)
[![Python](https://img.shields.io/badge/Python-3.11%2B%20%7C%2080%2F80%20Pass-brightgreen.svg)](https://python.org/)
[![Antigravity](https://img.shields.io/badge/Antigravity-IDE%20%2B%20CLI-purple.svg)](https://antigravity.google)
[![Security DAST](https://img.shields.io/badge/Styx-AI%20Red--Team-red.svg)](https://github.com/styx-security)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An enterprise-grade, production-hardened development platform and operational harness enabling **two engineers across two separate workstations** ("Computer 1" and "Computer 2") to build and deploy complex full-stack software autonomously using shared agentic context, distributed lease locks, anti-hallucination shields, native AST mutation testing, and adversarial multi-agent governance.

---

## ⚡ Core Architectural Pillars

1. **Dual-Mode Operator Architecture (Solo vs Dual)**:
   - **Solo Mode (`npm run mode:solo`)**: Instant solo-developer velocity. Automatically supersedes distributed lock contention while preserving subagent persona separation.
   - **Dual Mode (`npm run mode:dual`)**: Symmetrical 50/50 dual-lead workflow alternating across Computer 1 (Alpha) and Computer 2 (Beta).
   - Check status anytime via `npm run mode:status`.
2. **Universal In-Repo Living Documentation Architecture (6 Classes)**:
   - Eliminates ephemeral, orphaned conversation artifacts. Every technical artifact is permanently version-controlled under `docs/` and cataloged in living markdown indexes:
     - `docs/plans/` ([INDEX.md](file:///docs/plans/INDEX.md)) — Feature PRDs, phase roadmaps, and execution plans.
     - `docs/walkthroughs/` ([INDEX.md](file:///docs/walkthroughs/INDEX.md)) — End-of-turn execution walkthroughs and test proofs.
     - `docs/audits/` ([INDEX.md](file:///docs/audits/INDEX.md)) — System readiness probes, pentests, and flaw analyses.
     - `docs/adrs/` ([INDEX.md](file:///docs/adrs/INDEX.md)) — Architecture Decision Records preserving trade-offs and moats.
     - `docs/research/` ([INDEX.md](file:///docs/research/INDEX.md)) — Multi-hop statutory, competitive, and CVE research dossiers.
     - `docs/rfcs/` ([INDEX.md](file:///docs/rfcs/INDEX.md)) — Formal API schemas, state machines, and data contracts.
3. **Hierarchical Agile Product Squad & Fail-Closed Playwright**:
   - Simulates a full enterprise product team: Product Manager, System Architect, Adversarial SDET, Core Engineer, Mutation Auditor, and Technical Writer.
   - Enforces the **Red-to-Green Test Invariant**: SDET tests must be written first and verified RED before implementation begins.
   - **Fail-Closed Frontend Gate**: If frontend files exist, headless Playwright verification is strictly required (rejects builds with exit code `1` if tests are missing or broken).
4. **Deterministic AST Mutation Testing (≥ 80% Kill Rate)**:
   - Dual-engine AST fault injection: Python native AST (`python_mutation_tester.py`) and TypeScript (`mutation-tester.ts`).
   - Injects boundary inversions, boolean flips, arithmetic mutations, and return overrides with atomic `.bak` rollback on process interrupts.
5. **Universal Task Dispatcher Subsystems**:
   - **Task 1: Solution Formulation** (`--task solution`): First-principles dynamic synthesis, multi-hop live research triangulation, 4-moat defensibility matrix, and cloud COGS financial modeling.
   - **Task 2: Code Implementation** (`--task code`): Process sandbox jail, extreme edge-case fuzzing, 5-pass autonomous self-healing TDD loop.
   - **Task 3: Presentation Pitch Synthesis** (`--task presentation`): OmniDeck 2D Flex/Grid solver, 7 visual primitives, high-fidelity UI mockups (browser chrome, mobile HUD, 2x2 matrix), and cross-platform PDF export.
   - **Task 4: Enterprise Audit & Remediation** (`--task audit`): Automated 5-pillar health audit and auto-healing of legacy codebases.
6. **Distributed Domain Lease Locking**:
   - Atomic file/domain leases in `.agents/state/locks/<domain>.lock.json` managed via `scripts/lock-manager.ts` (with optional Supabase CloudHttpDriver).
7. **Strict Anti-Hallucination & Supply Chain Shield**:
   - Zero ghost packages tolerated. Automated AST scanning (`scripts/anti-hallucination-checker.ts`) against `package.json` and standard library built-ins.
8. **Token Economy & Progressive Disclosure**:
   - 298 on-demand modular skills dynamically discovered via `skill-finder.ts`. Prevents context window saturation through targeted bounded file reading.
9. **Dual-Persistence Memory Vault**:
   - Plain-text git-mergeable JSONL (`.agents/memory/vault/records.jsonl`) paired with local SQLite FTS5 database (`.agents/memory/vault.sqlite`) for ultra-fast full-text search.
10. **Autonomous Dynamic Red-Team DAST (Styx)**:
    - Multi-agent simulated hacker mesh attacks live container sandboxes with Proof-of-Exploit (PoE) verification before code merges.

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

# 4. Generate near-Canva level presentation pitch deck (<0.2s compile)
python -m scripts.orchestrator.task_dispatcher --task presentation --prompt "Wildfire Early Detection" --theme "cyber_dark_terminal" --slides 6

# 5. Verify Mutation Testing Kill Rate (Must kill >= 80% mutants)
python -m scripts.orchestrator.python_mutation_tester src/my_service.py "python -m unittest tests/test_my_service.py"
npm run test:mutation

# 6. Run Master Audit Trail (Verifies 6/6 enterprise gates)
npm run audit:trail
```

---

## 👥 Quickstart: 2-Person Dual Workstation Setup

### Prerequisites
- **Node.js**: v20.0+ LTS (Node 24 supported with `--experimental-strip-types`)
- **Python**: v3.10+ (Standard library `ast`, `unittest`, `sqlite3`)
- **Git**: v2.40+
- **Docker Engine & Docker Compose**: For local sandbox testing
- **Google Antigravity**: Antigravity IDE and/or CLI (`agy`)

---

### Workstation 1 (Computer 1) - Day 1 Setup

```bash
# 1. Clone repository
git clone https://github.com/Deepak-Sharma-2006/agent1.git
cd agent1

# 2. Install dependencies & type definitions
npm install

# 3. Set Dual Mode & Verify Antigravity customization layer
npm run mode:dual
npm run check:hallucinations   # Zero ghost packages check
npm run role:status            # Inspect active domain leases
npm run harness:dynamic        # Validate 5/5 next-gen dynamic test contracts

# 4. Acquire Phase 1 Lease (Alpha Builder Role)
npm run role:alpha -- auth      # Atomically leases 'auth' domain to Computer 1
```

---

### Workstation 2 (Computer 2) - Day 1 Setup

```bash
# 1. Clone repository
git clone https://github.com/Deepak-Sharma-2006/agent1.git
cd agent1

# 2. Install dependencies
npm install

# 3. Inspect active leases (Verify Computer 1 holds Phase 1 lease)
npm run role:status

# 4. AI Security Penetration Testing (Strix/Styx)
# Strix is installed via: pip install strix-agent
npm run strix:quick            # Fast pre-flight DAST check
# or run full pen-test suite:
npm run pentest
```

---

## 🔄 Daily Collaboration Cycle & Phase Handoff Runbook

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                             THE PHASE HANDOFF LIFECYCLE                                          │
├──────────────────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Computer 1 (Alpha) implements Phase 1 in Antigravity IDE / agy CLI.                           │
│ 2. Computer 1 writes tests (Vitest/Python) & authors dossier: docs/dossiers/phase-1-auth.md.    │
│ 3. SpecSync automatically saves plan & ADR into docs/plans/ and docs/adrs/.                      │
│ 4. Computer 1 commits to feat/phase-1-auth and pushes to origin.                                 │
│ 5. Computer 1 executes lease transfer:                                                           │
│    npm run role:transfer -- auth Computer2 Beta                                                  │
│ 6. Computer 2 (Beta) pulls branch, convenes Claude Council & runs Strix DAST:                    │
│    npm run pentest   (or: npm run strix:deep)                                                    │
│ 7. Computer 2 audits dossier, verifies zero timing attacks, and runs mutation tests.            │
│ 8. Computer 2 merges feat/phase-1-auth into main and releases lock:                             │
│    npm run role:release -- auth                                                                  │
│ 9. ROLE INVERSION: Computer 2 now acquires Phase 2 as ALPHA; Computer 1 becomes BETA!            │
│    (Computer 2 runs: npm run role:alpha -- payments)                                             │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
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
│   ├── adrs/ (INDEX.md)             # Architecture Decision Records
│   ├── research/ (INDEX.md)         # Multi-hop research triangulation dossiers
│   ├── rfcs/ (INDEX.md)             # API contracts, data models & state machines
│   └── dossiers/                    # Human operator cognitive dossiers
├── scripts/                         # Standalone operational tools
│   ├── orchestrator/                # Universal Task Dispatcher engine
│   │   ├── task_dispatcher.py       # Core CLI router for all 4 tasks
│   │   ├── squad_orchestrator.py    # 6-role agile squad engine
│   │   ├── spec_sync.py             # 6-class document persistence engine
│   │   ├── python_mutation_tester.py# Native Python AST mutation injector
│   │   ├── solution_council.py      # Dynamic first-principles solution engine
│   │   └── research_triangulator.py # Multi-hop statutory & market researcher
│   ├── engine/                      # OmniDeck presentation compiler
│   │   ├── deck_dispatcher.py       # Slide generator and geometry solver
│   │   └── render_bridge.py         # Cross-platform PPTX & PDF exporter
│   ├── lock-manager.ts              # Atomic lease lock & role exchange manager
│   ├── anti-hallucination-checker.ts# AST import & package.json validator
│   ├── mutation-tester.ts           # TypeScript AST mutation runner
│   ├── token-budget-guard.ts        # Real-time token monitor & brake
│   └── pen-test-runner.ts           # Strix/Styx dynamic penetration test runner
├── AGENTS.md                        # Root workspace-wide behavioral invariants
├── GEMINI.md                        # Operational pairing guidelines
├── SYSTEM_COMMANDS.md               # Master CLI & Agentic Command Cheat Sheet
├── implementation_setup_guide.md    # The Definitive Production Blueprint
└── specs/                           # Golden presentation and test contracts
```

---

## 📜 Master Documentation & Living Indexes

- **Living Catalogs**:
  - [Implementation Plans Index](docs/plans/INDEX.md)
  - [Walkthroughs Index](docs/walkthroughs/INDEX.md)
  - [Audits Index](docs/audits/INDEX.md)
  - [Architecture Decision Records Index](docs/adrs/INDEX.md)
  - [Deep Research Dossiers Index](docs/research/INDEX.md)
  - [Formal RFCs & Schemas Index](docs/rfcs/INDEX.md)
- **Comprehensive Guides**:
  - **[The Master Implementation Guide](implementation_setup_guide.md)**: Exhaustive architectural guide covering workflow topologies, graduated autonomy, database migrations, Styx DAST, and the 2-person collaboration runbook.
  - **[Master Command Cheat Sheet](SYSTEM_COMMANDS.md)**: CLI and prompt commands for all tasks.
  - **[Comprehensive System Audit](docs/audits/2026-09-21_agentic_workflow_comprehensive_audit.md)**: Stress test analysis of 15 enterprise subsystems and their remediations.

