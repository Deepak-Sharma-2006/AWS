# ADR 001: Adoption of Universal 6-Class In-Repo Documentation & Git-Mergeable Memory
## Status: ACCEPTED
## Context:
Previous implementations suffered from the 'Chat Trap', where rich architectural decisions were lost in the conversation window.
## Decision:
We mandate 6 document classes in docs/ (plans, walkthroughs, audits, adrs, research, rfcs) with living INDEX.md catalogs and dual JSONL/SQLite memory persistence.
## Consequences:
Zero documentation loss; clean git mergeability across multi-operator workstations.
