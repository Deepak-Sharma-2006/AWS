# Implementation Plan: Enterprise Agentic System Architecture Overhaul

Upgrade the Antigravity Agentic Platform into a production-grade enterprise software development squad with:
1. **Dual-Mode Operator Architecture** (Seamless toggle between 2-Person 50/50 Dual-Lead Mode and Autonomous Solo-Dev Mode).
2. **Next-Generation Open-Source Harness** (Migrating from the dummy static evaluator to a Nous Hermes / SWE-agent closed-loop dynamic behavioral evaluation harness).
3. **Hierarchical Enterprise Product Squad Simulation** (Formalizing 6 specialized agent personas: Product Owner, System Architect, Core Engineer, Adversarial SDET, AppSec Auditor, and Technical Writer).
4. **Anti-Green Signal Trap Enforcement** (Mandatory Test-First Red-to-Green gating and Mutation Testing to eliminate tautological tests and superficial mock implementations).
5. **Contract-First Schema & Reactive State Machine Gating** (Preventing frontend/backend disconnects and multi-tab state loss).

---

## User Review Required

> [!IMPORTANT]
> **Key Architecture Decisions for Operator Review**:
> 1. **Default Mode Setting**: We propose defaulting the repository to `mode: solo` so individual developers can immediately build without running two physical workstations, while preserving `mode: dual` via `npm run mode:dual` for team collaboration.
> 2. **Harness Selection**: We recommend adopting a hybrid **Hermes-SWE Evaluation Harness**:
>    - **Hermes Runtime Model**: Memory vault indexing via SQLite FTS5, progressive skill accretion, and subagent persona isolation.
>    - **SWE-bench Dynamic Verification**: Headless execution in isolated process jails where tests MUST fail on a clean baseline before being marked fixed by code.
> 3. **Mutation Testing Threshold**: For any new feature or module, we propose enforcing a **Mutation Score threshold of ≥ 80%** (i.e. at least 80% of deliberately injected mutants must fail tests) to permanently eliminate tautological tests.

---

## Open Questions

> [!NOTE]
> 1. **Automated Headless Browser in CLI**: For frontend projects, should the autonomous SDET run headless Playwright by default during local verification runs, or require an explicit flag (`--browser-e2e`) to conserve memory on low-resource machines? (Recommended: Default to headless Playwright when frontend files exist).
> 2. **LLM Persona Routing**: Should the 6 roles use differentiated system prompts and reasoning profiles (e.g. Architect and SDET configured with high-reasoning temperature/effort, while Coder uses deterministic low-temperature generation)? (Recommended: Yes).

---

## Proposed Changes

```
               ┌────────────────────────────────────────────────────────┐
               │           TARGET ENTERPRISE ARCHITECTURE               │
               └────────────────────────────────────────────────────────┘
                                           │
         ┌─────────────────────────────────┴─────────────────────────────────┐
         ▼                                                                   ▼
┌──────────────────┐                                                ┌──────────────────┐
│  MODE 1: SOLO    │                                                │  MODE 2: DUAL    │
│  Single Dev      │                                                │  2 Workstations  │
│  Autonomous Squad│                                                │  Computer1/2     │
└────────┬─────────┘                                                └────────┬─────────┘
         │                                                                   │
         └─────────────────────────────────┬─────────────────────────────────┘
                                           │
                                           ▼
┌───────────────────────────────────────────────────────────────────────────────────────┐
│                          HIERARCHICAL AGILE PRODUCT SQUAD                             │
├───────────────────────────────────────────────────────────────────────────────────────┤
│ 1. Product Manager (PRD & User Journey Specifications)                               │
│ 2. System Architect (Zod / Pydantic Typed Contracts & FSM State Transition Specs)     │
│ 3. Adversarial SDET (Black-Box Tests written FIRST; Verified RED before coding)      │
│ 4. Core Engineer (Implements logic until SDET tests turn GREEN)                       │
│ 5. Mutation Guard (Injects AST mutations; verifies mutants are KILLED)                │
│ 6. AppSec / Styx Auditor (DAST Pentest, Constant-time checks, Zero-Secret Shield)     │
│ 7. Technical Writer (6-Technique Cognitive Dossier, OpenAPI & Release Runbook)       │
└───────────────────────────────────────────────────────────────────────────────────────┘
                                           │
                                           ▼
┌───────────────────────────────────────────────────────────────────────────────────────┐
│                       NEXT-GEN DYNAMIC EVALUATION HARNESS                             │
│   (Hermes-style SQLite FTS5 Memory + SWE-agent Dynamic Red-to-Green Test Jail)        │
└───────────────────────────────────────────────────────────────────────────────────────┘
```

