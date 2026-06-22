/**
 * useAgentContext 最佳实践 — 最小暴露
 */

export type AppContext = {
  selectedProductId: string | null;
  filterCategory: string;
};

export function toAgentContext(state: AppContext) {
  return [
    {
      description: "Currently selected product id on the page",
      value: state.selectedProductId,
    },
    {
      description: "Active product category filter",
      value: state.filterCategory,
    },
  ];
}
