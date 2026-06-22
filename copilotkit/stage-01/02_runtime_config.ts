/**
 * 02_runtime_config.ts - CopilotRuntime 配置最佳实践
 */

export type RuntimeConfig = {
  basePath: string;
  mode: "single-route" | "multi-route";
  agents: Record<string, { model: string }>;
  a2ui?: { injectA2UITool: boolean };
};

export const productionRuntime: RuntimeConfig = {
  basePath: "/api/copilotkit",
  mode: "single-route",
  agents: {
    default: { model: "openai/gpt-4o-mini" },
  },
  a2ui: { injectA2UITool: false }, // 生产默认 Fixed Schema
};

export const exploreRuntime: RuntimeConfig = {
  ...productionRuntime,
  a2ui: { injectA2UITool: true }, // 探索 Dynamic Schema
};

function main() {
  console.log("=".repeat(50));
  console.log("02 - Runtime Config");
  console.log("=".repeat(50));
  console.log("\n  生产:", JSON.stringify(productionRuntime, null, 2));
  console.log("\n  探索:", JSON.stringify(exploreRuntime, null, 2));
  console.log("\n[OK] 完成");
}

import { fileURLToPath } from "node:url";
if (process.argv[1] === fileURLToPath(import.meta.url)) main();
