const DEPLOY_CHECKLIST = [
  ".env.example 完整",
  "onRequest 鉴权启用",
  "Catalog 版本 tag",
  "Fixed 模板 review",
  "E2E 冒烟通过",
  "a11y 无 critical",
];

function main() {
  console.log("=".repeat(50));
  console.log("01 - Deploy Checklist");
  console.log("=".repeat(50));
  DEPLOY_CHECKLIST.forEach((item, i) => console.log(`  [ ] ${i + 1}. ${item}`));
  console.log("\n[OK] 完成");
}

main();
