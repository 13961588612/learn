# CopilotKit + A2UI · 最佳实践速查

> P5 项目逐项验证。

## 1. 始终 v2 + 同源 Runtime

```tsx
// app/layout.tsx
<CopilotKitProvider runtimeUrl="/api/copilotkit" a2ui={{ catalog: companyCatalog }}>
  {children}
</CopilotKitProvider>
```

- 同源部署 → **无需 CORS**
- 勿把 `OPENAI_API_KEY` 放进 `NEXT_PUBLIC_*`

## 2. Runtime Handler 模板

```typescript
// app/api/copilotkit/route.ts
import { CopilotRuntime, createCopilotRuntimeHandler, BuiltInAgent } from "@copilotkit/runtime/v2";

const runtime = new CopilotRuntime({
  agents: {
    default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
  },
  a2ui: { injectA2UITool: false }, // Fixed Schema 生产可 false
});

export const POST = createCopilotRuntimeHandler({
  runtime,
  basePath: "/api/copilotkit",
  mode: "single-route",
  hooks: {
    onRequest: ({ request }) => {
      // JWT 校验 — 见 P4
    },
  },
});
```

可运行示例见 `showcase/01-runtime-starter/app/api/copilotkit/route.ts`。

## 3. A2UI 生产默认 Fixed Schema

| 环境 | injectA2UITool | 说明 |
|------|----------------|------|
| 探索 | true | Dynamic，慢但灵活 |
| **生产** | false | 人审模板 + dataModel |

## 4. Catalog 安全

- 不注册 `dangerouslySetInnerHTML` 类组件
- `includeBasicCatalog: false` 用于高合规页面（仅公司组件）
- 不可信 Agent：不用项目级随意 Catalog

## 5. Context 最小暴露

```typescript
useAgentContext({
  description: "Currently selected order",
  value: selectedOrderId,
});
```

- 只传 Agent **需要**的字段，不传整页 state
- PII 字段脱敏或 hash

## 6. Interrupt / HITL

- 支付、删除、权限变更 → **必须** `useInterrupt`
- A2UI 展示详情，Interrupt 负责确认

## 7. 错误与降级

| 失败 | UX |
|------|-----|
| SSE 断线 | 重连提示 + 保留最后消息 |
| A2UI 解析错 | 降级 Markdown + 错误码 |
| LangGraph 5xx | 「服务暂不可用」+ requestId |
| 401 | 跳转登录 |

## 8. 性能

- 大 Surface 分多次 `updateComponents`
- Catalog 组件 `React.memo`
- Chat 路由 `dynamic(() => import(...), { ssr: false })`

## 9. a11y

- Catalog 组件继承设计系统 aria
- CopilotChat 键盘 trap 不遮挡主内容
- 流式更新时 `aria-live="polite"`

## 10. 测试

```typescript
// Playwright 冒烟
await page.getByRole("textbox").fill("show order 1024");
await page.getByRole("button", { name: "Send" }).click();
await expect(page.getByTestId("a2ui-surface")).toBeVisible();
```

## 11. 与 LangGraph 协作

- Agent 节点返回 A2UI 消息放在 tool result 或 AG-UI 中间件识别的字段
- 复杂图状态在 LangGraph；**UI 意图**在 A2UI 消息
- 鉴权 token → `configurable.authorization`

## 12. 发布 checklist

```
[ ] .env.example 完整
[ ] onRequest 鉴权启用
[ ] Catalog 版本 tag
[ ] Fixed 模板 review
[ ] E2E 冒烟绿
[ ] Lighthouse a11y 无 critical
```

---

## 踩坑记录

| 现象 | 根因 | 修复 |
|------|------|------|
| A2UI 空白 | Runtime 未开 a2ui | Provider / runtime 加 `a2ui: true` 或 catalog |
| CORS 报错 | Runtime 跨域 | 改为同源 `runtimeUrl="/api/copilotkit"` |
| Key 泄露 | `NEXT_PUBLIC_*` 存密钥 | 仅服务端 `.env` + Runtime handler |
