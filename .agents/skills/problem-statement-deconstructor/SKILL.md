---
name: problem-statement-deconstructor
description: >-
  Systematic problem statement & requirements deconstruction engine for products. Use this skill when
  analyzing complex, ambiguous, or high-stakes problem statements, hackathon prompts, client briefs,
  or PRDs to extract root pain, implicit invariants, entity lifecycles, and a verifiable MVP spine.
metadata:
  origin: Antigravity-Governance
---

# Problem Statement Deconstructor — Product & Engineering Spec Engine

> **Trigger**: Run whenever receiving a hackathon prompt, client RFP/brief, complex issue description, or new product initiative before drafting implementation plans.
> **Principle**: *"A problem clearly understood is a problem half-solved."*

---

## 1. The Core Challenge

Problem statements in real engineering and competitive hackathons are rarely presented as clean technical specifications. They are usually:
- **Pain-Centric**: Focused on business frustration rather than system architecture.
- **Under-Specified**: Omitting crucial technical invariants (e.g., concurrency, rate limits, latency ceilings, zero hallucinations).
- **Over-Scraped**: Mixing immediate MVP necessities with ambitious 5-year vision items.

The **Problem Statement Deconstructor** transforms messy problem descriptions into crisp, deterministic engineering blueprints.

---

## 2. The 4-Stage Deconstruction Protocol

```
+-------------------------------------------------------------------------------+
|                      PROBLEM DECONSTRUCTION PIPELINE                          |
+-------------------------------------------------------------------------------+
| 1. ROOT PAIN TRIANGULATION   | What is the quantifiable human or system pain? |
| 2. INVARIANT EXTRACTION      | What are the explicit vs implicit invariants?  |
| 3. MVP SPINE ISOLATION       | What is the thinnest verifiable end-to-end?    |
| 4. VERIFICATION MATRIX       | How do we prove mathematically that it works?  |
+-------------------------------------------------------------------------------+
```

### Stage 1: Root Pain & Persona Triangulation
- **Primary Persona**: Who specifically hurts when this problem exists? (e.g., *"On-call engineer reviewing 200 alert emails per hour"* vs *"Retail customer waiting 5 seconds for cart checkout"*).
- **Quantified Pain Metric**: How is this pain measured? (e.g., latency, error rate, financial slippage, token burn, manual labor hours).
- **Current State Failure**: What happens today when they attempt to solve this?

### Stage 2: Invariant Extraction (Explicit vs Implicit)
Every problem statement contains two layers of constraints:
1. **Explicit Requirements**: Directly stated features (e.g., *"Must support Google OAuth"*, *"Must process CSV files up to 50MB"*).
2. **Implicit Invariants**: Unstated architectural imperatives that will break production if ignored:
   - *Security*: Constant-time token comparisons, zero secret leakage, RLS, Argon2id hashing.
   - *Concurrency*: Lease locking, idempotency keys, race condition protection.
   - *Reliability*: Zero ghost dependencies, fail-closed error boundaries, graceful retries.
   - *Performance*: Bounded token contexts, indexed queries, sub-second p95 responses.

### Stage 3: The MVP Spine vs Deferred Flesh
Separate the problem into three strict buckets:
- 🟢 **The Spine (Must Build First)**: The thinnest vertical slice that connects user input directly to the core value output.
- 🟡 **The Ergonomics (Build in Iteration 2)**: Polished CLI flags, rich dashboards, advanced filtering, automated notifications.
- 🔴 **The Anti-Goals (Explicitly Deferred)**: Multi-region failover, custom billing systems, complex ML recommenders.

### Stage 4: Verifiable Acceptance Matrix
Convert qualitative ambitions into deterministic test contracts:
- ❌ *"Make the system fast and responsive."*
- ✅ *"p95 endpoint response < 120ms under 50 concurrent requests (`tests/perf.test.ts`)."*
- ❌ *"Ensure reliable authentication."*
- ✅ *"Reject unauthorized requests with 401; enforce timing-safe comparison on session hashes (`tests/auth.test.ts`)."*

---

## 3. Standard Deconstruction Dossier Template

When executing this skill, output the findings in `docs/specs/problem-deconstruction.md`:

```markdown
# Problem Deconstruction Dossier: [Product Name]

## 1. Problem Statement & Root Pain
- **Original Prompt**: "[Verbatim User Prompt / Problem Excerpt]"
- **Target Persona**: [Primary User]
- **Core Friction**: [Quantifiable Pain Point]

## 2. Invariant Map
| Requirement Type | Invariant Description | Verification Mechanism |
| :--- | :--- | :--- |
| **Explicit** | [Directly requested feature] | [Unit/Integration test] |
| **Implicit Security** | [Timing-safe auth, zero ghost packages] | [AST Scanner + DAST Pentest] |
| **Implicit Concurrency** | [Lease locking on mutation] | [Lock Manager contract] |

## 3. The MVP Spine
1. Step 1: Ingest [Input payload]
2. Step 2: Validate via [Strict Schema]
3. Step 3: Execute [Core Domain Transformation]
4. Step 4: Persist via [Native Memory/SQLite]
5. Step 5: Deliver [Output/Response]

## 4. Anti-Goals (Strictly Deferred)
- ❌ [Deferred Item 1]
- ❌ [Deferred Item 2]
```

---

## 4. Integration with Other Skills

- Pair with `grill-me` when the problem statement has ambiguous gaps requiring interactive dialogue.
- Pair with `pdf-document-intelligence` when the problem statement is provided inside a PDF specification or slide deck.
- Pair with `agentic-loop-runner` to execute the verified MVP spine test-first.
