---
name: grill-me
description: >-
  Interactive Socratic prompt & intent interrogation engine. Use this skill when a user prompt,
  feature request, or problem statement is underspecified, ambiguous, high-stakes, or needs
  rigorous probing of edge cases, architectural tradeoffs, and hidden assumptions before code is written.
metadata:
  origin: Antigravity-Governance
---

# Grill-Me — Socratic Prompt & Architectural Alignment Protocol

> **Trigger**: Run whenever starting an ambiguous feature, receiving a high-level product prompt, responding to `/grill-me`, or when a user's instructions contain hidden architectural tradeoffs.
> **Motto**: *"Five minutes of relentless probing prevents five days of re-architecting."*

---

## 1. Core Mission

Naive AI agents immediately start generating code upon receiving a vague prompt (e.g., *"build a notifications system"*, *"create a crypto trading bot"*, or *"add user management"*). This leads to misaligned architecture, missing edge cases, wasted token budgets, and fragile code.

The **Grill-Me** skill forces a high-signal Socratic interrogation to extract:
1. **The True Invariant Goal**: What must happen for this to be considered a 100% success?
2. **The Anti-Goals**: What are we explicitly *not* building in this phase?
3. **The Failure Modes**: How should the system behave when external services fail, inputs are corrupted, or rate limits hit?
4. **The Data & State Lifecycle**: What is the canonical schema, who owns mutations, and where does state persist?
5. **The Operator Workflow**: Exactly how will the human or system trigger, configure, and inspect this feature?

---

## 2. The 5-Dimension Drilldown Matrix

When executing Grill-Me, interrogate the prompt across these five distinct dimensions:

```
+-------------------------------------------------------------------------------+
|                            GRILL-ME 5-DIMENSION MATRIX                        |
+-------------------------------------------------------------------------------+
| 1. CORE OUTCOME      | What is the single measurable definition of done?       |
| 2. SCOPE BOUNDARIES  | What is in-scope vs deferred to Phase 2?                |
| 3. FAILURE PATHS     | What happens on timeout, network drop, or bad payload?  |
| 4. DATA CONTRACT     | What are the fields, types, and persistence guarantees? |
| 5. ERGONOMICS        | CLI flags vs config file vs API? What is the DX?        |
+-------------------------------------------------------------------------------+
```

---

## 3. Operational Workflow

### Step 1: Rapid Gap Assessment
Inspect the user prompt and identify:
- Underspecified terms (e.g., *"fast"*, *"secure"*, *"scalable"*, *"modern"*).
- Missing error handling expectations.
- Unstated dependency constraints (e.g., zero-external packages vs npm libraries).
- Unaddressed security boundaries (auth, encryption, secrets, authorization).

### Step 2: Formulate 3-5 High-Yield Socratic Questions
Present 3 to 5 sharply focused, multiple-choice or direct questions.
- **Rule 1**: Never ask generic questions (e.g., *"What do you think?"* or *"Can you give more details?"*).
- **Rule 2**: Provide concrete alternatives with tradeoffs clearly labeled.
- **Rule 3**: Challenge questionable technical decisions politely (e.g., *"You mentioned polling every 100ms; would SSE or a Redis Pub/Sub backplane be preferable to avoid socket exhaustion?"*).

#### Example Grill-Me Prompt:
```markdown
### 🎯 Grill-Me Architectural Clarifications

To ensure our implementation matches your exact intent, please clarify these 4 core decisions:

1. **Storage & Persistence**:
   - [A] (Recommended) Local SQLite via native `node:sqlite` (zero ghost dependencies, fully transactional).
   - [B] In-memory Map (fastest, but resets on process restart).
   - [C] External PostgreSQL / Redis (requires external service running).

2. **Error & Retry Policy**:
   - [A] Fail-closed with explicit error reporting and exponential backoff (max 3 retries).
   - [B] Fail-open with silent fallback to cached data.

3. **Interface Surface**:
   - [A] CLI command with both `--flag` and positional support (`npm run feature -- --id 123`).
   - [B] REST API endpoint (`POST /api/v1/feature`).

4. **Out-of-Scope Anti-Goals**:
   - Are we strictly deferring multi-tenant authentication and analytics to Phase 2?
```

### Step 3: Crystallize Intent into Memory Vault
Once the user answers, do **not** let this clarity fade into conversational scrollback. Immediately record the crystallized intent in the Memory Vault:
```bash
npm run memory:save -- --type decision --title "Intent Contract: <Feature Name>" --summary "<Summary of agreed scope, data schema, and boundaries>" --tags prompt,intent,architecture
```

---

## 4. Anti-Patterns to Avoid

- ❌ **The Passive Nodder**: Saying *"Sure, I will build that right away!"* when the prompt is full of ambiguities.
- ❌ **The 20-Question Interrogation**: Overwhelming the user with 15 granular questions. Limit to 3-5 high-impact questions.
- ❌ **The Open-Ended Essay**: Asking *"How do you want authentication to work?"* without providing concrete architectural patterns.
- ❌ **Ignoring Anti-Goals**: Failing to establish boundaries, resulting in scope creep and blown token budgets.

---

## 5. Verification Rubric

Before writing implementation code, verify:
- [ ] Non-negotiable definition of done is established.
- [ ] At least one adversarial failure path is explicitly accounted for.
- [ ] In-scope vs out-of-scope boundaries are documented.
- [ ] Intent Contract is saved to `.agents/memory/`.
