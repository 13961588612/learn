const ALLOWED_CATALOG_TYPES = new Set(["Text", "Card", "StatusBadge", "DataTable", "Button"]);

function validateComponent(type: string): boolean {
  return ALLOWED_CATALOG_TYPES.has(type);
}

function main() {
  console.log("=".repeat(50));
  console.log("03 - Catalog Whitelist");
  console.log("=".repeat(50));
  for (const t of ["Card", "Script", "RawHtml"]) {
    console.log(`  ${t}: ${validateComponent(t) ? "ALLOW" : "DENY"}`);
  }
  console.log("\n  禁止: dangerouslySetInnerHTML 类组件");
  console.log("\n[OK] 完成");
}

main();
