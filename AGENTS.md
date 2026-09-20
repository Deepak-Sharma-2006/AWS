# Antigravity Workspace Invariants & Operational Directives

> **Scope**: Applied automatically to all agent invocations (both Antigravity IDE and Antigravity CLI `agy`) across this entire workspace.

---

## 1. Zero-Hallucination & Dynamic Dependency Policy

1. **Dynamic Dependency Architecture & Zero Ghost Packages**:
   - Dependencies are dynamic and permitted if they provide a demonstrable, measurable advantage over standard library implementations (e.g., performance, robust schema parsing, standardized protocol handling).
   - Before introducing any new dependency, you MUST inspect `package.json`. If a new package is required, it must be explicitly declared in `package.json` with an exact pinned version.
   - NEVER invent, assume, or import an npm package or library that is not explicitly declared in `package.json`.
   - The Anti-Hallucination Shield (`npm run check:hallucinations`) strictly scans AST imports across the entire codebase to reject undeclared packages.
2. **Strict Symbol & File Grounding**:
   - Every citation of a file, type, function, or API must be grounded in verified project evidence.
   - You MUST cite clickable markdown links using the `file://` scheme with forward slashes: `[SymbolName](file:///path/to/file.ts#L15-L30)`.
   - If context is missing or ambiguous, you MUST state: `"INSUFFICIENT CONTEXT DETECTED: Unable to ground symbol in codebase."` DO NOT guess, fabricate, or improvise missing APIs.
3. **Empirical Execution Grounding**:
   - NEVER assert that "tests pass", "build succeeds", or "vulnerabilities are fixed" based on mental simulation.
   - You must execute the relevant shell command (`npm test`, `tsc --noEmit`, or test runner) and verify an exit code of `0`.

---

## 2. Enterprise 2-Person Dual-Lead Architecture & Domain Leases (50/50 Balance)

1. **50/50 Co-Equal Enterprise Leadership**:
   - The workspace operates as a balanced two-person engineering team, translating an entire enterprise engineering organization into two co-equal leads:
     - **Lead 1 (Alpha / Feature Architect & Core Domain Lead - 50% Workload)**: Owns domain modeling, business logic, public API contracts, white-box unit TDD (`tests/unit/`), and system architecture dossiers.
     - **Lead 2 (Beta / Adversarial Systems, SDET & Product Lead - 50% Workload)**: Owns independent black-box adversarial suites (`tests/adversarial/*.test.ts`), concurrency & race fuzzing, malicious payload injection, AppSec DAST pentesting, product/UX ergonomics certification, and production release sign-off.
2. **Independent Adversarial Test Authoring Mandate**:
   - Lead 1 (Alpha) is strictly prohibited from writing or tampering with `tests/adversarial/`. Only Lead 2 authors adversarial tests.
   - Lead 2 must probe edge cases, race conditions, memory bounds, and fault injections that Lead 1's unit tests never contemplated.
3. **Lead 2 Hardening Authority**:
   - Lead 2 is NOT a passive spectator. Upon receiving a phase handoff, Lead 2 holds the **Hardening & Verification Lease** and is fully authorized to directly author hardening patches, input sanitizers, race-condition mutexes, and performance optimizations directly in `src/`.
4. **Distributed Lease Locking & Multi-Domain Concurrency**:
   - Developers acquire exclusive domain leases via `npm run lock:acquire --domain <name>`.
   - Independent domains (e.g. `core` and `adversarial`) can be developed concurrently without collisions.
   - Phase handoffs (`npm run role:handoff`) atomically transfer domain leases, enforce zero-secret scans, and invert roles on phase advancement ($N \rightarrow N+1$).

---

## 3. Human Operator Code Comprehension Protocol (Part 7 Mandate)

1. **Mandatory Phase Dossier Generation**:
   - At the completion of each feature phase, before opening a PR or requesting merge, the agent MUST generate a structured comprehension dossier in `docs/dossiers/phase-<X>-<domain>.md`.
