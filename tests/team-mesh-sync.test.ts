import test from "node:test";
import type { TestContext } from "node:test";
import assert from "node:assert/strict";
import { existsSync, unlinkSync, readFileSync } from "node:fs";
import { join } from "node:path";
import { acquireLock, releaseLock, listLocks, getOperatingMode } from "../scripts/lock-manager.ts";
import { setOperatingMode, getActiveProfile } from "../scripts/role-switch.ts";
import { syncAllHarnesses } from "../scripts/universal-harness-sync.ts";

test("N-Person Team Mesh & Universal Multi-Harness Test Suite", async (t: TestContext) => {
  const LOCKS_DIR = join(process.cwd(), ".agents/state/locks");

  await t.test("Operating mode switching should support solo, dual, and team", () => {
    // 1. Team mode
    setOperatingMode("team");
    assert.strictEqual(getOperatingMode(), "team");
    const teamProf = getActiveProfile();
    assert.strictEqual(teamProf.mode, "team");

    // 2. Dual mode
    setOperatingMode("dual");
    assert.strictEqual(getOperatingMode(), "dual");

    // 3. Return to Solo mode
    setOperatingMode("solo");
    assert.strictEqual(getOperatingMode(), "solo");
  });

  await t.test("Concurrent parallel domain leasing across N team members", () => {
    // Activate team mode
    setOperatingMode("team");

    // Developer 1 (Alice) leases 'auth'
    const ok1 = acquireLock("auth", "Alice", "DomainLead", 3600);
    assert.strictEqual(ok1, true, "Alice should acquire 'auth'");

    // Developer 2 (Bob) leases 'billing' concurrently
    const ok2 = acquireLock("billing", "Bob", "DomainLead", 3600);
    assert.strictEqual(ok2, true, "Bob should acquire 'billing' concurrently");

    // Developer 3 (Charlie) leases 'frontend' concurrently
    const ok3 = acquireLock("frontend", "Charlie", "DomainLead", 3600);
    assert.strictEqual(ok3, true, "Charlie should acquire 'frontend' concurrently");

    // Conflict test: Developer 4 (Dana) tries to steal 'auth' while actively leased to Alice
    const conflict = acquireLock("auth", "Dana", "DomainLead", 3600);
    assert.strictEqual(conflict, false, "Dana should be blocked by active lease held by Alice");

    // Cleanup leases
    releaseLock("auth", "Alice");
    releaseLock("billing", "Bob");
    releaseLock("frontend", "Charlie");

    // Revert to solo mode
    setOperatingMode("solo");
  });

  await t.test("Universal Multi-Harness Sync validates single universal instruction file and compact root", () => {
    const synced = syncAllHarnesses();
    assert.strictEqual(synced, true);

    const universalPath = join(process.cwd(), "UNIVERSAL_AGENT_INSTRUCTIONS.md");
    assert.ok(existsSync(universalPath), "UNIVERSAL_AGENT_INSTRUCTIONS.md must exist at root");

    const content = readFileSync(universalPath, "utf-8");
    assert.ok(content.includes("Universal Agent System Prompt"), "Must contain universal system prompt");
    assert.ok(content.includes("Cursor"), "Must document Cursor setup");
    assert.ok(content.includes("Claude Code"), "Must document Claude Code setup");
    assert.ok(content.includes("Windsurf"), "Must document Windsurf setup");
    assert.ok(content.includes("GitHub Copilot"), "Must document GitHub Copilot setup");

    // Assert tool-specific harness subdirectories are eliminated to prevent bloat
    assert.strictEqual(existsSync(join(process.cwd(), ".claude")), false, ".claude/ must not exist");
    assert.strictEqual(existsSync(join(process.cwd(), ".cursor")), false, ".cursor/ must not exist");
    assert.strictEqual(existsSync(join(process.cwd(), ".windsurf")), false, ".windsurf/ must not exist");
    assert.strictEqual(existsSync(join(process.cwd(), ".github")), false, ".github/ must not exist");
    assert.strictEqual(existsSync(join(process.cwd(), ".codex")), false, ".codex/ must not exist");
  });
});
