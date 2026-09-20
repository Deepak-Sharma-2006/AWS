import { existsSync, mkdirSync, readFileSync, writeFileSync } from "fs";
import { join } from "path";
import { execSync } from "child_process";
import { fileURLToPath } from "node:url";
import { acquireLock, listLocks, releaseLock, resolveOperator, transferLock } from "./lock-manager.ts";
import { saveMemory } from "./memory-vault.ts";

export interface ActiveRoleProfile {
  operator: string;
  role: "Alpha" | "Beta";
  roleTitle: string;
  phase: number;
  activeLeaseDomain: string;
  updatedAt: string;
}

const STATE_DIR = join(process.cwd(), ".agents/state");
const ROLE_FILE = join(STATE_DIR, "active-role.json");

function getRoleTitle(role: "Alpha" | "Beta"): string {
  return role === "Alpha"
    ? "Feature Architect & Core Domain Lead"
    : "Adversarial Systems, SDET & Product Lead";
}

function execGit(cmd: string): string {
  try {
    return execSync(cmd, { encoding: "utf-8" }).trim();
  } catch (err: any) {
    return "";
  }
}

export function getActiveProfile(): ActiveRoleProfile {
  if (!existsSync(STATE_DIR)) {
    mkdirSync(STATE_DIR, { recursive: true });
  }

  if (existsSync(ROLE_FILE)) {
    try {
      const parsed: ActiveRoleProfile = JSON.parse(readFileSync(ROLE_FILE, "utf-8"));
      if (!parsed.roleTitle) {
        parsed.roleTitle = getRoleTitle(parsed.role);
      }
      return parsed;
    } catch {
      // Fall through to default
    }
  }

  const role: "Alpha" | "Beta" = (process.env.ROLE as "Alpha" | "Beta") || "Alpha";
  const defaultProfile: ActiveRoleProfile = {
    operator: resolveOperator(),
    role,
    roleTitle: getRoleTitle(role),
    phase: parseInt(process.env.PHASE || "1", 10),
    activeLeaseDomain: "core",
    updatedAt: new Date().toISOString(),
  };

  saveProfile(defaultProfile);
  return defaultProfile;
}

export function saveProfile(profile: ActiveRoleProfile): void {
  if (!existsSync(STATE_DIR)) {
    mkdirSync(STATE_DIR, { recursive: true });
  }
  profile.roleTitle = getRoleTitle(profile.role);
  profile.updatedAt = new Date().toISOString();
  writeFileSync(ROLE_FILE, JSON.stringify(profile, null, 2), "utf-8");
}

export function printRoleMatrix(): void {
  console.log(`
================================================================================
     ENTERPRISE 2-PERSON DUAL-LEAD DIVISION OF LABOR (50/50 WORKLOAD)
================================================================================

┌──────────────────────────────────────────────────────────────────────────────┐
│ LEAD 1: FEATURE ARCHITECT & CORE DOMAIN LEAD (Alpha) - 50% Workload          │
├──────────────────────────────────────────────────────────────────────────────┤
│ 1. Schema & Contract Definitions  : Zod schemas, TypeScript domain models    │
│ 2. Core Business Engine           : Domain logic, transaction pipelines      │
│ 3. White-Box Unit Contracts       : Happy-path & expected exceptions TDD     │
│ 4. Mental Model & Visual Trace    : Entry point diagrams, data lifecycle     │
│ 5. Primary Domain Write Lease     : Exclusive lease on 'core' domain         │
└──────────────────────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────────────────────┐
│ LEAD 2: ADVERSARIAL SYSTEMS, SDET & PRODUCT LEAD (Beta) - 50% Workload       │
├──────────────────────────────────────────────────────────────────────────────┤
│ 1. Independent Black-Box SDET     : Writes 'tests/adversarial/*.test.ts'     │
│ 2. Concurrency & Race Fuzzing     : 10+ parallel worker contention probes    │
│ 3. Boundary & Malicious Injection : Path traversal, SQLi, XSS, fuzzing       │
│ 4. AppSec & Privilege Escalation  : Strix dynamic DAST, constant-time crypto │
│ 5. Product & UX Acceptance        : End-to-end user journeys, error handling │
│ 6. Hardening Commits & Patching   : Authorized to directly fix & harden src/ │
│ 7. Production Release SRE         : CleanProduction sync, rollback readiness │
└──────────────────────────────────────────────────────────────────────────────┘

* Both leads hold equal weight. Roles invert automatically each feature phase.
================================================================================`);
}

