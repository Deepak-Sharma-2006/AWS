import { execSync } from "child_process";
import { existsSync, mkdirSync, readFileSync, readdirSync, writeFileSync } from "fs";
import { join } from "path";

const DOSSIERS_DIR = join(process.cwd(), "docs/dossiers");
const STATE_DIR = join(process.cwd(), ".agents/state");
const ROLE_FILE = join(STATE_DIR, "active-role.json");

function getActiveRole() {
  if (existsSync(ROLE_FILE)) {
    try {
      const data = JSON.parse(readFileSync(ROLE_FILE, "utf-8"));
      return {
        operator: data.operator || data.currentOperator || "Computer1",
        role: data.role || data.activeRole || "Alpha",
        phase: data.phase ?? data.currentPhase ?? 1,
        activeLeaseDomain: data.activeLeaseDomain || data.activeDomain || "core",
      };
    } catch {
      // Fallback
    }
  }
  return { operator: "Computer1", role: "Alpha", phase: 1, activeLeaseDomain: "core" };
}

export function scaffoldPhaseDossier(phaseNumber: number, domain: string): string {
  if (!existsSync(DOSSIERS_DIR)) {
    mkdirSync(DOSSIERS_DIR, { recursive: true });
  }

  const dossierPath = join(DOSSIERS_DIR, `phase-${phaseNumber}-${domain}.md`);
  if (existsSync(dossierPath)) {
    console.log(`ℹ️ Existing Phase Dossier found: docs/dossiers/phase-${phaseNumber}-${domain}.md`);
    return dossierPath;
  }

  const template = `# Phase ${phaseNumber} Cognitive Comprehension & Operator Verification Dossier
**Domain**: \`${domain}\` | **Author**: \`Computer 1 (Alpha)\` | **Auditor**: \`Computer 2 (Beta)\`

---

## 1. Executive Summary & 1-Sentence Feynman Compression (Technique 6)
> **1-Sentence Mental Model**:
> *"Write a concise 1-sentence plain language summary describing what this component achieves."*

---

## 2. Component & Symbol Inventory
- \`src/${domain}/...\`: Core business logic and controllers.
- \`tests/${domain}/...\`: Unit and contract test specifications.

---

## 3. Entry Point & Call Graph Map (Technique 1)
\`\`\`mermaid
flowchart TD
    Client[Caller / Request] --> EntryPoint[src/${domain}/index.ts]
    EntryPoint --> Service[Core Domain Service]
    Service --> Storage[Data Layer / Database]
\`\`\`

---

## 4. Contract-First Test Specifications (Technique 2)
- Unit tests verifying deterministic inputs and outputs in \`tests/\`.
- Run command: \`npm test\`

---

## 5. Domain Data Lifecycle & Entity Journeys (Technique 3)
\`\`\`
[Input Payload] ──▶ [Validation] ──▶ [Transformation] ──▶ [Storage/Egress]
\`\`\`

---

## 6. Cognitive Gate Mask: Skipped vs. Core Logic (Technique 4)
- **Core Business Logic (Must Read First)**: Core mathematical / domain logic in \`src/\`.
- **Non-Blocking Noise (Skip on Pass 1)**: Telemetry, debug loggers, metric counters.

---

## 7. Adversarial Failure Path & Security Audit (Technique 5)
- **Timing Attack Resistance**: Critical string/token checks use \`crypto.timingSafeEqual\`.
- **Account Enumeration Defense**: Uniform error handling for authentication failures.
- **Input Sanitization**: Strict parameter parsing with zero unvalidated assumptions.

---

## 8. Operator Sign-Off & Verification Rubric
- [ ] TypeScript compiles cleanly (\`strict: true\`)
- [ ] Unit tests pass 100% with exit code 0
- [ ] Zero ghost packages detected (\`npm run check:hallucinations\`)
- [ ] Styx DAST red-team tests pass (\`npm run pentest\`)
`;

  writeFileSync(dossierPath, template, "utf-8");
  console.log(`📝 [Dossier Scaffolded] Created: docs/dossiers/phase-${phaseNumber}-${domain}.md`);
  return dossierPath;
}

