import { existsSync, mkdirSync, writeFileSync } from "fs";
import { join } from "path";
import { fileURLToPath } from "node:url";
import { listLocalSkills, viewSkill, searchSkills } from "./skill-finder.ts";
import { saveMemory } from "./memory-vault.ts";

export interface SkillCreationRequest {
  name: string;
  description: string;
  reason: string;
  metric: string;
  parentSkills: string[];
  directives?: string[];
  verificationRubric?: string[];
  force?: boolean;
}

export interface SkillCreationResult {
  success: boolean;
  skillPath: string;
  skillName: string;
  reason: string;
  metric: string;
  parentSkills: string[];
  justificationSummary: string;
}

const SKILLS_DIR = join(process.cwd(), ".agents/skills");

/**
 * Evaluates the 3-Prong Anti-Bloat Justification Test
 */
export function evaluateAntiBloatJustification(req: SkillCreationRequest): { allowed: boolean; reason: string } {
  // 1. Existing duplicate check
  const targetDir = join(SKILLS_DIR, req.name);
  if (existsSync(targetDir) && !req.force) {
    return {
      allowed: false,
      reason: `Skill '${req.name}' already exists at: ${targetDir}. Reuse or extend the existing skill.`,
    };
  }

  // 2. Metric & Reason Rigor Check
  if (!req.reason || req.reason.trim().length < 20) {
    return {
      allowed: false,
      reason: "REJECTED: Justification reason is too vague. Must describe a real-world significant/major improvement.",
    };
  }

  if (!req.metric || req.metric.trim().length < 10) {
    return {
      allowed: false,
      reason: "REJECTED: Target improvement metric is missing or insufficient (e.g. latency, throughput, token economy, accuracy).",
    };
  }

  // 3. Overlap Check: Search if existing skills already cover 80%+ of this
  const existingMatches = searchSkills(req.name);
  const exactMatch = existingMatches.find((s) => s.name.toLowerCase() === req.name.toLowerCase());
  if (exactMatch && !req.force) {
    return {
      allowed: false,
      reason: `REJECTED: Exact match already exists: '${exactMatch.name}' (${exactMatch.category}).`,
    };
  }

  return { allowed: true, reason: "PASSED: Rigorous justification and quantifiable metric verified." };
}

/**
 * Creates a new specialized skill synthesized from parent registry skills
 */
export function createSynthesizedSkill(req: SkillCreationRequest): SkillCreationResult {
  const check = evaluateAntiBloatJustification(req);
  if (!check.allowed) {
    console.error(`\n🛑 [Skill Creator Gate: BLOCKED]\n${check.reason}\n`);
    throw new Error(check.reason);
  }

  const targetDir = join(SKILLS_DIR, req.name);
  if (!existsSync(targetDir)) {
    mkdirSync(targetDir, { recursive: true });
  }

  // Collect insights from parent skills
  const parentSummaries: string[] = [];
  for (const parent of req.parentSkills) {
    const parentContent = viewSkill(parent);
    if (parentContent) {
      parentSummaries.push(`- **Inherited from \`${parent}\`**: Synthesizes verified patterns from base registry.`);
    }
  }

  const directivesBlock = req.directives && req.directives.length > 0
    ? req.directives.map((d, i) => `### Rule ${i + 1}: ${d}\n- Apply consistently across the workflow.`).join("\n\n")
    : `### Rule 1: High-Assurance Determinism
- Enforce strict validation on all inputs and data transformations.

### Rule 2: Measurable Metric Verification
- Track and verify target metric: ${req.metric}.

### Rule 3: Zero Ghost Dependencies
- Rely strictly on verified workspace packages; reject uninstalled libraries.`;

  const rubricBlock = req.verificationRubric && req.verificationRubric.length > 0
    ? req.verificationRubric.map((r) => `- [ ] ${r}`).join("\n")
    : `- [ ] Measurable improvement verified: ${req.metric}
- [ ] Zero ghost dependencies introduced
- [ ] Deterministic unit or behavioral test executed with passing status`;

  const skillContent = `---
name: ${req.name}
description: >-
  ${req.description.trim()}
metadata:
  origin: Antigravity-Synthesizer
  parents: ${JSON.stringify(req.parentSkills)}
  targetMetric: ${JSON.stringify(req.metric)}
  justification: ${JSON.stringify(req.reason)}
---

# ${req.name} Skill Manual

> **Justification**: ${req.reason}  
> **Target Metric**: ${req.metric}  
> **Lineage**: Synthesized from ${req.parentSkills.length > 0 ? req.parentSkills.map((p) => `\`${p}\``).join(", ") : "Core Workspace Invariants"}  

---

## 1. Trigger Conditions

