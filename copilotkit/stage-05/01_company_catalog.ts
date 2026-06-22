/**
 * 公司 Catalog 组件 schema（agent-facing description）
 */

export const companyCatalog = {
  catalogId: "company-v1",
  components: {
    StatusBadge: {
      description: "Show order or ticket status with color coding",
      props: { status: "string", variant: "success|warning|error" },
    },
    UserCard: {
      description: "Display employee name, role, avatar",
      props: { name: "string", role: "string" },
    },
    DataTable: {
      description: "Tabular data with columns; use for lists under 20 rows",
      props: { columns: "string[]", rows: "object[]" },
    },
  },
};

function main() {
  console.log("=".repeat(50));
  console.log("01 - Company Catalog");
  console.log("=".repeat(50));
  console.log(JSON.stringify(companyCatalog, null, 2));
  console.log("\n[OK] 完成");
}

main();
