/**
 * stage-02: AG-UI 客户端原语 — Agent Context 与最小暴露
 */

export type AgentContextEntry = {
  description: string;
  value: unknown;
};

export function buildOrderContext(selectedOrderId: string | null): AgentContextEntry[] {
  if (!selectedOrderId) return [];
  return [{ description: "Currently selected order id", value: selectedOrderId }];
}

function main() {
  console.log("=".repeat(50));
  console.log("02 - Agent Context");
  console.log("=".repeat(50));
  console.log("\n  有选中:", buildOrderContext("ORD-1024"));
  console.log("  无选中:", buildOrderContext(null));
  console.log("\n  最佳实践: 只传 Agent 需要的字段，不传整页 state");
  console.log("\n[OK] 完成");
}

main();
