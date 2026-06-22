const A11Y = [
  "Catalog 组件继承设计系统 aria",
  "CopilotChat 键盘 trap 不遮挡主内容",
  "流式更新 aria-live=polite",
];

function main() {
  console.log("=".repeat(50));
  console.log("02 - A11y Checklist");
  console.log("=".repeat(50));
  A11Y.forEach((x) => console.log(`  - ${x}`));
  console.log("\n[OK] 完成");
}

main();
