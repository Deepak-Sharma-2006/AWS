/**
 * Antigravity Enterprise Model Context Protocol (MCP) Server
 * Exposes TaskDispatcher and SquadOrchestrator tools via standard JSON-RPC stdio.
 * Compatible with Claude Desktop, Claude Code, Cursor, Windsurf, and open-source MCP clients.
 */

import { createInterface } from "node:readline";
import { spawn } from "node:child_process";
import { join } from "node:path";

interface McpTool {
  name: string;
  description: string;
  inputSchema: {
    type: "object";
    properties: Record<string, any>;
    required?: string[];
  };
}

const TOOLS: McpTool[] = [
  {
    name: "orchestrator_solution",
    description: "Formulates a first-principles dynamic solution architecture with multi-hop live research and 4-moat defensibility matrix.",
    inputSchema: {
      type: "object",
      properties: {
        prompt: { type: "string", description: "Problem statement or feature goal to formulate." },
      },
      required: ["prompt"],
    },
  },
  {
    name: "orchestrator_squad",
    description: "Executes the 6+1 Enterprise Agile Product Squad lifecycle on a feature with TDD self-healing, AST mutation testing, and living documentation.",
    inputSchema: {
      type: "object",
      properties: {
        feature: { type: "string", description: "Name of the feature to implement." },
        mode: { type: "string", enum: ["solo", "dual", "team"], description: "Execution mode." },
      },
      required: ["feature"],
    },
  },
  {
    name: "orchestrator_research",
    description: "Launches deep empirical research triangulation across 4 modes (EXPLORATION, FEASIBILITY, DIAGNOSTIC, IMPACT) with a minimum 120s deliberation timer.",
    inputSchema: {
      type: "object",
      properties: {
        prompt: { type: "string", description: "Topic or issue to research deeply." },
        mode: { type: "string", enum: ["EXPLORATION", "FEASIBILITY", "DIAGNOSTIC", "IMPACT"], description: "Research operating mode." },
        min_time: { type: "number", description: "Minimum deliberation time budget in seconds (default 120)." },
      },
      required: ["prompt"],
    },
  },
  {
    name: "orchestrator_audit",
    description: "Executes an enterprise 5-pillar project diagnostic audit or brownfield onboarding remediation on an existing or in-progress codebase.",
    inputSchema: {
      type: "object",
      properties: {
        target: { type: "string", description: "Target directory or file path to audit." },
        auto_heal: { type: "boolean", description: "Whether to automatically heal broken stubs and failing tests." },
      },
      required: ["target"],
    },
  },
  {
    name: "orchestrator_team_status",
    description: "Displays the active N-person team roster, active domain lease locks, and cross-device workstation statuses.",
    inputSchema: {
      type: "object",
      properties: {},
    },
  },
  {
    name: "orchestrator_attest",
    description: "Verifies the cryptographic SQLite attestation ledger and prints the latest verified execution provenance hashes.",
    inputSchema: {
      type: "object",
      properties: {
        verify: { type: "boolean", description: "True to verify the cryptographic ledger integrity." },
      },
    },
  },
];

function runCommand(command: string, args: string[]): Promise<string> {
  return new Promise((resolve, reject) => {
    const proc = spawn(command, args, { cwd: process.cwd(), shell: true });
    let stdout = "";
    let stderr = "";
    proc.stdout.on("data", (d: Buffer | string) => { stdout += d.toString(); });
    proc.stderr.on("data", (d: Buffer | string) => { stderr += d.toString(); });
    proc.on("close", (code: number | null) => {
      if (code === 0) resolve(stdout);
      else resolve(`[Command completed with exit code ${code}]\n${stdout}\n${stderr}`);
    });
    proc.on("error", (err: Error) => reject(err));
  });
}

async function handleToolCall(name: string, args: Record<string, any>): Promise<string> {
  if (name === "orchestrator_solution") {
    return await runCommand("python", ["-m", "scripts.orchestrator.task_dispatcher", "--task", "solution", "--prompt", `"${args.prompt}"`]);
  } else if (name === "orchestrator_squad") {
    return await runCommand("python", ["-m", "scripts.orchestrator.task_dispatcher", "--task", "squad", "--feature", args.feature, "--mode", args.mode || "solo"]);
  } else if (name === "orchestrator_research") {
    const cmdArgs = ["-m", "scripts.orchestrator.task_dispatcher", "--task", "research", "--prompt", `"${args.prompt}"`];
    if (args.mode) cmdArgs.push("--research-mode", args.mode);
    if (args.min_time) cmdArgs.push("--min-time", String(args.min_time));
    return await runCommand("python", cmdArgs);
  } else if (name === "orchestrator_audit") {
    const cmdArgs = ["-m", "scripts.orchestrator.task_dispatcher", "--task", "audit", "--target", `"${args.target}"`];
    if (args.auto_heal) cmdArgs.push("--auto-heal");
    return await runCommand("python", cmdArgs);
  } else if (name === "orchestrator_team_status") {
    return await runCommand("node", ["--experimental-strip-types", "scripts/role-switch.ts", "team-status"]);
  } else if (name === "orchestrator_attest") {
    return await runCommand("python", ["-m", "scripts.orchestrator.squad_attestation", "--verify"]);
  }
  throw new Error(`Tool not found: ${name}`);
}

export function startMcpServer(): void {
  const rl = createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal: false,
  });

  rl.on("line", async (line: string) => {
    if (!line.trim()) return;
    try {
      const msg = JSON.parse(line);
      const { id, method, params } = msg;

      if (method === "initialize") {
        const response = {
          jsonrpc: "2.0",
          id,
          result: {
            protocolVersion: "2024-11-05",
            capabilities: { tools: {} },
            serverInfo: {
              name: "antigravity-enterprise-orchestrator",
              version: "1.0.0",
            },
          },
        };
        console.log(JSON.stringify(response));
      } else if (method === "tools/list") {
        const response = {
          jsonrpc: "2.0",
          id,
          result: { tools: TOOLS },
        };
        console.log(JSON.stringify(response));
      } else if (method === "tools/call") {
        const { name, arguments: toolArgs } = params;
        try {
          const resultText = await handleToolCall(name, toolArgs);
          const response = {
            jsonrpc: "2.0",
            id,
            result: {
              content: [{ type: "text", text: resultText }],
            },
          };
          console.log(JSON.stringify(response));
        } catch (e: any) {
          const response = {
            jsonrpc: "2.0",
            id,
            error: { code: -32603, message: e.message || "Internal Tool Execution Error" },
          };
          console.log(JSON.stringify(response));
        }
      } else if (method === "notifications/initialized") {
        // No response needed for notification
      } else {
        const response = {
          jsonrpc: "2.0",
          id,
          error: { code: -32601, message: `Method not found: ${method}` },
        };
        console.log(JSON.stringify(response));
      }
    } catch (e: any) {
      // Ignore unparseable lines or print JSON-RPC error
    }
  });
}

import { fileURLToPath } from "node:url";
const isMain = process.argv[1] && (
  fileURLToPath(import.meta.url) === process.argv[1] ||
  process.argv[1].endsWith("mcp-server.ts") ||
  process.argv[1].endsWith("mcp-server.js")
);

if (isMain) {
  startMcpServer();
}
