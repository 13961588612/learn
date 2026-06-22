/**
 * 公司 A2UI Catalog 定义（agent-facing）
 */

export const companyCatalog = {
  catalogId: "learn-company-v1",
  includeBasicCatalog: true,
  components: {
    StatusBadge: {
      description: "Colored badge for order/ticket status",
      props: { status: "string", variant: "success|warning|error" },
    },
    OrderCard: {
      description: "Compact order summary card",
      props: { orderId: "string", title: "string", status: "string" },
    },
    DataTable: {
      description: "Table for up to 20 rows",
      props: { columns: "string[]", rows: "object[]" },
    },
  },
};

export const fixedOrderSurface = {
  surfaceId: "order-preview",
  components: [
    { id: "card", type: "OrderCard", bind: { orderId: "/id", title: "/title", status: "/status" } },
  ],
  dataModel: { id: "", title: "", status: "pending" },
};
