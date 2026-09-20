# Rule: Anti-Hallucination & Grounding Shield

## Purpose
Enforces absolute grounding of all code, dependencies, symbols, and test assertions. Eliminates ghost packages, fabricated APIs, and sycophantic assumptions.

## Invariants & Guardrails

### 1. Package Registry & Dependency Guard
- An agent is strictly prohibited from generating `import` statements for packages not present in `package.json`.
- When an agent believes a new library is necessary:
  1. It must check whether existing native libraries (e.g., `crypto`, `node:fs`, `node:path`) can satisfy the requirement.
  2. If an external package is indispensable, it must run `npm info <package>` or check the local registry to verify package health, maintenance, and CVE count.
  3. It must log a formal dependency proposal and request human operator sign-off before modifying `package.json`.

### 2. AST & Symbol Grounding
- Never guess function parameters, return types, or class names.
- Before invoking a helper function or method from another module, use `grep_search` or slice-bounded `view_file` to inspect the exact signature.
- If a method does not exist in the active codebase, do NOT fabricate it. Implement it explicitly or ask the operator.

### 3. Empirical Test & Verification Grounding
- An agent must NEVER write: *"All tests pass and the service is working"* unless it has physically executed the test command in the terminal and captured exit code `0`.
- Simulated mental runs do not constitute verification.

### 4. Anti-Sycophancy Rejection
- When evaluating user or peer agent code, do NOT offer unconditional praise or agree with logically flawed architectures.
- If an architectural choice introduces a security vulnerability (e.g., plaintext secrets, missing RLS, unescaped queries), you must raise a formal objection and suggest the secure alternative.