export function printRoleStatus(): void {
  const profile = getActiveProfile();
  const currentHost = resolveOperator();

  console.log(`
================================================================================
               ACTIVE WORKSPACE ROLE & LEASE PROFILE
================================================================================
  Current Workstation   : ${currentHost}
  Active Profile Leader : ${profile.operator}
  Assigned Role         : ${profile.role} (${profile.roleTitle})
  Current Phase         : Phase ${profile.phase}
  Active Domain Lease   : ${profile.activeLeaseDomain}
  Last Synchronized     : ${profile.updatedAt}
================================================================================`);

  console.log("\nActive Domain Locks in Repository:");
  listLocks();
  console.log("");
}

export function switchToAlpha(domain = "core", operator?: string): boolean {
  const profile = getActiveProfile();
  const currentOp = resolveOperator(operator);
  console.log(`\n⚙️ [Role Switch] Switching ${currentOp} to ALPHA (Feature Architect & Core Domain Lead) for '${domain}'...`);

  const ok = acquireLock(domain, currentOp, "Alpha", 7200);
  if (ok) {
    profile.operator = currentOp;
    profile.role = "Alpha";
    profile.roleTitle = getRoleTitle("Alpha");
    profile.activeLeaseDomain = domain;
    saveProfile(profile);
    console.log(`✅ [Role Confirmed] ${currentOp} is now ALPHA (Core Domain Lead) for Phase ${profile.phase}.\n`);
  }
  return ok;
}

export function switchToBeta(domain = "core", operator?: string): boolean {
  const profile = getActiveProfile();
  const currentOp = resolveOperator(operator);
  console.log(`\n⚙️ [Role Switch] Configuring ${currentOp} as BETA (Adversarial Systems, SDET & Product Lead) for Phase ${profile.phase}...`);

  const ok = acquireLock(domain, currentOp, "Beta", 7200);
  if (ok) {
    profile.operator = currentOp;
    profile.role = "Beta";
    profile.roleTitle = getRoleTitle("Beta");
    profile.activeLeaseDomain = domain;
    saveProfile(profile);
    console.log(`✅ [Role Confirmed] ${currentOp} is now BETA (Adversarial Systems Lead) for Phase ${profile.phase}.\n`);
  }
  return ok;
}