---

### Component 1: Dual/Solo Operator Mode Architecture

Enable solo developers to command the entire multi-agent squad without needing two physical machines or manual lease handoffs, while keeping the dual-workstation protocol for distributed teams.

#### [MODIFY] [scripts/role-switch.ts](file:///c:/Users/Deepak%20Sharma/OneDrive/Desktop/scripts/scripts/role-switch.ts)
- Add `mode` command (`npm run mode:solo`, `npm run mode:dual`, `npm run mode:status`).
- When in `solo` mode:
  - Domain lease locks are automatically acquired by the active session.
  - Role handoffs do not block on external workstation network pulls; instead, the orchestrator invokes the autonomous Beta subagent locally to perform the adversarial audit.
  - Preserves local audit trail in `.agents/state/active-role.json`.

#### [MODIFY] [scripts/lock-manager.ts](file:///c:/Users/Deepak%20Sharma/OneDrive/Desktop/scripts/scripts/lock-manager.ts)
- Add `isSoloMode()` check.
- In solo mode, avoid throwing lock conflict errors against the local operator while strictly enforcing domain boundaries between concurrent subagent runs.

#### [MODIFY] [package.json](file:///c:/Users/Deepak%20Sharma/OneDrive/Desktop/scripts/package.json)
- Add npm scripts:
  - `"mode:solo": "node --experimental-strip-types scripts/role-switch.ts mode solo"`
  - `"mode:dual": "node --experimental-strip-types scripts/role-switch.ts mode dual"`
  - `"mode:status": "node --experimental-strip-types scripts/role-switch.ts mode status"`
  - `"squad:run": "python -m scripts.orchestrator.squad_orchestrator"`
  - `"test:mutation": "node --experimental-strip-types scripts/mutation-tester.ts"`
  - `"harness:dynamic": "node --experimental-strip-types .agents/harness/dynamic-eval-runner.ts"`

---

### Component 2: Next-Gen Evaluation Harness (Hermes & SWE-agent Architecture)

Replace the static dummy evaluator (`.agents/harness/eval-runner.ts`) with a real dynamic behavioral harness.

#### [NEW] [.agents/harness/dynamic-eval-runner.ts](file:///c:/Users/Deepak%20Sharma/OneDrive/Desktop/scripts/.agents/harness/dynamic-eval-runner.ts)
- **Real Execution Pipeline**:
  - Spawns tasks in isolated sandboxed child processes.
  - Injects adversarial prompts into the agent loop.
  - Dynamically inspects generated files using TypeScript AST (`typescript` compiler API) to verify zero undeclared package imports.
  - Executes unit and E2E test commands and validates real exit codes (`0` vs `1`).
  - Verifies generated dossiers against all 6 mandatory Part 7 techniques with strict regex and section parsers.

#### [NEW] [.agents/harness/harness-contracts.json](file:///c:/Users/Deepak%20Sharma/OneDrive/Desktop/scripts/.agents/harness/harness-contracts.json)
- Replaces `golden-evals.json` with comprehensive execution benchmarks:
  - Anti-hallucination AST test contract.
  - Sycophancy & security rejection contract.
  - State machine persistence contract.
  - Mutation test kill-rate contract.
  - Part 7 Feynman compression & failure-path audit contract.

---

### Component 3: Hierarchical Enterprise Product Squad (`scripts/orchestrator/`)

Implement the multi-persona enterprise software company simulation to end the "shallow scaffolding" and "vanity metrics" traps.

#### [NEW] [scripts/orchestrator/squad_orchestrator.py](file:///c:/Users/Deepak%20Sharma/OneDrive/Desktop/scripts/scripts/orchestrator/squad_orchestrator.py)
- Manages the hierarchical pipeline across 6 distinct personas:
  1. **Product Manager**: Deconstructs user prompt into a structured Functional Specification (`specs/functional_spec.json`) with concrete user journeys, forbidden states, and acceptance criteria.
  2. **System Architect**: Outputs formal data schema contracts (`specs/contracts/schema.ts` or Pydantic models) and finite state machine transition tables.
  3. **Adversarial SDET**: Takes the Schema and Functional Spec and writes unit + integration tests **before any feature code is written**. Verifies that tests fail on empty stubs (**Red Phase**).
  4. **Core Engineer**: Implements production logic to turn the SDET's tests **Green**.
  5. **Adversarial Code Reviewer / Mutation Guard**: Injects mutations into the code (inverting comparisons, omitting state updates) to verify that SDET tests catch all mutants.
  6. **Technical Writer**: Synthesizes the 6-technique comprehension dossier, OpenAPI schema, and release runbook.

