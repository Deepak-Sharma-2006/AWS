# Antigravity Universal Multi-Agent System — Master Command Cheat Sheet

> **Quick Navigation**: Use this guide to assign tasks directly to the Antigravity agent or execute CLI commands in PowerShell / terminal.  
> **System Status**: Fully Operational & 100% Green (69 / 69 Tests Passing Across 13 Suites)  

---

## 1. Core Task Execution Commands

### Task 1: Solution Formulation, White-Space Moat & Cloud Unit Economics
Deconstructs a problem statement, conducts live online fact-checking, benchmarks commercial prior-art, designs a 10x technical moat, generates native visual architecture diagrams, models real cloud COGS (AWS/GCP/tokens at $\ge 75\%$ gross margin), and records decisions to SQLite Memory Vault.

```bash
# Basic Problem Prompt
python -m scripts.orchestrator.task_dispatcher --task solution --prompt "Autonomous satellite wildfire early detection"

# Detailed Problem Statement with Title & Domain
python -m scripts.orchestrator.task_dispatcher --task solution --title "PRAVAH Flood Intelligence" --prompt "Synthetic Aperture Radar flash flood forecasting" --domain "Hydrology & Disaster AI"
```
*Outputs: Executive solution dossier in `docs/dossiers/solution_dossier.md` (with Cloud COGS Financial Feasibility Matrix) and Memory Vault ADR record.*

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
# Stage 1: Fast PPTX Compilation (< 0.2s) - Default 6 Slides
python -m scripts.orchestrator.task_dispatcher --task presentation --prompt "Sovereign Defense AI" --theme "cyber_dark_terminal" --slides 6

# Stage 1: Extended & Custom Slide Themes (sih_official_light, modern_saas_glass, deep_navy_executive)
python -m scripts.orchestrator.task_dispatcher --task presentation --prompt "Sovereign Defense AI" --theme "sih_official_light" --slides 8

# Stage 2: Gated PDF Export (ONLY run when you explicitly approve the PPTX deck)
python -m scripts.orchestrator.task_dispatcher --task presentation --prompt "Sovereign Defense AI" --theme "cyber_dark_terminal" --export-pdf
```
*Outputs: Native PowerPoint deck in `specs/presentations/deck_dispatcher_output.pptx` (and PDF if `--export-pdf` passed).*

---

## 2. Memory Vault, Audits & Security Commands

### SQLite Memory Vault (Durable Knowledge Persistence)
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

## 3. Test Suites & System Health Verification

```bash
# Run all unit, adversarial, and orchestrator test suites (69/69 passing across 13 suites)
python -m unittest discover -s tests -p "test_*.py"

# Run individual specialized test suites
python -m unittest tests/test_sandbox_bridge.py          # Process Jail & Multi-File TDD
python -m unittest tests/test_cost_estimator.py          # Cloud Unit Economics (COGS)
python -m unittest tests/test_ui_mockup_primitives.py    # OmniDeck High-Fidelity UI Mockups
python -m unittest tests/test_orchestrator.py            # Universal Task Dispatcher
python -m unittest tests/test_project_auditor.py         # Case B/C Audit & Remediation
python -m unittest tests/test_contrarian_moats.py        # 4-Moat Matrix & Council Hardening

# Run Node.js enterprise test suites
npm run test:unit
npm run test:adversarial

# Run Anti-Hallucination Package Guard (AST import scanner)
npm run check:hallucinations
```

---

## 4. Distributed Domain Lease Locking (2-Computer Collaboration)

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

## 5. Key Documentation & Reference Artifacts

- **SIH Problem Solution Blueprints**: Located in `docs/sih_solutions/`
  - `docs/sih_solutions/sih-2026-mha-vasp-attribution-blueprint.md` (MHA I4C Cryptocurrency VASP Attribution)
  - `docs/sih_solutions/sih-2026-ntro-solution-blueprint.md` (NTRO Critical Infrastructure SAR Anomaly Detection)
- **Golden Reference Presentations**: Located in `specs/presentations/`
  - `specs/presentations/BHEDAK_SIH2026.pptx` (Championship Reference Deck)
  - `specs/presentations/CHAKRA_SIH2026.pptx` (Championship Reference Deck)
  - `specs/presentations/assets/` (Visual vector and diagram fixtures)
- **Comprehensive Setup & Architecture Guide**: [implementation_setup_guide.md](file:///implementation_setup_guide.md)
- **Latest Verification Walkthrough**: [walkthrough.md](file:///c:/Users/Deepak%20Sharma/.gemini/antigravity-ide/brain/c3c53c00-a334-4137-bd3b-cf0eecff66c4/walkthrough.md)
