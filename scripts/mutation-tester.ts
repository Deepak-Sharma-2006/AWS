/**
 * Enterprise Agentic Mutation Testing Engine
 * Prevents the "Green Signal Trap" by injecting deliberate syntax and boundary
 * mutations into code to verify that the test suite actively detects faults.
 *
 * Mandate: Mutation Score >= 80% required for production release.
 */

import { existsSync, readFileSync, writeFileSync, unlinkSync } from "fs";
import { join } from "path";
import { execSync } from "child_process";
import { fileURLToPath } from "node:url";

export interface MutationPattern {
  name: string;
  category: "boundary" | "return" | "arithmetic" | "logic";
  search: RegExp;
  replace: string;
}

export const MUTATION_PATTERNS: MutationPattern[] = [
  // 1. Boundary Mutations
  { name: "Strict Equality Inversion", category: "boundary", search: /===/g, replace: "!==" },
  { name: "Strict Inequality Inversion", category: "boundary", search: /!==/g, replace: "===" },
  { name: "Greater Than Inversion", category: "boundary", search: />(?!=)/g, replace: "<=" },
  { name: "Less Than Inversion", category: "boundary", search: /<(?!=)/g, replace: ">=" },

  // 2. Boolean & Logic Mutations
  { name: "Boolean True Inversion", category: "logic", search: /\btrue\b/g, replace: "false" },
  { name: "Boolean False Inversion", category: "logic", search: /\bfalse\b/g, replace: "true" },
  { name: "Logical AND to OR", category: "logic", search: /&&/g, replace: "||" },
  { name: "Logical OR to AND", category: "logic", search: /\|\|/g, replace: "&&" },

  // 3. Arithmetic Mutations
  { name: "Addition to Subtraction", category: "arithmetic", search: /\s\+\s/g, replace: " - " },
  { name: "Subtraction to Addition", category: "arithmetic", search: /\s\-\s/g, replace: " + " },

  // 4. Return Value Mutations
  { name: "Return Nullification", category: "return", search: /return\s+([a-zA-Z0-9_\.]+);/g, replace: "return null as any;" }
];

export interface MutationResult {
  mutantId: string;
  patternName: string;
  category: string;
  file: string;
  status: "KILLED" | "SURVIVED" | "SYNTAX_ERROR";
  executionTimeMs: number;
}

export interface MutationReport {
  totalMutants: number;
  killedCount: number;
  survivedCount: number;
  mutationScore: number;
  passedThreshold: boolean;
  threshold: number;
  results: MutationResult[];
}

export function runMutationTest(
  targetFile = "src/index.ts",
  testCommand = "npm run test:unit",
  threshold = 80
): MutationReport {
  console.log(`\n🧬 [Mutation Testing Engine] Probing test fidelity on '${targetFile}'...`);
  console.log(`   Test Runner Command : ${testCommand}`);
  console.log(`   Acceptance Threshold: >= ${threshold}% Mutants Killed\n`);

  const fullPath = join(process.cwd(), targetFile);
  if (!existsSync(fullPath)) {
    throw new Error(`Target file not found: ${fullPath}`);
  }

  const originalContent = readFileSync(fullPath, "utf-8");
  const backupPath = `${fullPath}.bak`;
  writeFileSync(backupPath, originalContent, "utf-8");

  const restoreOriginal = () => {
    try {
      if (existsSync(backupPath)) {
        writeFileSync(fullPath, originalContent, "utf-8");
        unlinkSync(backupPath);
      }
    } catch {
      // Ignore cleanup error
    }
  };

  const onSignal = () => {
    restoreOriginal();
    process.exit(1);
  };

  const onException = (err: any) => {
    restoreOriginal();
    console.error("Mutation runner exception:", err);
    process.exit(1);
  };

  process.on("SIGINT", onSignal);
  process.on("SIGTERM", onSignal);
  process.on("uncaughtException", onException);

  const results: MutationResult[] = [];

  try {
    let mutantCounter = 0;

    for (const pattern of MUTATION_PATTERNS) {
      if (!pattern.search.test(originalContent)) {
        continue;
      }
      // Reset regex index
      pattern.search.lastIndex = 0;

      // Generate mutant with single mutation replacement
      let matchCount = 0;
      const mutatedContent = originalContent.replace(pattern.search, (match) => {
        // Mutate first occurrence per pattern
        if (matchCount === 0) {
          matchCount++;
          return pattern.replace;
        }
        return match;
      });

      if (mutatedContent === originalContent) {
        continue;
      }

      mutantCounter++;
      const mutantId = `M${mutantCounter.toString().padStart(3, "0")}`;
      process.stdout.write(`   ▶ Testing ${mutantId} [${pattern.name}] (${pattern.category})... `);

      const startTime = Date.now();
      // Write mutant
      writeFileSync(fullPath, mutatedContent, "utf-8");

      let testFailed = false;
      try {
        execSync(testCommand, { stdio: "pipe", timeout: 15000 });
      } catch {
        // Exit code != 0 means test suite failed on the mutation -> Mutant KILLED!
        testFailed = true;
      }

      const duration = Date.now() - startTime;
      if (testFailed) {
        console.log(`🗡️  KILLED (${duration}ms)`);
        results.push({
          mutantId,
          patternName: pattern.name,
          category: pattern.category,
          file: targetFile,
          status: "KILLED",
          executionTimeMs: duration
        });
      } else {
        console.log(`⚠️  SURVIVED (Tests failed to catch this fault!)`);
        results.push({
          mutantId,
          patternName: pattern.name,
          category: pattern.category,
          file: targetFile,
          status: "SURVIVED",
          executionTimeMs: duration
        });
      }
    }

    const total = results.length;
    const killed = results.filter((r) => r.status === "KILLED").length;
    const survived = results.filter((r) => r.status === "SURVIVED").length;
    const score = total > 0 ? Math.round((killed / total) * 100) : 100;
    const passed = score >= threshold;

    console.log(`\n================================================================================`);
    console.log(`📊 MUTATION TEST FIDELITY REPORT`);
    console.log(`================================================================================`);
    console.log(`   Target Tested   : ${targetFile}`);
    console.log(`   Total Mutants   : ${total}`);
    console.log(`   Mutants Killed  : ${killed} 🗡️`);
    console.log(`   Mutants Survived: ${survived} ⚠️`);
    console.log(`   Mutation Score  : ${score}% (Threshold: >= ${threshold}%)`);
    console.log(`   Verdict         : ${passed ? "✅ PASSED (High Test Fidelity)" : "❌ FAILED (Green Signal Trap Detected)"}`);
    console.log(`================================================================================\n`);

    return {
      totalMutants: total,
      killedCount: killed,
      survivedCount: survived,
      mutationScore: score,
      passedThreshold: passed,
      threshold,
      results
    };
  } finally {
    restoreOriginal();
    process.removeListener("SIGINT", onSignal);
    process.removeListener("SIGTERM", onSignal);
    process.removeListener("uncaughtException", onException);
  }
}

const isMain = process.argv[1] && (
  fileURLToPath(import.meta.url) === process.argv[1] ||
  process.argv[1].endsWith("mutation-tester.ts") ||
  process.argv[1].endsWith("mutation-tester.js")
);

if (isMain) {
  const target = process.argv[2] || "src/index.ts";
  const cmd = process.argv[3] || "npm run test:unit";
  const report = runMutationTest(target, cmd);
  process.exit(report.passedThreshold ? 0 : 1);
}