#### [MODIFY] [scripts/orchestrator/task_dispatcher.py](file:///c:/Users/Deepak%20Sharma/OneDrive/Desktop/scripts/scripts/orchestrator/task_dispatcher.py)
- Update CLI dispatching:
  - Add `--squad` flag to run the full hierarchical enterprise loop.
  - Route `--task code` through the mandatory Red-to-Green + Mutation feedback loop.
  - Route `--task solution` to output machine-readable TypeScript/Python schema contracts in addition to human markdown dossiers.

#### [MODIFY] [scripts/orchestrator/coding_engine.py](file:///c:/Users/Deepak%20Sharma/OneDrive/Desktop/scripts/scripts/orchestrator/coding_engine.py)
- Enforce the **Red-to-Green Test Invariant**:
  - Step 1: Run newly generated test against existing code -> **Must fail (Exit code != 0)**. If it passes immediately, reject test as tautological!
  - Step 2: Write implementation.
  - Step 3: Run test again -> **Must pass (Exit code == 0)**.
  - Step 4: Run mutation test -> **Must kill all mutants**.

---

### Component 4: Anti-Green Signal Trap & Mutation Testing Engine

#### [NEW] [scripts/mutation-tester.ts](file:///c:/Users/Deepak%20Sharma/OneDrive/Desktop/scripts/scripts/mutation-tester.ts)
- A lightweight, native TypeScript mutation testing engine:
  - Injects 4 standard mutant classes into target files:
    1. **Boundary Inversion**: `>` to `<=`, `<` to `>=`, `===` to `!==`.
    2. **Return Value Mutation**: `return true` to `return false`, `return data` to `return []` / `return null`.
    3. **Arithmetic / Assignment Mutation**: `+` to `-`, `*` to `/`.
    4. **State Bypass Mutation**: Commenting out state persistence / emit calls.
  - Executes the test suite for each mutant.
  - Calculates the **Mutation Score**: $\frac{\text{Killed Mutants}}{\text{Total Mutants}} \times 100\%$.
  - Fails with exit code `1` if Mutation Score $< 80\%$, preventing false-green test suites from shipping.

---

### Component 5: Governance & Documentation Updates

#### [MODIFY] [AGENTS.md](file:///c:/Users/Deepak%20Sharma/OneDrive/Desktop/scripts/AGENTS.md)
- Formalize **Directive 11: Dual-Mode Operation (Solo vs Dual Operator)**:
  - Document Solo Mode autonomous squad execution vs Dual Mode distributed pairing.
- Formalize **Directive 12: Anti-Green Signal Trap & Red-First Testing Invariant**:
  - Forbid writing tests that pass without implementation.
  - Enforce mutation testing and observable outcome verification.
- Formalize **Directive 13: Universal Reactive State Store Mandate**:
  - Forbid isolated local state for multi-screen/multi-step workflows.

#### [MODIFY] [GEMINI.md](file:///c:/Users/Deepak%20Sharma/OneDrive/Desktop/scripts/GEMINI.md)
- Add rules for Solo Mode vs Dual Mode operations and strict test-first discipline.

#### [MODIFY] [README.md](file:///c:/Users/Deepak%20Sharma/OneDrive/Desktop/scripts/README.md)
- Add quickstart guides for both Solo Developer workflows and Dual-Workstation enterprise setups.
- Document the 6-persona enterprise squad commands.

---

## Verification Plan

### 1. Automated Behavioral & Dynamic Harness Validation
- Run dynamic behavioral harness:
  ```bash
  npm run harness:dynamic
  ```
  Must verify real AST inspection, real command execution, and exit code verification.

### 2. Solo vs Dual Mode Switching Verification
- Run mode commands:
  ```bash
  npm run mode:solo
  npm run role:status
  npm run mode:dual
  npm run role:status
  npm run mode:solo
  ```
  Verify state JSON transitions cleanly and locks adapt appropriately.

### 3. Mutation Testing Engine Verification
- Run mutation tester on core modules:
  ```bash
  npm run test:mutation
  ```
  Verify that surviving mutants cause build failure and killed mutants produce a high passing score.

### 4. Enterprise Squad Orchestrator Test
- Run `python -m unittest tests/test_squad_orchestrator.py` to verify:
  - PM generates functional spec.
  - Architect generates typed contract.
  - SDET writes failing test (verified Red).
  - Coder implements logic (verified Green).
  - Mutation tester kills mutants.
  - Technical writer generates complete 6-technique dossier.

### 5. Full System Regression Suite
- Run complete existing suite:
  ```bash
  npm test
  pytest tests/
  npm run check:secrets
  ```
  Verify 100% green pass rate without any secrets or regressions.
