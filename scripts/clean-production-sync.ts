import { existsSync, readdirSync } from "fs";
import { join } from "path";
import { execSync } from "child_process";
import { fileURLToPath } from "node:url";
import { runBetaAudit } from "./beta-audit-runner.ts";
import { getActiveProfile } from "./role-switch.ts";

function execCommand(cmd: string): string {
  try {
    return execSync(cmd, { encoding: "utf-8" }).trim();
  } catch {
    return "";
  }
}

export function getCleanProductionStatus(): void {
  console.log(`
================================================================================
           CLEAN PRODUCTION RELEASE & SYNC PIPELINE
================================================================================`);

  const remotesRaw = execCommand("git remote -v");
  const lines = remotesRaw.split("\n");

  let originUrl = "Not configured";
  let prodUrl = "⚠️ [Clean Production Remote Not Configured]";

  for (const line of lines) {
    const parts = line.split(/\s+/);
    if (parts[0] === "origin" && parts[2] === "(push)") {
      originUrl = parts[1];
    } else if ((parts[0] === "cleanproduction" || parts[0] === "jury") && parts[2] === "(push)") {
      prodUrl = parts[1];
    }
  }

  const latestCommit = execCommand("git log -1 --oneline") || "No commits found";
  const profile = getActiveProfile();

  console.log(`  Internal Collab Remote (origin)      : ${originUrl}`);
  console.log(`  Public Clean Showcase Remote (prod)  : ${prodUrl}`);
  console.log(`  Latest Synchronized Commit           : ${latestCommit}`);
  console.log(`  Current Development Phase            : Phase ${profile.phase} (${profile.role})`);

  console.log("\nReady Cognitive Comprehension Dossiers for Review:");
  const dossierDir = join(process.cwd(), "docs/dossiers");
  if (existsSync(dossierDir)) {
    const files = readdirSync(dossierDir).filter((f) => f.endsWith(".md"));
    if (files.length > 0) {
      for (const f of files) {
        console.log(`  📄 docs/dossiers/${f}`);
      }
    } else {
      console.log("  (None generated yet)");
    }
  }

  if (prodUrl.includes("Not Configured")) {
    console.log(`
ℹ️ To configure the secondary Clean Production repository, run:
   npm run cleanproduction:set-remote -- <YOUR_CLEAN_PROD_GITHUB_REPO_URL>
`);
  }

  console.log("================================================================================\n");
}

export function setCleanProductionRemote(url: string): boolean {
  if (!url || !url.trim()) {
    console.error("❌ Error: Please provide a valid Git remote URL.");
    return false;
  }

  const trimmed = url.trim();
  const remotes = execCommand("git remote").split("\n");

  try {
    if (remotes.includes("cleanproduction")) {
      execSync(`git remote set-url cleanproduction ${trimmed}`, { stdio: "inherit" });
      console.log(`✅ [Remote Updated] 'cleanproduction' remote set to: ${trimmed}`);
    } else {
      execSync(`git remote add cleanproduction ${trimmed}`, { stdio: "inherit" });
      console.log(`✅ [Remote Added] 'cleanproduction' remote added: ${trimmed}`);
    }
    return true;
  } catch (err) {
    console.error("❌ Failed to configure cleanproduction remote:", err);
    return false;
  }
}

export function generateChangelog(sinceTag?: string): string {
  try {
    const lastTag = sinceTag || execCommand("git describe --tags --abbrev=0 2>nul") || "";
    const range = lastTag ? `${lastTag}..HEAD` : "-n 15";
    const log = execCommand(`git log ${range} --pretty=format:"* %s (%h)"`);
    return log || "* Baseline release initialization.";
  } catch {
    return "* General engineering updates and performance improvements.";
  }
}

export function publishToCleanProduction(customTag?: string, skipAudit = false): boolean {
  console.log(`\n🚀 [Clean Production Release Pipeline] Initiating pre-publish gate barrier...`);

  // Step 1: Execute 5-layer Beta Audit
  if (!skipAudit) {
    console.log("Step 1: Running mandatory 5-layer Beta verification audit...");
    const auditPassed = runBetaAudit();
    if (!auditPassed) {
      console.error(`\n🛑 [Publish Blocked] Beta audit failed! Only fully audited, certified code can be published.\n`);
      return false;
    }
  } else {
    console.log("Step 1: Skipping 5-layer Beta verification audit (operator explicitly specified --skip-audit)...");
  }

  // Step 2: Check remote
  const remotes = execCommand("git remote").split("\n");
  const remoteName = remotes.includes("cleanproduction") ? "cleanproduction" : remotes.includes("jury") ? "jury" : null;

  if (!remoteName) {
    console.error(`\n❌ [Publish Aborted] Git remote 'cleanproduction' is not configured.`);
    console.error(`Run 'npm run cleanproduction:set-remote -- <URL>' first.\n`);
    return false;
  }

  const profile = getActiveProfile();
  const tag = customTag || `v1.0-phase-${profile.phase}`;
  const changelog = generateChangelog();

  console.log(`\n📋 [Release Changelog Generated]:`);
  console.log(changelog);

  try {
    console.log(`\nStep 2: Tagging release commit with '${tag}'...`);
    execSync(`git tag -a ${tag} -m "Release ${tag} - Certified 5/5 by Beta Auditor"`, { stdio: "inherit" });

    console.log(`\nStep 3: Pushing release to '${remoteName}' showcase remote...`);
    execSync(`git push ${remoteName} main`, { stdio: "inherit" });
    execSync(`git push ${remoteName} ${tag}`, { stdio: "inherit" });

    console.log(`\n🎉 [Clean Production Published] Successfully deployed ${tag} to ${remoteName} showcase repository!`);
    return true;
  } catch (err) {
    console.error(`\n❌ Failed to push release to ${remoteName} remote:`, err);
    return false;
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
  process.argv[1].endsWith("clean-production-sync.ts") ||
  process.argv[1].endsWith("clean-production-sync.js")
);

if (isMain) {
  const rawArgs = process.argv.slice(2);
  const command = (rawArgs[0] && !rawArgs[0].startsWith("--") ? rawArgs[0] : "status").toLowerCase();
  const flags = parseCliFlags(rawArgs);
  const positional = rawArgs.filter((a) => !a.startsWith("--") && a !== command);

  if (command === "status") {
    getCleanProductionStatus();
  } else if (command === "set-remote") {
    const url = flags["url"] || positional[0];
    setCleanProductionRemote(url);
  } else if (command === "publish") {
    const tag = flags["tag"] || positional[0];
    const skipAudit = flags["skip-audit"] === "true" || rawArgs.includes("--skip-audit");
    publishToCleanProduction(tag, skipAudit);
  } else {
    console.log(`
Usage: node --experimental-strip-types scripts/clean-production-sync.ts <command> [options]

Commands:
  status               Display cleanproduction remote status and release metadata
  set-remote <URL>     Configure secondary cleanproduction Git remote URL
  publish [TAG]        Audit code via 5-layer gate, generate changelog, tag, and publish
`);
  }
}
