import { redactPii } from "../shared/types.ts";

function main() {
  console.log("=".repeat(50));
  console.log("03 - PII Redaction");
  console.log("=".repeat(50));
  const raw = "联系人 zhang@corp.com 手机 13800138000";
  console.log("\n  原始:", raw);
  console.log("  脱敏:", redactPii(raw));
  console.log("\n[OK] 完成");
}

main();
