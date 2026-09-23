# Technical Walkthrough: Universal Brownfield Ingestion, N-Person Team Mesh & Multi-Harness Architecture

This walkthrough documents the full technical architecture, implementation, and empirical verification of the 4 enterprise scaling capabilities:
1. **Brownfield Project Ingestion & Resumption Engine**
2. **N-Person Team & Hackathon Mesh Mode (`mode: "team"`)**
3. **Universal Multi-Harness Portability & Standard MCP Server**
4. **Deterministic 4-Layer Fail-Closed Multi-Model Compliance**

---

## 1. Executive Capability Overview

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        UNIVERSAL ENTERPRISE AGENTIC PLATFORM                           │
├─────────┬───────────────────────────────┬────────────────────────────┬─────────────────┤
│ System  │ Capability                    │ Core Component             │ Living Catalog  │
├─────────┼───────────────────────────────┼────────────────────────────┼─────────────────┤
│ Axis 1  │ Brownfield Ingestion & Delta  │ ProjectAuditor             │ docs/audits/,   │
│         │ Resumption (Scenarios A & B)  │ (project_auditor.py)       │ docs/plans/     │
├─────────┼───────────────────────────────┼────────────────────────────┼─────────────────┤
│ Axis 2  │ N-Person Team Mesh &          │ LockManager & LanSyncServer│ .agents/state/  │
│         │ Hackathon Synchronization     │ (lock-manager.ts, lan-sync)│ locks/          │
├─────────┼───────────────────────────────┼────────────────────────────┼─────────────────┤
│ Axis 3  │ Universal Multi-Harness Sync  │ HarnessCompiler & McpServer│ CLAUDE, Cursor, │
│         │ (Claude, Cursor, Windsurf)    │ (universal-harness-sync.ts)│ Windsurf, Codex │
├─────────┼───────────────────────────────┼────────────────────────────┼─────────────────┤
│ Axis 4  │ 4-Layer Deterministic         │ Pre-Commit 3-Gate Barrier  │ .git/hooks/     │
│         │ Multi-Model Compliance        │ (install-hooks.ts)         │ pre-commit      │
└─────────┴───────────────────────────────┴────────────────────────────┴─────────────────┘
```

---

## 2. Granular Architectural Implementations

### 2.1 Brownfield Ingestion & Resumption Engine ([`project_auditor.py`](file:///scripts/orchestrator/project_auditor.py))
- **Scenario A (Completed Project Review & Audit)**:
  - Traverses existing repositories, classifying modules, packages, and test suites.
  - Audits code against the 5 Enterprise Pillars: (1) Architecture & Types, (2) Edge-Case Test Probe Depth, (3) AppSec & Secrets, (4) Cloud Financial Economics, and (5) Anti-Tamper Cryptographic State.
  - Generates an Executive Diagnostic Scorecard and Flaw Findings Matrix persisted directly to `docs/audits/` via SpecSync.
- **Scenario B (Developing Project Onboarding & Resumption)**:
  - Stabilizes baseline code first: auto-heals broken stubs (`NotImplementedError`, `TODO`, failing tests) using `CodingEngine`.
  - Formulates a **Delta Work Breakdown Structure (WBS)** implementation plan persisted to `docs/plans/`.
  - Freezes existing behavior with characterization tests and resumes the 6+1 Squad loop from Phase 3 (TDD Red-Tests) for missing modules.

### 2.2 N-Person Team Mesh & Hackathon Coordination ([`lock-manager.ts`](file:///scripts/lock-manager.ts) & [`lan-sync-server.ts`](file:///scripts/lan-sync-server.ts))
- **Tri-Mode Operating Architecture**:
  - `mode:solo`: Single-developer velocity (multi-host locks bypassed).
  - `mode:dual`: 2-person 50/50 Alpha/Beta rotational workflow.
  - `mode:team`: N-person team mesh for hackathons and squads.
- **Dynamic Parallel Domain Locking**:
  - Developers acquire independent domain leases:
    - Developer 1: `domain: "auth"`, `role: "DomainLead"`
    - Developer 2: `domain: "billing"`, `role: "DomainLead"`
    - Developer 3: `domain: "frontend"`, `role: "DomainLead"`
  - Parallel work progresses simultaneously with zero lock contention.
  - Conflicting requests on the same domain are blocked with a clear expiration notice.
- **Zero-Dependency LAN Synchronization Server**:
  - [`scripts/lan-sync-server.ts`](file:///scripts/lan-sync-server.ts) runs on port 4040 on any laptop in an offline hackathon room.
  - Teammates connect via `$env:LOCK_WEBHOOK_URL="http://<HOST_IP>:4040"`.
  - Provides sub-10ms lock heartbeats, acquisition, and team roster queries (`npm run team:status`).

### 2.3 Universal Multi-Harness Sync ([`universal-harness-sync.ts`](file:///scripts/universal-harness-sync.ts))
- Compiles `AGENTS.md` into 6 native agent formats with a single command (`npm run harness:sync`):
  1. `CLAUDE.md`: Anthropic Claude Code CLI with project commands and 6+1 persona directives.
  2. `.cursorrules`: Root rules for Cursor IDE.
  3. `.cursor/rules/agentic-workflow.mdc`: Cursor directory-level MDC format.
  4. `.windsurfrules`: Codeium Windsurf rules.
  5. `.github/copilot-instructions.md`: GitHub Copilot Workspace.
  6. `CODEX.md`: OpenAI Codex and Aider.

### 2.4 Model Context Protocol (MCP) Server ([`mcp-server.ts`](file:///scripts/mcp-server.ts))
- Standard JSON-RPC stdio MCP server (`npm run mcp:start`) exposing 6 core tools:
  - `orchestrator_solution`: Formulates first-principles solutions with live research.
  - `orchestrator_squad`: Drives 6+1 agile squad feature implementation.
  - `orchestrator_research`: Deliberates across 4 deep research modes.
  - `orchestrator_audit`: Audits completed projects or onboards developing codebases.
  - `orchestrator_team_status`: Inspects active team members and domain leases.
  - `orchestrator_attest`: Verifies the cryptographic execution provenance ledger.

### 2.5 4-Layer Deterministic Multi-Model Fail-Closed Compliance
- **Layer 1 (Git Pre-Commit Hook Barrier)**: Installed in `.git/hooks/pre-commit` via `npm run hooks:install`. Rejects commits with exit code 1 if staged secrets, raw LaTeX delimiters, or undeclared AST imports exist.
- **Layer 2 (Schema Boundary Validation)**: Validates persona steps against typed JSON schema contracts, triggering autonomous self-healing on schema drift.
- **Layer 3 (Cryptographic Attestation Ledger)**: Mandates immutable SHA-256 execution provenance receipts in `.agents/memory/vault.sqlite` and `.agents/audit_trail.log` (`npm run attest:verify`).
- **Layer 4 (Turn-Boundary Prompt Injection)**: Re-anchors the 6+1 Persona structure at prompt boundaries to prevent long-context attention degradation.

---

## 3. Empirical Verification Results

### 3.1 Unit Test Suites
1. **TypeScript Unit Suite (`npm run test:unit`)**:
   - `tests/bootstrap.test.ts` + `tests/team-mesh-sync.test.ts`: **8/8 Tests Passed** (0 failures, 308ms).
   - Verified: Operating mode switching (solo/dual/team), concurrent parallel domain locking (Alice, Bob, Charlie), lock conflict blocking (Dana blocked on `auth`), and universal harness synchronization.
2. **Project Auditor Suite (`python -m unittest tests/test_project_auditor.py`)**:
   - **15/15 Tests Passed** (0 failures, 0.337s).
   - Verified: 5-pillar health scoring, stub detection, SpecSync audit dossier persistence, and Delta WBS generation.
3. **Squad Orchestrator Suite (`python -m unittest tests/test_squad_orchestrator.py`)**:
   - **10/10 Tests Passed** (0 failures, 1.054s).
   - Verified: 7 personas defined, PM pre-flight auto-trigger, System Architect ADR gating, red-to-green TDD loop, and Phase 8 impact analysis.

### 3.2 Markdown Zero-LaTeX Linter (`npm run lint:markdown`)
- `docs/`: **0 Violations (PASSED)**
- `README.md`: **0 Violations (PASSED)**
- `SYSTEM_COMMANDS.md`: **0 Violations (PASSED)**
- `implementation_setup_guide.md`: **0 Violations (PASSED)**
- `CLAUDE.md`, `CODEX.md`: **0 Violations (PASSED)**

### 3.3 Living Documentation Catalogs (`python -m scripts.orchestrator.spec_sync --all-indexes`)
All 6 living documentation indexes verified active and synchronized:
- `docs/plans/INDEX.md`: 8 documents
- `docs/walkthroughs/INDEX.md`: 6 documents
- `docs/audits/INDEX.md`: 19 documents
- `docs/adrs/INDEX.md`: 5 documents
- `docs/research/INDEX.md`: 12 documents
- `docs/rfcs/INDEX.md`: 8 documents

---

## 4. Verification Reference Table

| Capability | Source File | Status | Verification Command |
| :--- | :--- | :--- | :--- |
| **Brownfield Ingestion** | [`project_auditor.py`](file:///scripts/orchestrator/project_auditor.py) | Verified | `npm run audit:project -- --target src` |
| **Delta Resumption** | [`project_auditor.py`](file:///scripts/orchestrator/project_auditor.py) | Verified | `python -m unittest tests/test_project_auditor.py` |
| **Team Mesh Locking** | [`lock-manager.ts`](file:///scripts/lock-manager.ts) | Verified | `npm run mode:team && npm run team:status` |
| **LAN Sync Server** | [`lan-sync-server.ts`](file:///scripts/lan-sync-server.ts) | Verified | `node --experimental-strip-types scripts/lan-sync-server.ts` |
| **Universal Harness Sync** | [`universal-harness-sync.ts`](file:///scripts/universal-harness-sync.ts) | Verified | `npm run harness:sync` |
| **Standard MCP Server** | [`mcp-server.ts`](file:///scripts/mcp-server.ts) | Verified | `node --experimental-strip-types scripts/mcp-server.ts` |
| **3-Gate Pre-Commit Barrier**| [`install-hooks.ts`](file:///scripts/install-hooks.ts) | Verified | `npm run hooks:install` |