export function runAlphaSuite(): boolean {
  console.log(`\n⚡ [ALPHA BUILDER SUITE] Initiating Alpha Pre-Flight & Build Pipeline...`);
  console.log(`================================================================================`);

  const role = getActiveRole();
  console.log(`Operator: ${role.operator} | Role: ${role.role} | Phase: ${role.phase} | Domain: ${role.activeLeaseDomain}\n`);

  let allPassed = true;

  // 1. Zero-Secret Shield
  console.log(`▶ [1/6] Scanning for Hardcoded Secrets (Zero-Secret Shield)...`);
  try {
    execSync("node --experimental-strip-types scripts/secret-scanner.ts", { stdio: "inherit" });
    console.log(`✅ Zero-Secret Shield: PASSED`);
  } catch {
    console.error(`❌ Zero-Secret Shield: FAILED`);
    allPassed = false;
  }

  // 2. Ghost Package Scanner
  console.log(`\n▶ [2/6] Checking Ghost Dependencies (Anti-Hallucination Shield)...`);
  try {
    execSync("node --experimental-strip-types scripts/anti-hallucination-checker.ts scripts src tests", { stdio: "inherit" });
    console.log(`✅ Anti-Hallucination Shield: PASSED`);
  } catch {
    console.error(`❌ Anti-Hallucination Shield: FAILED`);
    allPassed = false;
  }

  // 3. Strict TypeScript Compilation
  console.log(`\n▶ [3/6] Compiling TypeScript (Strict Mode)...`);
  try {
    execSync("npx tsc --noEmit", { stdio: "inherit" });
    console.log(`✅ TypeScript Compilation: PASSED (0 Errors)`);
  } catch {
    console.error(`❌ TypeScript Compilation: FAILED`);
    allPassed = false;
  }

  // 4. Unit Test & Behavioral Contract Execution
  console.log(`\n▶ [4/6] Running Unit Tests & Behavioral Harness...`);
  try {
    execSync("npm test", { stdio: "inherit" });
    console.log(`✅ Test & Behavioral Harness: PASSED`);
  } catch {
    console.error(`❌ Test & Behavioral Harness: FAILED`);
    allPassed = false;
  }

  // 5. Scaffold / Verify Phase Cognitive Dossier
  console.log(`\n▶ [5/6] Verifying / Scaffolding Phase Comprehension Dossier...`);
  scaffoldPhaseDossier(role.phase, role.activeLeaseDomain);

  // 6. Token Economy Check
  console.log(`\n▶ [6/6] Checking Token Economy & Budget Ceilings...`);
  try {
    execSync("node --experimental-strip-types scripts/token-budget-guard.ts", { stdio: "inherit" });
    console.log(`✅ Token Budget: WITHIN LIMITS`);
  } catch {
    console.warn(`⚠️ Token budget monitor warning.`);
  }

  console.log(`\n================================================================================`);
  if (allPassed) {
    console.log(`🎉 [ALPHA BUILD SUITE COMPLETE] Domain implementation & contracts ready!`);
    console.log(`Next Action: Run 'npm run role:handoff' to transfer lease to Lead 2 (Adversarial Systems & Product Lead).`);
    return true;
  } else {
    console.error(`🚨 [ALPHA BUILD FAILED] Resolve compilation or test errors before handoff.`);
    return false;
  }
}

import { fileURLToPath } from "node:url";

const isMain = process.argv[1] && (
  fileURLToPath(import.meta.url) === process.argv[1] ||
  process.argv[1].endsWith("alpha-builder-runner.ts") ||
  process.argv[1].endsWith("alpha-builder-runner.js")
);

if (isMain) {
  const ok = runAlphaSuite();
  process.exit(ok ? 0 : 1);
}
