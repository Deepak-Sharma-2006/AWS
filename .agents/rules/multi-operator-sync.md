# Rule: Multi-Operator Synchronization & Dynamic Role Inversion

## Purpose
Coordinates concurrent work between Computer 1 and Computer 2, eliminates file overwrite collisions via distributed lease locking, and enforces dynamic role inversion.

## The Dynamic Alpha <-> Beta Alternating Protocol

### 1. Functional Roles
- **Alpha (Primary Author & Implementer)**:
  - Leads architecture design and writes Architecture Decision Records (ADRs).
  - Authors feature code and deterministic unit tests.
  - Generates the initial Phased Code Reading Dossier (`docs/dossiers/phase-X.md`).
- **Beta (Adversarial Critic & Quality Auditor)**:
  - Convenes the 5-Advisor Claude Council for code review.
  - Executes Styx dynamic red-team penetration testing (DAST) on live containers.
  - Audits failure paths, account enumeration risks, and timing differentials.
  - Approves and merges the phase PR.

### 2. Symmetrical Phase Alternation
- Project phases strictly alternate roles between Computer 1 and Computer 2:
  - **Odd Phases (1, 3, 5, 7, ...)**: Computer 1 = Alpha; Computer 2 = Beta.
  - **Even Phases (2, 4, 6, 8, ...)**: Computer 2 = Alpha; Computer 1 = Beta.
- Neither operator is confined to a single domain. Both achieve 50% authoring and 50% auditing contribution.

### 3. Distributed Lease Locking
- Every domain mutation requires an active lease lock in `.agents/state/locks/<domain>.lock.json`.
- A lease specifies:
  - `domain`: Feature domain (e.g., `auth`, `billing`, `database`).
  - `operator`: `Computer1` or `Computer2`.
  - `role`: `Alpha` or `Beta`.
  - `expiresAt`: ISO 8601 expiration timestamp (default TTL: 3600s).
- Any attempt by an operator or agent to edit files in a locked domain without holding the active lease is rejected.
- Transfer of ownership occurs explicitly via `scripts/lock-manager.ts transfer`.