2. **The 6-Technique Structure**:
   - Technique 1: The Human Mental Model (Plain-language purpose & boundary).
   - Technique 2: Visual Code Flow (ASCII / Mermaid call graph).
   - Technique 3: Variable Lifecycle Trace (Birth $\rightarrow$ Transformation $\rightarrow$ Egress).
   - Technique 4: Non-Blocking Noise Filtering (Bypassing telemetry/logging on Pass 1).
   - Technique 5: Audit Exactly One Failure Path (Account enumeration & timing differential checks).
   - Technique 6: 1-Sentence Feynman Compression Test.

---

## 4. Token Economy & Adaptive Multi-Model Optimizer

1. **Progressive Disclosure & Skill Search**:
   - Do NOT load massive raw documentation or all skills into prompt context. Search skills dynamically via `npm run skill:search` or `scripts/skill-finder.ts`. Read only relevant sections using bounded file reading (`StartLine`/`EndLine`).
2. **Slice-Targeted File Reading**:
   - Avoid reading files $>150$ lines in their entirety. Use `grep_search` to locate target line numbers, then view the specific slice.
3. **Hard Loop Limits & Model Saturation**:
   - Max 5 auto-correction loops per task.
   - Respect model-specific context thresholds via `npm run token:budget`. If context saturation exceeds 70%, trigger context reduction, suppress verbose command outputs, and offload facts to Memory Vault.
4. **Token Budget Ceiling**:
   - Hard cap of 250,000 tokens per feature phase. If approaching warning thresholds, alert operator and prioritize context compression.

---

## 5. Code Quality & Security Standards

1. **Strict TypeScript**:
   - `strict: true` is enforced. Zero usage of `any`. Explicit interfaces/types for all function signatures.
2. **Deterministic TDD**:
   - Every new service, utility, or business logic component must have a corresponding test file (`*.test.ts`) using native Node test runner or Vitest.
3. **Millee 20-Point Security Hardening**:
   - Enforce row-level security (RLS), parameterized queries, constant-time comparisons (`crypto.timingSafeEqual`), and Argon2id password hashing.

---

## 6. Durable Context Persistence & Memory Vault

1. **Memory as Source of Truth**:
   - Cross-phase decisions, architectural rationales, and critical bug resolutions must be persisted to `.agents/memory/` using `npm run memory:save`.
   - Before starting complex tasks, recall relevant past learnings via `npm run memory:search`.
   - Phase handoffs must record a structured handoff document in `.agents/memory/team/handoffs/`.

---

## 7. Strict Zero-Secret Invariant & Pre-Commit Shield

1. **Absolute Zero Secrets Policy**:
   - Committing, staging, or pushing any secret, API key, access token, private key, or credential of any kind (including AWS, Stripe, GitHub, OpenAI, Anthropic, Google, Slack, RSA/SSH private keys, Bearer tokens, and `X-API-Key` values) to any git branch or repository is strictly forbidden.
   - Documentation, examples, and tests must EXCLUSIVELY use safe non-tokenized placeholders (e.g. `<YOUR_API_KEY>`, `YOUR_STRIPE_KEY`, `your-api-key-here`). NEVER use pseudo-realistic mock tokens (e.g. `sk_live_...`, `sk_test_...`) that trigger GitGuardian, Trufflehog, or GitHub Secret Scanning.
2. **Automated Shield & Hook Enforcement**:
   - All commits are gated by `.git/hooks/pre-commit`, which automatically executes `npm run check:secrets:staged`. Commits are rejected with exit code `1` if any secret or suspicious token pattern is detected.
   - The Zero-Secret Shield (`npm run check:secrets`) is permanently embedded as Layer 1 of the Adversarial Beta Audit (`npm run audit:beta`) and Probe 7/7 of the System Readiness Probe (`npm run readiness`).
   - Bypassing pre-commit hooks via `--no-verify` is strictly prohibited.

---

## 8. Universal Multi-Agent Orchestrator & Task Execution Directives

