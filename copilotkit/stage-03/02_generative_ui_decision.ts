/**
 * Generative UI 三种模式选型（见 notes/generative-ui-patterns.md）
 */

export type UiMode = "frontend_tool" | "render_tool_call" | "a2ui" | "headless";

export function pickMode(scenario: string): UiMode {
  if (scenario.includes("导航") || scenario.includes("打开页面")) return "frontend_tool";
  if (scenario.includes("订单卡片") || scenario.includes("表单")) return "a2ui";
  if (scenario.includes("Tool 富渲染")) return "render_tool_call";
  return "headless";
}

function main() {
  console.log("=".repeat(50));
  console.log("02 - Generative UI Decision");
  console.log("=".repeat(50));
  const cases = ["打开设置页", "展示订单卡片", "搜索商品结果", "完全自定义布局"];
  for (const c of cases) {
    console.log(`  ${c} -> ${pickMode(c)}`);
  }
  console.log("\n[OK] 完成");
}

main();
