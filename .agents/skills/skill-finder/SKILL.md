---
name: skill-finder
description: >-
  Searches, inspects, and registers specialized skills on-demand without context window bloat.
  Use this skill when the current task requires specialized tooling, third-party runbooks, or when
  evaluating whether an optimal skill already exists in the workspace.
metadata:
  origin: Antigravity-Governance
---

# Dynamic Skill Finder & On-Demand Registry

> **Core Directives**: Progressive disclosure, zero context window bloat, instant retrieval across 296+ skills.
> **Principle**: *"Never dump 300 skills into the prompt context; discover dynamically, view bounded slices, execute with precision."*

---

## 1. Architecture & Capabilities

The **Skill Finder** manages the hybrid library of 296+ skills (combining Antigravity governance foundations with the full ECC domain catalog). It uses a local SQLite index (`.agents/state/skills-cache.sqlite`) for sub-millisecond retrieval across descriptions, triggers, and tags.

### Curated Skill Domains (10 Categories)
1. **⭐ Core Governance**: `agentic-loop-runner`, `claude-council`, `code-reading-dossier`, `git-sync-lock`, `grill-me`, `skill-finder`, `styx-pentest`, `token-budget-guard`.
2. **🎯 Product Discovery & Alignment**: `grill-me`, `problem-statement-deconstructor`, `pdf-document-intelligence`, `product-lens`, `product-capability`, `intent-driven-development`.
3. **🎨 Frontend & Design**: `design-system`, `motion-ui`, `frontend-patterns`, `react-patterns`, `vue-patterns`.
4. **⚙️ Backend & Persistence**: `backend-patterns`, `postgres-patterns`, `redis-patterns`, `mysql-patterns`, `api-design`.
5. **🛡️ Security & Pentesting**: `styx-pentest`, `security-review`, `security-scan`, `django-security`, `laravel-security`.
6. **🤖 AI & Machine Learning**: `eval-harness`, `mle-workflow`, `deep-research`, `iterative-retrieval`, `cost-aware-llm-pipeline`.
7. **🚀 DevOps & Cloud Infrastructure**: `deployment-patterns`, `docker-patterns`, `kubernetes-patterns`, `uncloud`, `canary-watch`.
8. **💻 Systems & Languages**: `golang-patterns`, `rust-patterns`, `python-patterns`, `swiftui-patterns`, `kotlin-patterns`.
9. **🧪 Quality & Architecture**: `tdd-workflow`, `e2e-testing`, `browser-qa`, `verification-loop`, `coding-standards`.
10. **🌐 General Utilities**: `terminal-ops`, `email-ops`, `brand-voice`, `content-engine`.

---

## 2. Fast CLI Commands

- **List All Installed Skills by Domain**:
  ```bash
  npm run skill:list
  ```

- **Search Skills by Keyword & Domain**:
  ```bash
  npm run skill:search -- --query <keyword>
  npm run skill:search -- --query "auth" --category "security"
  ```

- **Inspect Skill Manual Without Context Bloat**:
  ```bash
  npm run skill:view -- --name <skill-name>
  ```

- **Scaffold a New Specialized Skill**:
  ```bash
  npm run skill:new -- <skill-name> "Clear description of trigger conditions and patterns"
  ```

---

## 3. High-Leverage Skill Workflows

| Phase | Primary Skills | Synergy |
| :--- | :--- | :--- |
| **1. Requirements & Discovery** | `grill-me` + `problem-statement-deconstructor` + `pdf-document-intelligence` | Interrogates prompt, deconstructs PDF specs, and establishes immutable intent contracts before coding. |
| **2. Architectural Design** | `product-capability` + `claude-council` + `design-system` | Multi-perspective architecture consensus and component tokenization. |
| **3. Implementation Loop** | `agentic-loop-runner` + `tdd-workflow` + `git-sync-lock` | 4-part self-correcting feedback loop with distributed lease safety. |
| **4. Verification & Release** | `audit:beta` + `styx-pentest` + `cleanproduction:publish` | 5-layer adversarial certification and public showcase synchronization. |