1. **Individual Modular Execution (Anti-Monolithic Invariant)**:
   - All tasks must be executed independently through [TaskDispatcher](file:///scripts/orchestrator/task_dispatcher.py) (`python -m scripts.orchestrator.task_dispatcher`):
     - **Task 1: Solution Formulation & White-Space Moat Strategy** (`--task solution`): Deconstructs problem statements, conducts mandatory live online search for real-world facts/regulations (anti-bias policy), benchmarks competitive commercial prior-art, establishes 10x technical moats, renders native ASCII/Unicode architecture diagrams, and commits architectural decisions to the SQLite Memory Vault (`.agents/memory/vault.sqlite`).
     - **Task 2: Code Implementation & Autonomous TDD Self-Healing** (`--task code`): Implements production business logic using an autonomous red-to-green TDD feedback loop (native Node or Python unittest). Mimics senior human experts to cover extreme edge cases (boundary limits, empty/null, malformed inputs, concurrency, unpredictable user actions). Enforces clean, idiomatic industry-standard code without unnecessary complexity, auto-patching up to 5 passes until 100% green, and emitting verifiable benchmark metrics (`specs/benchmark_metrics.json`).
     - **Task 3: Presentation Pitch Synthesis** (`--task presentation`): Generates competition-winning presentation pitch decks using [OmniDeck](file:///scripts/engine/) with 2D Flex/Grid geometry, 7 visual primitives, vector graphics, and cognitive layout density. Supports the default 6 championship archetypes as well as arbitrary user-defined custom slide archetypes and counts.
     - **System Audits & Readiness** (`--task audit`): Runs AppSec red-team scans and pre-commit secret scanners.
     - **Memory Vault Search & Recall** (`--task memory`): Retrieves indexed decisions, architectural notes, and handoffs from `.agents/memory/vault.sqlite`.
   - Never combine these 3 tasks into a single monolithic loop unless explicitly commanded by the operator.
2. **Two-Stage Presentation Protocol (Stage 1 PPTX -> Stage 2 Gated PDF)**:
   - OmniDeck compiles native `.pptx` first (<0.2s). Never auto-generate `.pdf` without explicit operator instruction (`--export-pdf`).

---

## 9. Enterprise Native Visual Documentation Standard

1. **Native Markdown Diagrams, Workflows & Charts**:
   - Human-facing documentation (`implementation_plan.md`, `walkthrough.md`, phase dossiers) must use clear, universally-rendering native Markdown diagrams (ASCII/Unicode box-drawing, workflow pipelines), structured data tables, and benchmark matrices.
2. **Zero Resource Waste & Zero Broken Image Icons**:
   - Do NOT waste system resources generating external image files for markdown documents.
   - Never embed fragile local image paths (`![Caption](...)`) that risk failing to render or displaying broken image icons in markdown viewers.
3. **Executive Visual Design Hierarchy**:
   - Documentation must be styled as C-level Enterprise Engineering Deliverables: sleek typography, executive summary cards, comparative capability matrix tables, verified empirical benchmarks, and clear operational commands.

---

## 10. Mandatory Adversarial Council Hardening Invariant (claude-council)

1. **Mandatory Council Hardening on All Plans & Solutions**:
   - Every implementation plan, architectural decision record (ADR), and solution blueprint MUST be hardened through the 5-Advisor Claude Council (`claude-council`) before execution or merge.
   - The 5 unaligned perspectives must be explicitly documented in the deliverable:
     - **The Contrarian (`01-contrarian`)**: Attacks foundational assumptions, seeks single points of failure, and demands failure-mode mitigations.
     - **The First-Principles Engineer (`02-first-principles`)**: Strips jargon, auditing raw algorithmic complexity, latency physics, and deterministic type safety.
     - **The Expansionist (`03-expansionist`)**: Identifies 10x defensible moats, asymmetrical leverage, and future-proof extensibility.
     - **The Naive Outsider (`04-outsider`)**: Audits cognitive ergonomics, eliminating over-engineering and obscure naming.
     - **The Pragmatic Executor (`05-executor`)**: Demands concrete migration runbooks, rollback mechanics, and verified empirical benchmarks.
2. **Unanimous Council Verdict & Non-Negotiable Moats**:
   - Every solution must achieve an explicit Council Verdict (`APPROVED WITH HARDENING`) and pass the **Contrarian 4-Moat Test** (Data Ingestion, Algorithmic, Sovereign/Statutory, and Financial Unit Economics).
   - Solutions must incorporate **Cryptographic Anti-Tamper & Enclave Isolation Specifications** (SHA-256 Merkle chain-of-custody, constant-time `timingSafeEqual` security, and fail-closed state transitions) to ensure solutions are non-reproducible by generic AI prompts and resilient against reverse-engineering.



