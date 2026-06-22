# Generative UI 三种模式选型

| 模式 | API | 适用 |
|------|-----|------|
| Frontend Tool | `useFrontendTool` | 导航、填表、改页内状态 |
| Render Tool Call | `useRenderToolCall` | Tool 结果富渲染 |
| A2UI | Catalog + Surface 消息 | 订单卡片、表格、可审计 UI |
| Headless | `useAgent` | 完全自定义布局 |

## 决策

- 跨端复用 UI → **A2UI**
- 只改当前页 → **Frontend Tool**
- 生产支付/权限 → **Fixed A2UI + Interrupt**

详见 [`../../base/copilotkit-a2ui/notes/generative-ui-patterns.md`](../../base/copilotkit-a2ui/notes/generative-ui-patterns.md)
