/**
 * 01_stack_overview.ts - AG-UI / A2UI / CopilotKit 协议栈
 *
 * 学习要点:
 * 1. CopilotKit = 前端 SDK + Next Runtime（BFF）
 * 2. AG-UI = Agent↔App 双向 SSE 事件流
 * 3. A2UI = 声明式 Generative UI JSON（Catalog 白名单渲染）
 */

const STACK = [
  { layer: "业务应用", items: ["Next.js 页面", "设计系统组件"] },
  { layer: "CopilotKit 客户端", items: ["CopilotKitProvider", "CopilotChat", "A2UI Renderer"] },
  { layer: "传输", items: ["AG-UI / SSE", "/api/copilotkit"] },
  { layer: "Runtime + Agent", items: ["BuiltInAgent", "LangGraphAgent"] },
];

function main() {
  console.log("=".repeat(50));
  console.log("01 - Stack Overview");
  console.log("=".repeat(50));

  for (const { layer, items } of STACK) {
    console.log(`\n  [${layer}]`);
    items.forEach((i) => console.log(`    - ${i}`));
  }

  console.log("\n  边界: Runtime 跑在 route.ts（服务端），密钥不进客户端 bundle");
  console.log("\n[OK] 完成");
}

main();
