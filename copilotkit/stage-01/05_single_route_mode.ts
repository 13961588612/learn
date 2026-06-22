/**
 * 05_single_route_mode.ts - single-route Runtime 模式
 *
 * 最佳实践: 同源 /api/copilotkit，避免 CORS 与密钥暴露
 */

export type HandlerOptions = {
  runtime: { agents: string[] };
  basePath: string;
  mode: "single-route";
};

export function buildHandlerOptions(): HandlerOptions {
  return {
    runtime: { agents: ["default"] },
    basePath: "/api/copilotkit",
    mode: "single-route",
  };
}

function main() {
  console.log("=".repeat(50));
  console.log("05 - Single Route Mode");
  console.log("=".repeat(50));
  console.log("\n  layout.tsx:");
  console.log('    <CopilotKitProvider runtimeUrl="/api/copilotkit">');
  console.log("\n  route.ts:");
  console.log("    createCopilotRuntimeHandler({ basePath, mode: 'single-route' })");
  console.log("\n  配置:", JSON.stringify(buildHandlerOptions(), null, 2));
  console.log("\n[OK] 完成");
}

main();
