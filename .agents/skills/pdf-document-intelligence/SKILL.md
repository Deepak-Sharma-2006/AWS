---
name: pdf-document-intelligence
description: >-
  Systematic ingestion, parsing, and requirements extraction from PDF specifications, whitepapers,
  slide decks, and product requirement documents. Use this skill when a coding task, hackathon problem,
  or product architecture is defined in PDF files.
metadata:
  origin: Antigravity-Governance
---

# PDF Document Intelligence — Product Spec & Problem Statement Extraction

> **Trigger**: Run whenever a task references a `.pdf` file (e.g., product specification, hackathon brief, architecture deck, academic whitepaper, or API RFC).
> **Principle**: *"Zero hallucinated citations; verify every requirement against page, section, and diagram."*

---

## 1. The PDF Challenge in Agentic Coding

PDFs are binary, multi-modal documents containing complex formatting, multi-column text, embedded schemas, tables, and architectural diagrams. Naive AI agents often:
1. **Hallucinate Content**: Assume details from document titles without reading inner pages.
2. **Exhaust Context**: Dump thousands of raw token pages into the prompt at once.
3. **Miss Structural Nuances**: Overlook footnotes, callout boxes, table cell constraints, and sequence diagrams.

The **PDF Document Intelligence** skill enforces a disciplined, token-bounded, grounded extraction protocol.

---

## 2. Ingestion & Inspection Workflow

```
+-------------------------------------------------------------------------------+
|                    PDF DOCUMENT INTELLIGENCE PIPELINE                         |
+-------------------------------------------------------------------------------+
| 1. METADATA PROBE        | Inspect page count, layout, TOC, and chapters      |
| 2. TARGETED EXTRACTION   | Read bounded page ranges (view_file / CLI helpers) |
| 3. SCHEMA & FLOW PARSING | Parse tables, data contracts, and diagrams         |
| 4. GROUNDED SPEC MATRIX  | Generate cited engineering requirements & delta    |
+-------------------------------------------------------------------------------+
```

### Step 1: Metadata & Structure Probe
Before reading pages in bulk:
1. Identify the file location and size.
2. Inspect the Table of Contents (TOC), executive summary, or architecture overview to map out relevant page numbers.
3. Determine if the PDF is text-native (searchable) or scanned (requires OCR).

### Step 2: Targeted Page-Bounded Reading
Never attempt to ingest an entire 50-page PDF into prompt memory.
- Use `view_file` on the PDF path with bounded page or byte offsets.
- When extracting text via shell tools (e.g., `pdftotext`, `python -m pypdf`, or Node scripts), extract only the target sections:
  ```bash
  # Extract specific page slice without context bloat
  node -e "const fs = require('fs'); ... "
  ```

### Step 3: Multi-Modal Extraction Hierarchy
When analyzing a PDF for a software product, extract four distinct layers:

1. **The Core Problem Statement & User Personas**:
   - What pain point does the document state?
   - What user roles or system actors are defined?
2. **Domain Entities & Data Schemas**:
   - Extract tables, JSON schemas, entity-relationship diagrams, and state transitions.
   - Note exact field names, data types, nullability, and primary/foreign keys.
3. **API & Interface Specifications**:
   - Endpoints, methods (`GET`, `POST`, `PUT`, `DELETE`), headers, error codes.
   - Rate limits, authentication requirements, and payload examples.
4. **Architectural & Security Invariants**:
   - Latency thresholds (e.g., *"Responses under 200ms"*).
   - Security constraints (e.g., *"All passwords salted and hashed with Argon2id"*).
   - Compliance mandates (e.g., SOC2, GDPR, HIPAA, zero ghost dependencies).

### Step 4: Workspace Delta Analysis
Compare the extracted PDF requirements against the active codebase:
- **Implemented**: Features already present and verified by tests.
- **Partially Implemented**: Features existing in code but missing PDF-specified edge cases.
- **Missing / Unbuilt**: Requirements in the PDF that have zero implementation in the workspace.

---

## 3. Standard PDF Extraction Report (`PDF-SPEC-AUDIT.md`)

```markdown
# PDF Specification Audit: [Document Title]

- **Source Document**: `[spec.pdf](file:///path/to/spec.pdf)`
- **Analyzed Sections**: Pages X through Y
- **Target Domain**: [Auth / Core / Billing / Ingestion]

## 1. Grounded Requirements Matrix
| Requirement ID | PDF Citation | Requirement Description | Active Code Status | Test Contract |
| :--- | :--- | :--- | :--- | :--- |
| **REQ-01** | Page 4, §2.1 | SHA-256 session token hashing | 🟢 Implemented | `tests/auth.test.ts` |
| **REQ-02** | Page 7, Table 2 | Rate limit: 60 req/min per IP | 🔴 Missing | Pending |

## 2. Identified Data Contracts
```typescript
interface DocumentEntity {
  id: string; // Page 8, §3.2
  title: string;
  status: "draft" | "active" | "archived";
}
```

## 3. Ambiguities & Discrepancies
- *Discrepancy 1*: Page 5 specifies 30-day session TTL, but Table 3 indicates 7-day TTL.
  - *Recommendation*: Use `grill-me` to confirm human intent.
```

---

## 4. Operational Invariants

1. **Strict Citation Grounding**: Every extracted requirement must cite the specific page or section number.
2. **Anti-Hallucination Guard**: If a page is blurry, corrupted, or unreadable, explicitly flag: `"INSUFFICIENT CONTEXT DETECTED: Unable to extract text from page X."` Never guess missing parameters.
3. **Progressive Token Economy**: Offload extracted schemas and summaries into the Memory Vault (`.agents/memory/project/facts/`) to preserve prompt context.
