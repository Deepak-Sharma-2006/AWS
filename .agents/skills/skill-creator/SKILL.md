---
name: skill-creator
description: >-
  Synthesizes and registers specialized new skills based on existing registry skills when a major
  real-world product improvement or technical metric breakthrough is required. Enforces strict
  anti-bloat justification gates and mandates transparent reporting to the user.
metadata:
  origin: Antigravity-Governance
---

# Skill Creator — Autonomous Skill Synthesis & Anti-Bloat Protocol

> **Trigger**: Activate at ANY stage of product discovery, planning, analysis, coding, debugging, or testing when a specialized workflow gap requires a new skill before delivering output to the user.
> **Cardinal Invariant**: *"Never create a skill for trivial conveniences. Every new skill must deliver a demonstrable, major leap in product capability or technical execution metrics, and must ALWAYS be reported to the user."*

---

## 1. Core Mission

The Antigravity harness maintains a curated library of 296+ skills. When facing novel domains, proprietary APIs, unique hackathon architectures, or specialized debugging scenarios, the agent can dynamically synthesize a **new, permanent skill** from the existing registry.

However, unchecked skill creation causes **skill bloat** (wasting token context and degrading search accuracy). The **Skill Creator** enforces a strict gatekeeper mechanism to ensure that only high-leverage, well-grounded skills are ever created.

---

## 2. The 3-Prong Strict Anti-Bloat Gate

Before creating any skill, the agent MUST evaluate and satisfy all three criteria:

```
+-------------------------------------------------------------------------------+
|                      THE 3-PRONG ANTI-BLOAT GATEWAY                           |
+-------------------------------------------------------------------------------+
| 1. COMPOSITION DEFICIT TEST | Can existing skills achieve this? (>80% overlap |
|                             | = HARD REJECTION: Compose existing skills).     |
| 2. MAJOR METRIC LEAP        | Does it provide a quantifiable major gain in    |
|                             | product value, latency, tokens, or accuracy?    |
| 3. RECURRENCE & BOUNDARY    | Is this a reusable, bounded workflow with clear |
|                             | operational directives and verification rubric? |
+-------------------------------------------------------------------------------+
```

### Criterion 1: The Composition Deficit Test
Search the existing registry via `npm run skill:search <keywords>`. If combining existing skills (e.g., `grill-me` + `fastapi-patterns` + `tdd-workflow`) already achieves 80%+ of the goal, **SKILL CREATION IS DENIED**. Compose existing skills instead.

### Criterion 2: The Major Metric Leap Test
The creation MUST be justified by a significant, measurable improvement:
- **Product Leap**: Enabling a novel product capability that was previously unachievable or error-prone (e.g., low-latency WebSocket order-book matcher, multi-agent arbitration engine, zero-loss ETL backpressure).
- **Engineering Metric Leap**:
  - **Latency / Performance**: e.g., Reducing response times from 1.2s to <80ms.
  - **Token Economy**: e.g., Reducing context window consumption by >50% via progressive data extraction.
  - **Debugging / Test Reliability**: e.g., Eliminating flaky concurrency race conditions with formal property checks.
  - **Security / Assurance**: e.g., Cryptographic Proof-of-Exploit verification for bespoke protocols.

### Criterion 3: Self-Contained Boundary Test
The skill must have unambiguous trigger conditions, 3-5 sharp operational rules, an actionable workflow, and a deterministic verification checklist.

---

## 3. Mandatory User Reporting Protocol

The agent **MUST ALWAYS** explicitly disclose any created skill in its response to the user. Never create skills silently.

### Required Reporting Format:
```markdown
### 🛠️ New Skill Synthesized: [<skill-name>](file:///absolute/path/to/SKILL.md)
- **Why It Was Created**: [Exact real-world problem or architectural gap encountered]
- **Inherited Parent Skills**: [List of base registry skills drawn from, e.g. `styx-pentest`, `backend-patterns`]
- **Measured / Expected Improvement**: [Quantifiable metric, e.g., 65% token reduction, sub-50ms streaming latency]
- **Verification Evidence**: [How the skill was tested and validated]
```

Furthermore, every skill creation automatically writes an audit record into the Memory Vault (`.agents/memory/project/decisions/`).

---

## 4. Operational Execution via Tooling

Execute skill creation using the CLI engine:

```bash
node --experimental-strip-types scripts/skill-creator.ts \
  --name <skill-name> \
  --desc "<Concise description of trigger and capability>" \
  --reason "<Detailed real-world problem justification (min 20 chars)>" \
  --metric "<Quantifiable metric improvement>" \
  --parents "<parent-skill-1>,<parent-skill-2>"
```

### Example:
```bash
node --experimental-strip-types scripts/skill-creator.ts \
  --name sse-telemetry-streaming \
  --desc "High-throughput Server-Sent Events telemetry stream with backpressure and reconnect safety" \
  --reason "Real-time client telemetry dashboard required sub-50ms event dispatch with zero socket leaks under network drops" \
  --metric "Sub-50ms streaming latency with 100% reconnection idempotency" \
  --parents "backend-patterns,motion-ui"
```

---

## 5. Verification Rubric

Before presenting results to the human operator:
- [ ] All 3 Anti-Bloat criteria evaluated and documented.
- [ ] New `SKILL.md` contains valid YAML frontmatter with `parents`, `targetMetric`, and `justification`.
- [ ] Memory Vault audit record created (`.agents/memory/project/decisions/`).
- [ ] Skill Finder registry index updated (`scripts/skill-finder.ts list`).
- [ ] Explicit disclosure table included in the final user response.
