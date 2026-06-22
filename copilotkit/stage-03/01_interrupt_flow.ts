/**
 * Interrupt / HITL 流程模拟
 */

type InterruptState = "idle" | "pending" | "approved" | "rejected";

function runInterruptFlow(userApproves: boolean): InterruptState[] {
  const log: InterruptState[] = ["idle", "pending"];
  log.push(userApproves ? "approved" : "rejected");
  return log;
}

function main() {
  console.log("=".repeat(50));
  console.log("01 - Interrupt Flow");
  console.log("=".repeat(50));
  console.log("\n  批准:", runInterruptFlow(true).join(" -> "));
  console.log("  拒绝:", runInterruptFlow(false).join(" -> "));
  console.log("\n  适用: 支付、删除、权限变更 — useInterrupt");
  console.log("\n[OK] 完成");
}

main();
