# Rule: Human Operator Code Comprehension (The 6-Technique Phased Dossier)

## Purpose
Governs the generation of standardized, phased code reading documentation so the human operator and peer agents understand every line, data flow, and failure path in depth.

## Mandatory Handoff Requirement
At the conclusion of each phase, before any code is merged from `feat/phase-X` to `main`, the Alpha operator must generate:
`docs/dossiers/phase-<X>-<domain>.md`

## The 6 Mandatory Techniques

### Technique 1: The Human Mental Model
- State in 2–3 plain English paragraphs:
  1. What real-world problem does this component solve?
  2. What is strictly inside its responsibility boundary?
  3. What is explicitly outside its scope?

### Technique 2: Visual Code Flow (The Call Graph)
- Provide an ASCII or Mermaid diagram illustrating:
  - Inbound Entry Point (HTTP route, RPC, or CLI command).
  - Middleware & Validation Gates.
  - Core Domain Service execution.
  - Database / External Infrastructure persistence.
  - Outbound Egress response.

### Technique 3: Variable Lifecycle Trace (Follow the Data)
- Detail the lifecycle of the core entity (e.g., `user`, `session`, `paymentIntent`):
  - **Birth**: How and where the variable is initialized.
  - **Mutation**: Transformations, hashing, sanitization.
  - **Packaging**: Wrapping into response DTOs or JWT claims.
  - **Egress / Death**: Transmission to client and garbage collection.

### Technique 4: Non-Blocking Noise Filtering
- List all telemetry, audit loggers, analytics, and non-essential middleware that were bypassed during Pass 1 to keep cognitive focus on the primary business logic.

### Technique 5: Audit Exactly One Failure Path
- Pick one critical failure scenario and verify:
  1. **Account Enumeration**: Are error messages identical when a resource exists vs. when it does not?
  2. **Timing Differential ($\Delta t$)**: Is constant-time verification (`crypto.timingSafeEqual`) used to prevent timing attacks?

### Technique 6: The 1-Sentence Feynman Compression Test
- Conclude with a single, dense, jargon-free summary sentence:
  *"[Verb] [Target Entity] via [Mechanism], verify [Condition], and return [Result]."*
- The peer auditor (Beta) must read and pass this compression test before signing off.
