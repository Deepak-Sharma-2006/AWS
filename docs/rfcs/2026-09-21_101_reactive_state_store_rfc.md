# RFC 101: Universal Centralized Reactive State Store & Fail-Closed Gating
## Summary:
Mandates that all multi-view applications store telemetry outputs and graph models in a single reactive, persistent store.
## Schema:
- appState: { currentTab: string, engines: Record<string, EngineOutput>, activeCase: CaseModel }
## Invariants:
Zero telemetry reset on tab navigation; fail-closed statutory certificate gating.
