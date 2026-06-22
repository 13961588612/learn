/**
 * Frontend Tool 注册表（教学模拟 useFrontendTool）
 */

export type FrontendTool = {
  name: string;
  description: string;
  parameters: Record<string, { type: string; description?: string }>;
  handler: (args: Record<string, unknown>) => string;
};

export const frontendTools: FrontendTool[] = [
  {
    name: "navigateTo",
    description: "Navigate to an in-app route. Use when user asks to open a page.",
    parameters: {
      path: { type: "string", description: "App route e.g. /orders" },
    },
    handler: (args) => `NAVIGATE:${args.path}`,
  },
  {
    name: "fillSearchQuery",
    description: "Fill the product search box on the current page.",
    parameters: {
      query: { type: "string" },
    },
    handler: (args) => `FILL_SEARCH:${args.query}`,
  },
];

function main() {
  console.log("=".repeat(50));
  console.log("02 - Frontend Tool Registry");
  console.log("=".repeat(50));
  for (const t of frontendTools) {
    console.log(`\n  ${t.name}: ${t.description.slice(0, 50)}...`);
  }
  console.log("\n  demo:", frontendTools[0].handler({ path: "/orders" }));
  console.log("\n[OK] 完成");
}

main();
