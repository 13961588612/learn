import type { A2UiMessage } from "../shared/types.ts";

const SURFACE_FLOW: A2UiMessage[] = [
  { kind: "createSurface", surfaceId: "order-card", catalogId: "company-v1" },
  {
    kind: "updateComponents",
    surfaceId: "order-card",
    components: [{ id: "root", type: "Card", children: ["title", "status"] }],
  },
  { kind: "updateDataModel", surfaceId: "order-card", path: "/title", value: "Order #1024" },
  { kind: "updateDataModel", surfaceId: "order-card", path: "/status", value: "shipped" },
];

function main() {
  console.log("=".repeat(50));
  console.log("01 - A2UI Surface Lifecycle");
  console.log("=".repeat(50));
  for (const msg of SURFACE_FLOW) {
    console.log(`  ${msg.kind}${"surfaceId" in msg ? ` (${msg.surfaceId})` : ""}`);
  }
  console.log("\n[OK] 完成");
}

main();
