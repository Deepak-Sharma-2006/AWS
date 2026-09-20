import { existsSync, mkdirSync, writeFileSync, chmodSync } from "fs";
import { join } from "path";
import { fileURLToPath } from "node:url";

export function installGitHooks(): boolean {
  const hooksDir = join(process.cwd(), ".git/hooks");
  if (!existsSync(hooksDir)) {
    mkdirSync(hooksDir, { recursive: true });
  }

  const preCommitHook = `#!/bin/sh
# Antigravity Autonomous Pre-Commit Shield: Zero-Secret & Anti-Hallucination Gate
echo "🔒 [Pre-Commit Gate] Verifying zero secrets in staged changes..."

node --experimental-strip-types scripts/secret-scanner.ts --staged
if [ $? -ne 0 ]; then
  echo "🛑 [COMMIT REJECTED] Secret scanner detected forbidden secrets in staged diff!"
  echo "Remove hardcoded credentials before committing."
  exit 1
fi

echo "✅ [Pre-Commit Gate] Secret check passed."
exit 0
`;

  const hookPath = join(hooksDir, "pre-commit");
  writeFileSync(hookPath, preCommitHook, "utf-8");

  try {
    chmodSync(hookPath, 0o755);
  } catch {
    // Windows may ignore chmod
  }

  console.log(`✅ [Git Hook Installed] Pre-commit zero-secret barrier installed at: ${hookPath}`);
  return true;
}

const isMain = process.argv[1] && (
  fileURLToPath(import.meta.url) === process.argv[1] ||
  process.argv[1].endsWith("install-hooks.ts") ||
  process.argv[1].endsWith("install-hooks.js")
);

if (isMain) {
  installGitHooks();
}
