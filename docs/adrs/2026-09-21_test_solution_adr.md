# ADR: Architecture Decision Record for MEDGUARD: Real-Time Edge AI Waveform Sepsis Predictor

> **Status**: `APPROVED WITH HARDENING` | **Domain**: `AI / Defense` | **Date**: `2026-09-21`

---

## 1. Context & Problem Statement
Real-time sepsis prediction in ICU patients

## 2. Decision & 4-Moat Defensibility
1. **Data Ingestion Moat**: 100Hz bedside physiological waveform stream (ECG/PPG/Arterial line) unavailable in public datasets.
2. **Algorithmic Moat**: Cross-modal temporal waveform attention transformer predicting micro-vascular collapse 6 hours before shock.
3. **Statutory Moat**: Statutory HIPAA/DISHA patient privacy isolation, immutable RLS audit trails, and clinical trial compliance.
4. **Economic Moat**: Local edge inference node (42/mo hardware amortization) eliminates1,200/mo per-bed API subscriptions.

## 3. Cryptographic Anti-Tamper Specification
- **Merkle Chain**: Cryptographic Merkle tree linking every vitals sample to physician sign-off, rendering records unalterable.
- **Constant Time**: Constant-time token validation and timing-safe record hashing (timingSafeEqual / compare_digest).
- **Enclave Isolation**: Predictive clinical weights hosted inside isolated hospital enclave; doctor tablets act as read-only HUDs.

## 4. Architectural Tiers
```json
[
  {
    "name": "Tier 1: Bedside Telemetry",
    "nodes": [
      "ECG / PPG Feeder",
      "Arterial Line Streamer",
      "HL7 FHIR Gateway"
    ]
  },
  {
    "name": "Tier 2: Waveform Attention Core",
    "nodes": [
      "Temporal Convolution Net",
      "Cross-Modal Transformer",
      "Latency Buffer"
    ]
  },
  {
    "name": "Tier 3: Clinical Vault",
    "nodes": [
      "TimescaleDB Cluster",
      "Vector Embedding Store",
      "Audit Ledger"
    ]
  },
  {
    "name": "Tier 4: ICU Physician Cockpit",
    "nodes": [
      "Real-Time Alert HUD",
      "Vasopressor Titration Advisor",
      "EHR Sync"
    ]
  }
]
```
