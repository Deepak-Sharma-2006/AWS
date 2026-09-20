import { existsSync, readFileSync, readdirSync, statSync } from "fs";
import { join } from "path";

const NODE_BUILTINS = new Set([
  "assert", "async_hooks", "buffer", "child_process", "cluster", "console",
  "constants", "crypto", "dgram", "diagnostics_channel", "dns", "domain",
  "events", "fs", "fs/promises", "http", "http2", "https", "inspector",
  "module", "net", "os", "path", "path/posix", "path/win32", "perf_hooks",
  "process", "punycode", "querystring", "readline", "repl", "stream",
  "stream/promises", "stream/web", "string_decoder", "sys", "timers",
  "timers/promises", "tls", "trace_events", "tty", "url", "util",
  "util/types", "v8", "vm", "wasi", "worker_threads", "zlib", "test", "sqlite"
]);

function getDeclaredDependencies(projectRoot: string): Set<string> {
  const pkgPath = join(projectRoot, "package.json");
  const declared = new Set<string>();

  if (!existsSync(pkgPath)) {
    return declared;
  }

  try {
    const pkg = JSON.parse(readFileSync(pkgPath, "utf-8"));
    if (pkg.dependencies) {
      Object.keys(pkg.dependencies).forEach((dep) => declared.add(dep));
    }
    if (pkg.devDependencies) {
      Object.keys(pkg.devDependencies).forEach((dep) => declared.add(dep));
    }
    if (pkg.peerDependencies) {
      Object.keys(pkg.peerDependencies).forEach((dep) => declared.add(dep));
    }
  } catch {
    // Malformed package.json
  }

  return declared;
}

function extractImports(fileContent: string): string[] {
  // Strip single-line and multi-line comments first to prevent matching in comments
  const strippedContent = fileContent
    .replace(/\/\*[\s\S]*?\*\//g, "")
    .replace(/\/\/.*/g, "");

  const imports: string[] = [];
  const importRegex = /(?:import\s+(?:[\w*\s{},]*\s+from\s+)?['"]([^'"]+)['"])|(?:require\(['"]([^'"]+)['"]\))/g;
  let match;

  while ((match = importRegex.exec(strippedContent)) !== null) {
    const specifier = match[1] || match[2];
    if (specifier) {
      imports.push(specifier);
    }
  }

  return imports;
}

export function validateFileImports(filePath: string, declaredDeps: Set<string>): { valid: boolean; ghostDependencies: string[] } {
  const content = readFileSync(filePath, "utf-8");
  const imports = extractImports(content);
  const ghostDependencies: string[] = [];

  for (const imp of imports) {
    // Skip relative or absolute local file imports
    if (imp.startsWith(".") || imp.startsWith("/") || imp.startsWith("\\")) {
      continue;
    }

    // Strip subpath, e.g. '@anthropic-ai/sdk' -> '@anthropic-ai/sdk' or 'lodash/clone' -> 'lodash'
    let packageName = imp;
    if (imp.startsWith("@")) {
      const parts = imp.split("/");
      packageName = parts.slice(0, 2).join("/");
    } else {
      packageName = imp.split("/")[0];
    }

    // Check if it's a node builtin (supports `node:crypto` as well)
    const cleanName = packageName.replace(/^node:/, "");
    if (NODE_BUILTINS.has(cleanName)) {
      continue;
    }

    // Check if declared in package.json
    if (!declaredDeps.has(packageName)) {
      ghostDependencies.push(packageName);
    }
  }

  return {
    valid: ghostDependencies.length === 0,
    ghostDependencies,
  };
}

export function scanDirectory(dir: string, declaredDeps: Set<string>): boolean {
  console.log(`🔍 [Anti-Hallucination] Scanning directory: ${dir}`);
  let hasErrors = false;

  function walk(currentDir: string): void {
    if (!existsSync(currentDir)) return;
    const items = readdirSync(currentDir);

    for (const item of items) {
      if (item === "node_modules" || item === ".git" || item === "dist" || item === "build") {
        continue;
      }
      const fullPath = join(currentDir, item);
      const stat = statSync(fullPath);

      if (stat.isDirectory()) {
        walk(fullPath);
      } else if (stat.isFile() && (item.endsWith(".ts") || item.endsWith(".tsx") || item.endsWith(".js") || item.endsWith(".jsx"))) {
        const result = validateFileImports(fullPath, declaredDeps);
        if (!result.valid) {
          hasErrors = true;
          console.error(`\n🚨 HALLUCINATION DETECTED in ${fullPath}:`);
          for (const ghost of result.ghostDependencies) {
            console.error(`   ❌ Ghost Dependency: '${ghost}' is imported but NOT declared in package.json!`);
          }
        }
      }
    }
  }

  walk(dir);

  if (hasErrors) {
    console.error(`\n❌ Anti-Hallucination Shield: Process failed! Remove phantom imports or declare in package.json.`);
    return false;
  }

  console.log("✅ Anti-Hallucination Shield: Zero ghost dependencies detected.");
  return true;
}

import { fileURLToPath } from "node:url";

const isMain = process.argv[1] && (
  fileURLToPath(import.meta.url) === process.argv[1] ||
  process.argv[1].endsWith("anti-hallucination-checker.ts") ||
  process.argv[1].endsWith("anti-hallucination-checker.js")
);

if (isMain) {
  const root = process.cwd();
  const declared = getDeclaredDependencies(root);
  const rawArgs = process.argv.slice(2);
  const targets = rawArgs.length > 0 ? rawArgs : ["scripts", "src", "tests", ".agents"];
  let allOk = true;

  for (const t of targets) {
    const fullPath = join(root, t);
    if (existsSync(fullPath)) {
      const ok = scanDirectory(fullPath, declared);
      if (!ok) allOk = false;
    }
  }

  process.exit(allOk ? 0 : 1);
}
