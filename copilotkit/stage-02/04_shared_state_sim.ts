/**
 * 共享状态模拟：页面 state + Agent 可读快照
 */

type AppState = {
  selectedProductId: string | null;
  filters: { category: string };
};

function toAgentSnapshot(state: AppState) {
  return {
    selectedProductId: state.selectedProductId,
    filterCategory: state.filters.category,
  };
}

function main() {
  console.log("=".repeat(50));
  console.log("04 - Shared State Sim");
  console.log("=".repeat(50));
  const state: AppState = { selectedProductId: "P-9", filters: { category: "device" } };
  console.log("\n  snapshot:", toAgentSnapshot(state));
  console.log("\n[OK] 完成");
}

main();
