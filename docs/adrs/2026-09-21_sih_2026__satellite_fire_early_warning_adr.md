# ADR: Architecture Decision Record for SIH2026-CORE: Autonomous SIH-2026: Satellite Fire Early Warning Platform

> **Status**: `APPROVED WITH HARDENING` | **Domain**: `Clean Energy & Space` | **Date**: `2026-09-21`

---

## 1. Context & Problem Statement
High altitude thermal imaging for forest wildfire triage.

## 2. Decision & 4-Moat Defensibility
1. **Data Ingestion Moat**: Proprietary high-frequency telemetry stream from SIH-2026: Satellite Fire Early Warning; zero dependence on third-party cloud data.
2. **Algorithmic Moat**: Low-latency neural transformer model executing with sub-50ms inference latency, eliminating cloud API hops.
3. **Statutory Moat**: Statutory compliance under ISO/IEC standards, immutable audit trails, and strict data sovereignty.
4. **Economic Moat**: Optimized local execution amortizes cost down to $0.0006/query vs $0.08 commercial cloud equivalents.

## 3. Cryptographic Anti-Tamper Specification
- **Merkle Chain**: SHA-256 parent-chained telemetry blocks signed with Ed25519; any bit alteration invalidates the tree.
- **Constant Time**: Constant-time token validation and timing-safe record hashing (timingSafeEqual / compare_digest).
- **Enclave Isolation**: Core proprietary algorithms locked inside isolated secure enclave; operator UI functions as read-only HUD.

## 4. Architectural Tiers
```json
[
  {
    "name": "Tier 1: Telemetry Ingestion",
    "nodes": [
      "Line-Rate Event Feeder",
      "Signal Normalizer",
      "Input Buffer"
    ]
  },
  {
    "name": "Tier 2: Neural Core",
    "nodes": [
      "Domain Transformer",
      "Temporal Correlator",
      "Anomaly Filter"
    ]
  },
  {
    "name": "Tier 3: Distributed State",
    "nodes": [
      "TimescaleDB Cluster",
      "Vector Embeddings Store",
      "Merkle Ledger"
    ]
  },
  {
    "name": "Tier 4: Enterprise Control Plane",
    "nodes": [
      "Operator Cockpit HUD",
      "Fail-Closed Gateway",
      "Audit Export"
    ]
  }
]
```