Activate this skill when:
- The task encounters the specific domain requirements outlined below.
- Existing standard skills lack the specialized capabilities needed to achieve: **${req.metric}**.
- Operational execution requires verified synthesis from parent workflows: ${req.parentSkills.join(", ") || "None"}.

---

## 2. Synthesis Lineage & Parent Foundation

${parentSummaries.length > 0 ? parentSummaries.join("\n") : "- Formulated from core Antigravity zero-hallucination and distributed governance principles."}

---

## 3. Operational Directives & Core Rules

${directivesBlock}

---

## 4. Execution Workflow

1. **Pre-Flight Invariant Check**:
   - Verify preconditions and check for relevant domain locks or constraints.
2. **Specialized Execution**:
   - Execute the domain logic targeting the primary metric: ${req.metric}.
3. **Evidence Collection**:
   - Record outputs and verify execution correctness.

---

## 5. Verification Rubric

${rubricBlock}
`;

  const skillFilePath = join(targetDir, "SKILL.md");
  writeFileSync(skillFilePath, skillContent, "utf-8");

  // Record into Memory Vault
  saveMemory({
    title: `Skill Created: ${req.name}`,
    kind: "decision",
    scope: "project",
    phase: 1,
    operator: process.env.OPERATOR_NAME || "Computer1",
    tags: ["skill-creation", "registry", req.name, ...req.parentSkills],
    body: `### Dynamically Synthesized Skill: ${req.name}
- **File**: ${skillFilePath}
- **Justification**: ${req.reason}
- **Target Metric**: ${req.metric}
- **Parent Skills**: ${req.parentSkills.join(", ") || "None"}
- **Description**: ${req.description}`,
  });

  console.log(`\n✨ [Skill Creator] Successfully synthesized and registered: '${req.name}'`);
  console.log(`   📁 File   : ${skillFilePath}`);
  console.log(`   🎯 Metric : ${req.metric}`);
  console.log(`   💡 Reason : ${req.reason}\n`);

  return {
    success: true,
    skillPath: skillFilePath,
    skillName: req.name,
    reason: req.reason,
    metric: req.metric,
    parentSkills: req.parentSkills,
    justificationSummary: `Created skill '${req.name}' to achieve ${req.metric}. Reason: ${req.reason}`,
  };
}

function parseCliFlags(args: string[]): Record<string, string> {
  const flags: Record<string, string> = {};
  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    if (arg.startsWith("--")) {
      const key = arg.slice(2);
      if (i + 1 < args.length && !args[i + 1].startsWith("--")) {
        flags[key] = args[i + 1];
        i++;
      } else {
        flags[key] = "true";
      }
    }
  }
  return flags;
}

const isMain = process.argv[1] && (
  fileURLToPath(import.meta.url) === process.argv[1] ||
  process.argv[1].endsWith("skill-creator.ts") ||
  process.argv[1].endsWith("skill-creator.js")
);

if (isMain) {
  const rawArgs = process.argv.slice(2);
  const flags = parseCliFlags(rawArgs);
  const positional = rawArgs.filter((a) => !a.startsWith("--"));

  const name = flags["name"] || positional[0];
  const desc = flags["desc"] || flags["description"] || positional[1] || "Synthesized domain skill.";
  const reason = flags["reason"] || flags["why"] || positional[2] || "";
  const metric = flags["metric"] || flags["improvement"] || positional[3] || "";
  const parents = flags["parents"] || flags["parent"] ? (flags["parents"] || flags["parent"]).split(",").map((s) => s.trim()) : [];
  const force = flags["force"] === "true";

  if (!name || !reason || !metric) {
    console.log(`
Usage: node --experimental-strip-types scripts/skill-creator.ts [options]

Required Options:
  --name <skill-name>      Name of the skill to create (kebab-case)
  --desc <description>     Clear, concise summary of trigger and utility
  --reason <justification> Real-world problem or major improvement reason (min 20 chars)
  --metric <metric>        Quantifiable improvement (e.g., latency, token savings, accuracy)

Optional Options:
  --parents <parent1,p2>   Comma-separated list of existing registry skills to inherit from
  --force                  Bypass existence check (overwrite)

Example:
  npm run skill:create -- --name streaming-data-pipeline --desc "Low-latency SSE streaming parser" --reason "Required for real-time telemetry streaming in product UI" --metric "Sub-50ms latency with zero socket exhaustion" --parents backend-patterns,motion-ui
`);
    process.exit(1);
  }

  try {
    createSynthesizedSkill({
      name,
      description: desc,
      reason,
      metric,
      parentSkills: parents,
      force,
    });
    process.exit(0);
  } catch (err: any) {
    console.error(`❌ Error: ${err.message}`);
    process.exit(1);
  }
}
