/**
 * Fixed Schema：人写组件树，Agent 只填 dataModel
 */

export const fixedOrderCardSchema = {
  surfaceId: "order-card",
  components: [
    { id: "title", type: "Text", bind: "/title" },
    { id: "status", type: "StatusBadge", bind: "/status" },
  ],
  dataModel: { title: "", status: "pending" },
};

function main() {
  console.log("=".repeat(50));
  console.log("02 - Fixed Schema");
  console.log("=".repeat(50));
  console.log(JSON.stringify(fixedOrderCardSchema, null, 2));
  console.log("\n  生产默认: injectA2UITool=false，Agent 只更新 dataModel");
  console.log("\n[OK] 完成");
}

main();
