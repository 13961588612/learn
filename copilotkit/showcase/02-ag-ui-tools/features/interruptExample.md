# Interrupt / HITL 示例

```tsx
// Client Component — 伪代码
useCopilotAction({
  name: "deleteOrder",
  description: "Delete an order. Requires user confirmation.",
  parameters: [{ name: "orderId", type: "string", required: true }],
  handler: async ({ orderId }) => {
    const ok = await confirm(`确认删除订单 ${orderId}?`);
    if (!ok) return "用户取消";
    // ...
    return "已删除";
  },
});
```

生产推荐：`useInterrupt` + A2UI 展示订单详情后再确认。
