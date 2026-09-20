# Rule: Token Economy & Cost Reduction

## Purpose
Minimizes LLM prompt token consumption, prevents context bloat, and enforces strict execution time and dollar cost ceilings for all autonomous loops.

## Operational Directives

### 1. Progressive Disclosure First
- Do NOT inject bulky design guides, API documentation, or source dumps into prompt contexts.
- Use modular skill files (`SKILL.md`) that contain only high-level instructions and point to sub-references loaded on demand.

### 2. Slice-Targeted Reading
- Never use full-file views on source files larger than 150 lines.
- Always use `grep_search` to identify exact line ranges, then call `view_file` specifying `StartLine` and `EndLine` with narrow spans ($<100$ lines).

### 3. Transcript Compression
- When reading past conversation history, use `transcript.jsonl` (compact summaries) rather than `transcript_full.jsonl`.

### 4. Hard Execution Ceilings
- **Max Correction Loops**: 5 iterations per task. If an issue is unresolved after 5 loops, halt immediately.
- **Task Timeout**: 300 seconds (5 minutes) maximum execution duration.
- **Token Ceiling**: 250,000 tokens per feature phase. If a session approaches 200,000 tokens, trigger a context compaction warning.