export function executeRoleHandoff(toOperator?: string, customNotes?: string): boolean {
  const profile = getActiveProfile();
  const currentOp = profile.operator;
  const targetOp = resolveOperator(toOperator || (currentOp === "Computer1" ? "Computer2" : "Computer1"));

  console.log(`\n🔄 [Enterprise Handoff] Initiating atomic role handoff from ${currentOp} (${profile.role}) to ${targetOp}...`);

  // Step 1: Pre-Commit Secret Scanner Check
  console.log("🔒 [Zero-Secret Gate] Verifying clean workspace before handoff...");
  try {
    execSync("node --experimental-strip-types scripts/secret-scanner.ts", { stdio: "inherit" });
  } catch {
    console.error("🛑 [HANDOFF ABORTED] Secret detected in workspace! Purge secrets before handoff.");
    return false;
  }

  // Step 2: Check git status
  const status = execGit("git status -s");
  if (status) {
    console.log("📦 Staging and committing modified workspace state for handoff...");
    try {
      execSync("git add -A", { stdio: "inherit" });
      execSync(`git commit -m "chore(handoff): Phase ${profile.phase} handoff from ${currentOp} to ${targetOp}"`, { stdio: "inherit" });
    } catch {
      console.warn("⚠️ Git commit encountered no changes or skipped.");
    }
  }

  // Step 3: Transfer lease lock
  if (profile.role === "Alpha") {
    // Alpha completed domain development -> handoff to Beta for Adversarial SDET, Chaos, and 6-Pillar Audit
    const ok = transferLock(profile.activeLeaseDomain, currentOp, targetOp, "Beta");
    if (ok) {
      profile.role = "Beta";
      profile.roleTitle = getRoleTitle("Beta");
      saveProfile(profile);

      // Record in memory vault
      saveMemory({
        title: `Phase ${profile.phase} Handoff: Alpha -> Beta`,
        kind: "handoff",
        scope: "team",
        phase: profile.phase,
        operator: currentOp,
        body: customNotes || `Phase ${profile.phase} core implementation complete for domain '${profile.activeLeaseDomain}'. Transferred to ${targetOp} for independent adversarial testing, fuzzing, AppSec, and 6-pillar enterprise certification.`,
      });

      // Push state
      console.log("🚀 Synchronizing handoff state to origin...");
      try {
        execSync("git push origin main", { stdio: "inherit" });
      } catch {
        console.warn("⚠️ Git push failed or remote unreachable. Push manually before partner continues.");
      }

      console.log(`\n================================================================================`);
      console.log(`✅ [HANDOFF COMPLETE] Domain '${profile.activeLeaseDomain}' transferred to ${targetOp} (Lead 2 / Beta).`);
      console.log(`👉 Partner Actions for ${targetOp} (Adversarial Systems & Product Lead):`);
      console.log(`   1. git pull`);
      console.log(`   2. npm run test:adversarial`);
      console.log(`   3. npm run audit:beta`);
      console.log(`================================================================================\n`);
      return true;
    }
    return false;
  } else {
    // Beta completed 6-pillar audit & approved -> advance phase and invert roles!
    releaseLock(profile.activeLeaseDomain, currentOp);
    profile.phase += 1;
    profile.role = "Alpha";
    profile.roleTitle = getRoleTitle("Alpha");
    profile.operator = targetOp;
    saveProfile(profile);

    saveMemory({
      title: `Phase ${profile.phase - 1} Certified & Phase ${profile.phase} Inversion`,
      kind: "decision",
      scope: "team",
      phase: profile.phase - 1,
      operator: currentOp,
      body: `Phase ${profile.phase - 1} passed 6-pillar enterprise verification. Roles inverted for Phase ${profile.phase}. ${profile.operator} is now Alpha (Feature Architect & Core Domain Lead).`,
    });

    console.log("🚀 Synchronizing phase inversion state to origin...");
    try {
      execSync("git add .agents/state/active-role.json .agents/state/locks/", { stdio: "inherit" });
      execSync(`git commit -m "chore(role): Phase ${profile.phase} start - ${profile.operator} assumed Alpha"`, { stdio: "inherit" });
      execSync("git push origin main", { stdio: "inherit" });
    } catch {
      // Ignored if clean
    }

    console.log(`\n================================================================================`);
    console.log(`🎉 [PHASE ADVANCED] Phase ${profile.phase - 1} certified and merged!`);
    console.log(`🚀 [ROLE INVERSION] ${profile.operator} is now ALPHA for Phase ${profile.phase}.`);
    console.log(`👉 Partner Command for ${profile.operator} (Core Domain Lead):`);
    console.log(`   git pull && npm run build:alpha`);
    console.log(`================================================================================\n`);
    return true;
  }
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
  process.argv[1].endsWith("role-switch.ts") ||
  process.argv[1].endsWith("role-switch.js")
);

if (isMain) {
  const rawArgs = process.argv.slice(2);
  const command = (rawArgs[0] && !rawArgs[0].startsWith("--") ? rawArgs[0] : "status").toLowerCase();
  const flags = parseCliFlags(rawArgs);
  const positional = rawArgs.filter((a) => !a.startsWith("--") && a !== command);

  if (command === "status") {
    printRoleStatus();
  } else if (command === "matrix") {
    printRoleMatrix();
  } else if (command === "alpha") {
    const domain = flags["domain"] || positional[0] || "core";
    const op = flags["operator"] || flags["op"] || positional[1];
    switchToAlpha(domain, op);
  } else if (command === "beta") {
    const domain = flags["domain"] || positional[0] || "core";
    const op = flags["operator"] || flags["op"] || positional[1];
    switchToBeta(domain, op);
  } else if (command === "handoff") {
    const toOp = flags["to"] || flags["target"] || positional[0];
    const notes = flags["notes"] || flags["msg"] || positional.slice(1).join(" ");
    executeRoleHandoff(toOp, notes);
  } else {
    console.log(`
Usage: node --experimental-strip-types scripts/role-switch.ts <command> [options]

Commands:
  status               Display active operator, role title, phase, and domain lease
  matrix               Display the enterprise 50/50 division of labor matrix
  alpha [domain] [op]  Acquire domain lease and set workstation as Lead 1 (Alpha)
  beta [domain] [op]   Configure workstation as Lead 2 (Beta) with Hardening Authority
  handoff [toOp] [msg] Execute atomic git-synchronized role handoff to partner
`);
  }
}
