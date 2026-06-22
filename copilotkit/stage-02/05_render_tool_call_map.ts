/**
 * Render Tool Call 映射：tool 名 -> React 组件名（配置层）
 */

export const renderToolCallMap: Record<string, string> = {
  search_products: "ProductSearchResult",
  get_weather: "WeatherCard",
};

function main() {
  console.log("=".repeat(50));
  console.log("05 - Render ToolCall Map");
  console.log("=".repeat(50));
  console.log("\n  映射:", renderToolCallMap);
  console.log("\n  v2: useRenderToolCall / useDefaultRenderTool");
  console.log("\n[OK] 完成");
}

main();
