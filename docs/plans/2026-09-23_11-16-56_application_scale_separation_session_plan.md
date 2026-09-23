# Architectural Implementation Plan: Application Scale Separation, Session Lifecycle Protocol & Template Release

This plan outlines the long-term enterprise solutions for:
1. **Chat Context Window & Compaction Management**: Standard operating protocol for human operators to achieve maximum LLM accuracy across feature phases.
2. **Application vs. Workflow Scale Separation**: Refactoring `scripts/project-scale-detector.ts` and `scripts/mutation-tester.ts` to evaluate scale strictly on the user's application codebase (`src/`, `app/`, `packages/`, etc.) rather than counting the agentic workflow's own harness code.
3. **Clean Template Release**: Staging, committing, and pushing the clean, fully-automated workflow template to the remote repository (`https://github.com/Deepak-Sharma-2006/script`).

---

## 1. User Review Required & Design Decisions

> [!IMPORTANT]
> **Doubt 1: Chat Context Window & Compaction Protocol (How to use for Maximum Accuracy)**:
> In enterprise agentic engineering, state is externalized to the repository (`docs/`, `.agents/memory/vault.sqlite`, and Git), NOT stored in transient chat memory.
> - **The Golden Rule**: **1 Chat Session = 1 Cohesive Feature Phase / Epic**.
> - During a phase, keep the same chat as long as saturation is `🟢 OPTIMAL (<40%)` or `🟡 MODERATE (40-65%)`.
> - Once the feature phase is complete (walkthrough generated, tests green), **start a fresh chat session for the next phase**.
> - **Autonomous Onboarding Handshake**: When a fresh chat starts, the agent autonomously inspects `docs/*/INDEX.md` and active state files (`.agents/state/`) on Turn 1—the human operator never needs to manually paste history.
> - **Token Economics of Recall**: Carrying an old chat forces the model to re-ingest **500,000+ tokens of stale logs and error traces on every turn**. Targeted index recall consumes **only ~1,500 to 2,500 tokens of distilled signal (0.2% of context)**, achieving a **99.6% token reduction** with 100% reasoning precision.

> [!IMPORTANT]
> **Doubt 2: Framework vs. Application Codebase Scale Separation**:
> Currently, `project-scale-detector.ts` counts the workflow's own scripts (`scripts/`, `docs/`, `demo/`), classifying a blank template as "MEDIUM".
> We update the detector to implement **Dual-Scope Classification**:
> - **Application Domain (`src/`, `app/`, `pkg/`, `packages/`, `lib/`, `backend/`, `frontend/`)**: Governs the codebase classification (`SMALL`, `MEDIUM`, `LARGE`) and mutation testing auto-scoping.
> - **Harness & Tooling (`scripts/`, `templates/`)**: Reported separately as infrastructure metadata.
> - A freshly cloned template will accurately register as `🟢 SMALL (Application Domain: <5k LOC)`, ensuring full mutation testing without false constraints.

---

## 2. Proposed Changes by Component

```
d:\workflow\
├── scripts\
│   ├── project-scale-detector.ts [MODIFY: Dual-scope separation: Application vs Workflow Harness]
│   └── mutation-tester.ts        [MODIFY: Scope mutations strictly to Application Domain]
├── tests\
│   └── workflow-upgrades.test.ts [MODIFY: Update tests to assert Application Domain scale metrics]
├── .gitignore                    [MODIFY: Ensure session-specific markdown drafts remain local]
├── docs/                         [VERIFY: Clean baseline living catalogs for template cloning]
└── Remote Push                   [EXECUTE: Clean commit & push to Deepak-Sharma-2006/script]
```

---

### Component 1: Dual-Scope Project Scale Detector

#### [MODIFY] [`scripts/project-scale-detector.ts`](file:///d:/workflow/scripts/project-scale-detector.ts)
- Define standard application directories: `src`, `app`, `pkg`, `packages`, `lib`, `backend`, `frontend`, `api`, `services`.
- Separate LOC counts:
  - `applicationLoc`: Lines of code in application directories.
  - `harnessLoc`: Lines of code in `scripts/`, `templates/`.
  - `documentationLoc`: Lines of code in `docs/`.
- Scale classification (`SMALL`, `MEDIUM`, `LARGE`) binds exclusively to `applicationLoc`.
- Display comprehensive dual-scope breakdown banner.

#### [MODIFY] [`scripts/mutation-tester.ts`](file:///d:/workflow/scripts/mutation-tester.ts)
- Bind `--diff` auto-scoping to `applicationLoc > 50,000 LOC`.
- Filter mutation targets strictly to application source files.

---

### Component 2: Session Lifecycle Protocol Documentation

#### [MODIFY] [`UNIVERSAL_AGENT_INSTRUCTIONS.md`](file:///d:/workflow/UNIVERSAL_AGENT_INSTRUCTIONS.md) & [`README.md`](file:///d:/workflow/README.md)
- Add the **Session Lifecycle & Compaction Protocol**:
  - Explains the Phase Boundary Rule (1 Chat = 1 Feature Phase).
  - Explains how memory vault externalization makes fresh chats lossless and 10x faster.
  - Documents how to monitor `context_telemetry` badges.

---

### Component 3: Clean Template Release to Remote Repository

- Configure `.gitignore` to keep ephemeral chat session documents local (`docs/plans/2026-09-23_...`, `docs/walkthroughs/2026-09-23_...`) while committing the clean template baseline living indexes (`docs/*/INDEX.md`).
- Execute clean git commit:
  `feat(workflow): enterprise zero-process hook, live context telemetry, team mesh reconciler, and scale separation`
- Push to `origin/main` (`https://github.com/Deepak-Sharma-2006/script`).

---

## 3. Verification Plan

### Automated Tests
```bash
# 1. Verify Application Scale Separation
npm run project:scale

# 2. Run Master Unit & Upgrades Suite
npm run test:unit

# 3. Verify Mutation Testing Scoping
node --experimental-strip-types scripts/mutation-tester.ts --diff

# 4. Verify Zero Secrets & Zero Hallucinations
npm run check:secrets
npm run check:hallucinations
npm run lint:markdown

# 5. Git Commit & Push
git commit ...
git push origin main
```
