# Rule: Strict Coding Standards & Modular Architecture

## Purpose
Enforces software craftsmanship, TypeScript typing contracts, deterministic unit test coverage, and anti-pattern avoidance.

## Directives
1. **TypeScript Strictness**:
   - `tsconfig.json` must enforce `"strict": true`, `"noImplicitAny": true`, and `"exactOptionalPropertyTypes": true`.
   - Never use `any` or `unknown as any`. Define concrete interfaces and types.
2. **Deterministic TDD**:
   - Every module must have automated unit tests (`*.test.ts`) covering normal flow, edge cases, and error handling.
   - Tests must run deterministically in $<500$ms without network calls (use mocks for external services).
3. **Anti-Pattern Purge (aj.on.ai)**:
   - Purge AI clichés: Avoid glowing floating purple buttons, generic dark mode without semantic tokens, and hallucinated icon names.
   - Use standard Shadcn UI components and Tailwind design tokens.
