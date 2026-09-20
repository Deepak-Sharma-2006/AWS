---
name: agentic-loop-runner
description: >-
  Executes the autonomous 4-part self-correcting feedback loop for software engineering tasks.
  Use this skill when implementing complex features, debugging failed tests, or refactoring code
  where automated test execution can verify correctness.
---

# Autonomous 4-Part Agentic Feedback Loop

This skill implements the self-correcting engineering loop pioneered by Claude Code and modern AI engineering:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                 THE 4-PART AUTONOMOUS EXECUTION LOOP                         │
├─────────────────┬─────────────────┬─────────────────┬───────────────────────┤
│ 1. CONTEXT      │ 2. PROTOCOL     │ 3. EXECUTION    │ 4. CRITIC & CORRECTION│
│ Gather AST,     │ Define plan,    │ Write code,     │ Run tests, inspect    │
│ types, & specs  │ tests, & diff   │ apply diff      │ errors, auto-fix      │
└─────────────────┴─────────────────┴─────────────────┴───────────────────────┘
```

## Step-by-Step Procedure

1. **Context Phase**: Read relevant types, active tests, and schema contracts.
2. **Protocol Phase**: Create deterministic test cases defining success criteria *before* modifying production code (TDD).
3. **Execution Phase**: Apply targeted code edits.
4. **Critic & Auto-Correction**:
   - Run test suite: `npm test` or `npx vitest run`.
   - If tests fail, inspect exact stack trace and apply correction.
   - Max 5 iterations allowed before escalating to human operator.
