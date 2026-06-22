/**
 * Frontend Tool 最佳实践（复制到 Client Component）
 *
 * import { useCopilotAction } from "@copilotkit/react-core";
 */

export const frontendToolDefinitions = [
  {
    name: "navigateTo",
    description: "Navigate to an in-app route when the user asks to open a page.",
    parameters: [
      { name: "path", type: "string", description: "Route path e.g. /orders", required: true },
    ],
  },
  {
    name: "selectProduct",
    description: "Select a product on the current page by id.",
    parameters: [
      { name: "productId", type: "string", required: true },
    ],
  },
] as const;

/** 在组件内: useCopilotAction({ name, description, parameters, handler }) */
