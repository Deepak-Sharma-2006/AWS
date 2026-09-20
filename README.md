# Enterprise 2-Person / 2-Computer Autonomous Agentic Engineering Platform
### Built on Google Antigravity IDE & Antigravity CLI (`agy`)

[![TypeScript](https://img.shields.io/badge/TypeScript-Strict-blue.svg)](https://www.typescriptlang.org/)
[![Antigravity](https://img.shields.io/badge/Antigravity-IDE%20%2B%20CLI-purple.svg)](https://antigravity.google)
[![Security DAST](https://img.shields.io/badge/Styx-AI%20Red--Team-red.svg)](https://github.com/styx-security)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

An enterprise-grade, production-hardened development platform and operational harness enabling **two engineers across two separate workstations** ("Computer 1" and "Computer 2") to build and deploy complex full-stack software autonomously using shared agentic context, distributed lease locks, anti-hallucination shields, and adversarial multi-agent governance.

---

## ⚡ Core Architectural Pillars

1. **Dual-Mode Operator Architecture (Solo vs Dual)**:
   - **Solo Mode (`npm run mode:solo`)**: Instant solo-developer velocity. Automatically supersedes distributed lock contention while preserving subagent persona separation.
   - **Dual Mode (`npm run mode:dual`)**: Symmetrical 50/50 dual-lead workflow alternating across Computer 1 (Alpha) and Computer 2 (Beta).
   - Check status anytime via `npm run mode:status`.
2. **Hierarchical Agile Product Squad (`npm run squad:run`)**:
   - Simulates a full enterprise product team: Product Manager, System Architect, Adversarial SDET, Core Engineer, Mutation Auditor, and Technical Writer.
   - Enforces the **Red-to-Green Test Invariant**: SDET tests must be written first and verified RED before implementation begins.
   - Automated Headless Browser verification with Playwright whenever frontend code is detected.
3. **Deterministic Mutation Testing Engine (`npm run test:mutation`)**:
   - Injects AST faults (boundary flips, return overrides, arithmetic inversions, state bypasses) to ensure test suites kill $\ge 80\%$ of injected bugs. Eliminates false green tests.
4. **Distributed Domain Lease Locking**:
   - Atomic file/domain leases in `.agents/state/locks/<domain>.lock.json` managed via `scripts/lock-manager.ts`.
5. **Strict Anti-Hallucination & Supply Chain Shield**:
   - Zero ghost packages tolerated. Automated AST scanning (`scripts/anti-hallucination-checker.ts`) against `package.json` and Node.js built-ins.
6. **Token Economy & Hard Budget Brakes**:
   - Progressive disclosure, max 5 iterations per auto-correction loop, and 250,000 token ceiling per phase.
7. **Cognitive Code Comprehension Protocol (Part 7)**:
   - Mandatory 6-technique cognitive reading dossiers generated for every completed phase in `docs/dossiers/`.
8. **Autonomous Dynamic Red-Team DAST (Styx)**:
   - Multi-agent simulated hacker mesh attacks live container sandboxes with Proof-of-Exploit (PoE) verification before code merges.

---

## 🚀 Quickstart: Solo Operator Workflow

```bash
# 1. Switch to Solo Operator Mode (No distributed lock contention)
npm run mode:solo
npm run mode:status

# 2. Run Enterprise Agile Product Squad on any feature
python -m scripts.orchestrator.task_dispatcher --task squad --feature case_state_manager

# 3. Verify Mutation Testing Kill Rate (Must kill >= 80% mutants)
npm run test:mutation

# 4. Run Next-Gen Dynamic Behavioral Evaluation Harness
npm run harness:dynamic
```

---

## 👥 Quickstart: 2-Person Dual Workstation Setup

### Prerequisites
- **Node.js**: v20.0+ LTS (Node 24 supported with `--experimental-strip-types`)
- **Git**: v2.40+
- **Docker Engine & Docker Compose**: For local sandbox testing
- **Google Antigravity**: Antigravity IDE and/or CLI (`agy`)

---

### Workstation 1 (Computer 1) - Day 1 Setup

```bash
# 1. Clone repository
git clone https://github.com/Deepak-Sharma-2006/script.git
cd script

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
git clone https://github.com/Deepak-Sharma-2006/script.git
cd script

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
│ 2. Computer 1 writes tests (Vitest) & authors dossier: docs/dossiers/phase-1-auth.md.            │
│ 3. Computer 1 commits to feat/phase-1-auth and pushes to origin.                                 │
│ 4. Computer 1 executes lease transfer:                                                           │
│    npm run role:transfer -- auth Computer2 Beta                                                  │
│ 5. Computer 2 (Beta) pulls branch, convenes Claude Council & runs Strix DAST:                    │
│    npm run pentest   (or: npm run strix:deep)                                                    │
│ 6. Computer 2 audits dossier, verifies zero timing attacks, and executes Feynman compression.    │
│ 7. Computer 2 merges feat/phase-1-auth into main and releases lock:                             │
│    npm run role:release -- auth                                                                  │
│ 8. ROLE INVERSION: Computer 2 now acquires Phase 2 as ALPHA; Computer 1 becomes BETA!            │
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
│   ├── skills/                      # Modular operational runbooks
│   │   ├── claude-council/          # 5-member adversarial council
│   │   ├── styx-pentest/            # Autonomous AI red-team DAST (Strix)
│   │   ├── code-reading-dossier/    # 6-technique comprehension generator
│   │   ├── token-budget-guard/      # Token calculation & cost limiter
│   │   ├── agentic-loop-runner/     # 4-part self-correcting feedback loop
│   │   ├── git-sync-lock/           # Distributed lease lock coordinator
│   │   └── skill-finder/            # Zero-token dynamic skill search & scaffold
│   ├── hooks.json                   # Lifecycle hooks (safety, lint, token)
│   ├── harness/                     # Behavioral evaluation test suite
│   │   ├── eval-runner.ts           # Automated test harness runner
│   │   └── golden-evals.json        # Benchmark test contracts
│   └── state/                       # Ephemeral locks & metrics
├── scripts/                         # Standalone operational tools
│   ├── lock-manager.ts              # Atomic lease lock & role exchange manager
│   ├── anti-hallucination-checker.ts# AST import & package.json validator
│   ├── token-budget-guard.ts        # Real-time token monitor & brake
│   ├── skill-finder.ts              # Dynamic skill lookup & generator
│   └── pen-test-runner.ts           # Strix/Styx dynamic penetration test runner
├── docs/
│   └── dossiers/                    # Human operator comprehension records
│       └── phase-1-auth.md          # Sample Phase 1 dossier
├── AGENTS.md                        # Root workspace-wide behavioral invariants
├── GEMINI.md                        # Operational pairing guidelines
├── implementation_setup_guide.md    # The Definitive 10-Part Production Blueprint
└── scripts_transcripts_deep_analysis.md # Comprehensive 8-Pillar Technical Analysis
```

---

## 📜 Master Documentation
- **[The 10-Part Production Blueprint](implementation_setup_guide.md)**: Exhaustive architectural guide covering workflow topologies, graduated autonomy, database migrations, Styx DAST, and the 2-person collaboration runbook.
- **[The 8 Pillars Deep Analysis](scripts_transcripts_deep_analysis.md)**: Deconstruction of the 8 pillars of modern vibe coding and agentic workflows.
- **[Phase 1 Cognitive Dossier Sample](docs/dossiers/phase-1-auth.md)**: Concrete reference demonstrating the 6 cognitive reading techniques in practice.
