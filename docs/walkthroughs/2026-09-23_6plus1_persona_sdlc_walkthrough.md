# Technical Walkthrough: 6+1 Enterprise Agile Product Squad & 9-Phase SDLC Architecture

This walkthrough documents the full architecture, implementation, and empirical verification of the **6+1 Enterprise Agile Product Squad**, the **9-Phase SDLC Lifecycle**, the **Deep Research Specialist** engine, and the **Workspace-Wide Mandatory Zero-LaTeX Invariant**.

---

## 1. Executive Summary & SDLC Lifecycle Completion

Prior to this enhancement, the squad consisted of 6 personas covering internal development and testing, leaving pre-flight discovery/market validation and post-ship telemetry unanchored.

The squad is now expanded to a **6+1 Enterprise Agile Product Squad** mapped across all **9 phases of the enterprise SDLC**:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        THE 9-PHASE ENTERPRISE SDLC LIFECYCLE                           │
├─────────┬───────────────────────────────┬────────────────────────────┬─────────────────┤
│ Phase   │ Name                          │ Lead Persona               │ Primary Output  │
├─────────┼───────────────────────────────┼────────────────────────────┼─────────────────┤
│ Phase 0 │ Discovery & Deep Research     │ Deep Research Specialist   │ docs/research/  │
│ Phase 1 │ Requirements Formulation      │ Product Manager            │ docs/plans/     │
│ Phase 2 │ Architectural Modeling        │ System Architect           │ docs/rfcs/, adrs│
│ Phase 3 │ Adversarial TDD (Red-Phase)   │ Adversarial SDET           │ tests/          │
│ Phase 4 │ Idiomatic Implementation      │ Core Engineer              │ src/            │
│ Phase 5 │ Mutation & AppSec Hardening   │ Mutation Auditor           │ specs/metrics   │
│ Phase 6 │ Cognitive Dossier & Doc Sync  │ Technical Writer           │ docs/dossiers/  │
│ Phase 7 │ Packaging & Release Gating    │ Adversarial SDET           │ release artifacts│
│ Phase 8 │ Post-Ship Impact & Telemetry  │ Deep Research Specialist   │ docs/research/  │
└─────────┴───────────────────────────────┴────────────────────────────┴─────────────────┘
```

---

## 2. Key Architectural Enhancements

### 2.1 Deep Research Specialist Engine ([`research_triangulator.py`](file:///scripts/orchestrator/research_triangulator.py))
- **4 Operational Modes**:
  1. `EXPLORATION`: Pre-flight discovery, market validation, statutory/regulatory scans.
  2. `FEASIBILITY`: Mid-architecture dependency viability and trade-off benchmarking.
  3. `DIAGNOSTIC`: Bug reproduction, upstream defect analysis, and CVE lookups.
  4. `IMPACT`: Post-production telemetry synthesis grounded in real test suite metrics.
- **Modern Keyless 2025/2026 Connectors**:
  - `Jina Reader`: Clean markdown extraction from web pages via `https://r.jina.ai/<URL>`.
  - `DuckDuckGo`: Privacy-preserving, unauthenticated web search.
  - `Semantic Scholar & arXiv`: Academic paper and citation graph retrieval.
  - `NIST NVD`: CVE vulnerability database lookup.
- **Saturation Index & 120s Deliberation Timer**:
  ```
  saturation_index = min(1.0, (unique_citations * 0.15) + (hops * 0.20) + (time_spent / 120.0))
  ```
  The engine enforces a minimum 120-second deliberation window with an Operator Extension Gate if saturation remains below 0.85.

### 2.2 Product Manager Mandatory Pre-Flight Auto-Trigger
- Whenever an operator provides a new project, problem statement, idea, or theme, `ProductManagerRole.create_functional_spec()` automatically triggers Phase 0 Deep Research (`EXPLORATION` mode), even when the operator prompt does not explicitly request research.
- The resulting research dossier is persisted directly to `docs/research/` and indexed via SpecSync.

