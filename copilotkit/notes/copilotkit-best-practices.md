# CopilotKit + A2UI · 最佳实践速查

> 完整版：[`../../base/copilotkit-a2ui/notes/copilotkit-best-practices.md`](../../base/copilotkit-a2ui/notes/copilotkit-best-practices.md)

## 核心原则

1. **v2 + 同源 Runtime**：`CopilotKitProvider runtimeUrl="/api/copilotkit"`
2. **密钥只在服务端**：禁止 `NEXT_PUBLIC_*` 存 API Key
3. **生产 A2UI**：`injectA2UITool: false`，Fixed Schema + Catalog 白名单
4. **Context 最小暴露**：`useAgentContext` 只传必要字段，PII 脱敏
5. **HITL**：支付/删除/权限 → `useInterrupt` + A2UI 详情
6. **错误降级**：SSE 断线、A2UI 解析失败、401/5xx 各有 UX
7. **LangGraph**：token 经 `onRequest` → `configurable.authorization`

## Runtime 模板

见 [showcase/01-runtime-starter/app/api/copilotkit/route.ts](../showcase/01-runtime-starter/app/api/copilotkit/route.ts)
