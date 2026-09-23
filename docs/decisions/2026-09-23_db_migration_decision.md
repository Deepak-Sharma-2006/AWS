# ADR: DB_MIGRATION Architecture Decision Record

> **Scope**: `db_migration` | **Status**: `ACCEPTED` | **Persona**: `System Architect`

---

## 1. Context & Problem Statement
Architectural pivot and trade-off evaluation for `db_migration`.

## 2. Decision Outcome
Chosen design: FSM with 5 explicit states and fail-closed gate.
Rationale: Evaluated Postgres vs SQLite; chose SQLite for sub-50ms local zero-cloud latency.

## 3. Trade-offs Evaluated
- Chosen: Centralized reactive state machine with fail-closed gates.
- Rejected: Unbounded event emitters with implicit state mutations.
