# Antigravity Universal Multi-Agent System — Master Command Cheat Sheet

> **Quick Navigation**: Use this guide to assign tasks directly to the Antigravity agent or execute CLI commands in PowerShell / terminal.  
> **System Status**: Fully Operational & 100% Green (80 / 80 Python Tests Passing Across 13 Suites + 4/4 Node Unit Tests + 4/4 Behavioral Harness Contracts + 6/6 Master Audit Trail Gates)  

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
- `docs/adrs/` & `docs/adrs/INDEX.md` (Architecture Decision Record)
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

### Task 4 / Enterprise Product Squad: 6-Pillar Autonomous Squad Run
Simulates the full enterprise product team: Product Manager, System Architect, Adversarial SDET, Core Engineer, Mutation Auditor, and Technical Writer.

```bash
# Execute end-to-end squad workflow on a target feature
python -m scripts.orchestrator.task_dispatcher --task squad --feature case_state_manager

# View live mode status (Solo vs Dual-Lead 50/50)
npm run mode:status
```
*Outputs: Execution proof, walkthough dossier in `docs/walkthroughs/`, and updated living index.*

---

## 2. In-Repo Living Documentation Architecture (6 Document Classes)

Every system artifact is permanently version-controlled under `docs/` and tracked in living `INDEX.md` catalogs.

| Document Class | Directory | Living Catalog | Purpose & Contents |
| :--- | :--- | :--- | :--- |
| **Implementation Plans** | `docs/plans/` | [`docs/plans/INDEX.md`](file:///docs/plans/INDEX.md) | Feature PRDs, phase roadmaps, and execution plans |
| **Walkthroughs** | `docs/walkthroughs/` | [`docs/walkthroughs/INDEX.md`](file:///docs/walkthroughs/INDEX.md) | End-of-turn execution records, test proof, and diffs |
| **System Audits** | `docs/audits/` | [`docs/audits/INDEX.md`](file:///docs/audits/INDEX.md) | System readiness probes, adversarial red-team DAST |
| **Architecture Decisions** | `docs/adrs/` | [`docs/adrs/INDEX.md`](file:///docs/adrs/INDEX.md) | Architectural trade-offs, moats, and non-negotiables |
| **Research Dossiers** | `docs/research/` | [`docs/research/INDEX.md`](file:///docs/research/INDEX.md) | Multi-hop statutory, competitive, and CVE research |
| **Formal RFCs & Contracts** | `docs/rfcs/` | [`docs/rfcs/INDEX.md`](file:///docs/rfcs/INDEX.md) | API schemas, data contracts, and state machines |

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

### Fail-Closed Headless Playwright Verification
Strictly rejects builds with exit code `1` if frontend files exist and browser tests are missing or failing.

```bash
# Run headless browser verification
npx playwright test

# Audit frontend layout against Directive 14 Component Shell (<footer class="app-action-dock">)
npm run test:e2e
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
python -m scripts.orchestrator.task_dispatcher --task audit --target docs/sih_solutions/solution_blueprint.md
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

## 6. Distributed Domain Lease Locking (2-Computer Collaboration)

Supports dual storage modes: **LocalGitDriver** (offline default using `.agents/state/locks/`) and **CloudHttpDriver** (Supabase / REST remote coordination without Git merge conflicts).

```bash
# Inspect all active domain leases (Local Mode)
node --experimental-strip-types scripts/lock-manager.ts status

# Inspect active domain leases (Cloud Mode)
node --experimental-strip-types scripts/lock-manager.ts status --cloud

# Acquire exclusive domain lease (Lead 1 Alpha or Lead 2 Beta)
node --experimental-strip-types scripts/lock-manager.ts acquire --domain core --operator "Deepak" --role Alpha --ttl 7200

# Transfer lease during phase handoff
node --experimental-strip-types scripts/lock-manager.ts transfer --domain core --operator "Deepak" --to "Partner" --role Beta

# Release lease
node --experimental-strip-types scripts/lock-manager.ts release --domain core --operator "Deepak"
```

---

## 7. Key Documentation & Reference Artifacts

- **Living Document Indexes**:
  - Implementation Plans: [`docs/plans/INDEX.md`](file:///docs/plans/INDEX.md)
  - Walkthroughs: [`docs/walkthroughs/INDEX.md`](file:///docs/walkthroughs/INDEX.md)
  - System Audits: [`docs/audits/INDEX.md`](file:///docs/audits/INDEX.md)
  - Architecture Decisions (ADRs): [`docs/adrs/INDEX.md`](file:///docs/adrs/INDEX.md)
  - Research Dossiers: [`docs/research/INDEX.md`](file:///docs/research/INDEX.md)
  - Formal RFCs & Schemas: [`docs/rfcs/INDEX.md`](file:///docs/rfcs/INDEX.md)
- **Comprehensive Setup & Architecture Guide**: [implementation_setup_guide.md](file:///implementation_setup_guide.md)
- **SIH Problem Solution Blueprints**: Located in `docs/sih_solutions/`
  - `docs/sih_solutions/sih-2026-mha-vasp-attribution-blueprint.md` (MHA I4C Cryptocurrency VASP Attribution)
  - `docs/sih_solutions/sih-2026-ntro-solution-blueprint.md` (NTRO Critical Infrastructure SAR Anomaly Detection)
- **Golden Reference Presentations**: Located in `specs/presentations/`
  - `specs/presentations/BHEDAK_SIH2026.pptx` (Championship Reference Deck)
  - `specs/presentations/CHAKRA_SIH2026.pptx` (Championship Reference Deck)
  - `specs/presentations/assets/` (Visual vector and diagram fixtures)
- **Latest Comprehensive Audit**: [`docs/audits/2026-09-21_agentic_workflow_comprehensive_audit.md`](file:///docs/audits/2026-09-21_agentic_workflow_comprehensive_audit.md)

