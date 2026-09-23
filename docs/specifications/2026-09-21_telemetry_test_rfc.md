# RFC: TELEMETRY_TEST Contract Specification

> **Scope**: `telemetry_test` | **Persona**: `System Architect` | **Type**: `Formal Contract & FSM Schema`

---

## 1. Finite State Machine (FSM) States
`IDLE`, `RUNNING`, `COMPLETED`, `FAILED`, `CERTIFIED`

### Transitions:
| Source State | Target State | Trigger Event |
| :--- | :--- | :--- |
| `IDLE` | `RUNNING` | `START_JOB` |
| `RUNNING` | `COMPLETED` | `EXECUTION_SUCCESS` |
| `RUNNING` | `FAILED` | `EXECUTION_ERROR` |
| `COMPLETED` | `CERTIFIED` | `AUDIT_SIGN_OFF` |

---

## 2. Typed Data Schemas
```json
{
  "CaseState": {
    "case_id": "string",
    "status": "enum(IDLE, RUNNING, COMPLETED, FAILED, CERTIFIED)",
    "calculated_confidence": "float (0.0 to 1.0)",
    "evidence_nodes": "list[string]",
    "updated_at": "ISO-8601 string"
  }
}
```

---

## 3. API Contract Endpoints
| HTTP Method | Path | Response Type |
| :--- | :--- | :--- |
| `GET` | `/api/status` | `CaseState` |
| `POST` | `/api/execute` | `JobReceipt` |