### 2.3 System Architect ADR Gating
- `SystemArchitectRole.design_contract()` now strictly differentiates between routine interface contracts and significant architectural trade-offs:
  - Routine API schemas, data models, and state machines are persisted to `docs/rfcs/`.
  - Architecture Decision Records are generated in `docs/adrs/` **only when significant architectural trade-offs** or irreversible structural decisions are made (`is_significant_tradeoff=True`).

### 2.4 Universal Task Dispatcher CLI Integration
- Added `--task research` and `--task impact` with `--research-mode` and `--min-time` CLI flags to [`task_dispatcher.py`](file:///scripts/orchestrator/task_dispatcher.py).

### 2.5 Workspace-Wide Mandatory Zero-LaTeX Invariant
- Codified in `AGENTS.md` (Section 9.4), `GEMINI.md` (Section 6), `SYSTEM_COMMANDS.md`, and `implementation_setup_guide.md` (Section 11.13).
- Prohibits raw LaTeX math delimiters across all markdown files (`docs/`, plans, walkthroughs, dossiers).
- All mathematical expressions, bounds, percentages, and formulas use clean Unicode typography (`≥`, `≤`, `×`, `≠`, `→`, `≈`, `±`, `Δt`) or fenced code blocks.
- Audited and verified fail-closed by `scripts/markdown-linter.ts`.

---

## 3. Empirical Verification Results

### 3.1 Unit Test Suite (`tests/test_squad_orchestrator.py`)
Executed via `python -m unittest tests/test_squad_orchestrator.py`:
- **10/10 Tests Passed** (0 failures, 0 errors in 1.017s):
  1. `test_7_personas_defined`: Verified all 7 personas exist in `SQUAD_PERSONA_PROFILES`.
  2. `test_deep_research_role_instantiation`: Verified `DeepResearchRole` initializes and executes.
  3. `test_pm_auto_triggers_research_on_new_problem`: Verified PM automatically launches Deep Research in `EXPLORATION` mode.
  4. `test_system_architect_adr_gating`: Verified ADR is generated only when `is_significant_tradeoff=True`; routine contracts update RFCs only.
  5. `test_research_triangulator_modes`: Verified `EXPLORATION` and `IMPACT` modes in `ResearchTriangulator`.
  6. `test_squad_lifecycle_end_to_end`: Verified complete 9-phase lifecycle (Phase 0 Research -> PM Spec -> Architect RFC -> SDET Red Test -> Core Green Impl -> PEAV 100% -> Mutation 100% -> Dossier -> Phase 8 Impact).
  7. `test_peav_shield_alignment`: Verified plan-execution alignment verification.
  8. `test_sdet_red_phase_enforcement`: Verified fail-closed red-first testing gate.
  9. `test_squad_attestation_receipt`: Verified cryptographic SHA-256 receipt generation.
  10. `test_spec_sync_integration`: Verified catalog synchronization.

### 3.2 Workspace-Wide Markdown Linting (`npm run lint:markdown`)
Executed via `node --experimental-strip-types scripts/markdown-linter.ts`:
- `docs/`: **0 Violations (PASSED)**
- `README.md`: **0 Violations (PASSED)**
- `implementation_setup_guide.md`: **0 Violations (PASSED)**
- `implementation_plan.md`: **0 Violations (PASSED)**

### 3.3 Living Documentation Catalogs (`spec_sync.py --all-indexes`)
All 6 living documentation indexes verified active and synchronized:
- `docs/plans/INDEX.md`: 7 documents
- `docs/walkthroughs/INDEX.md`: 5 documents
- `docs/audits/INDEX.md`: 5 documents
- `docs/adrs/INDEX.md`: 5 documents
- `docs/research/INDEX.md`: 12 documents
- `docs/rfcs/INDEX.md`: 8 documents
