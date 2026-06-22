# 02-ag-ui-tools · AG-UI 客户端原语

对应 **stage-02~03 / P1**。

## 内容

| 文件 | 说明 |
|------|------|
| `features/frontendTools.ts` | Frontend Tool 定义模板 |
| `features/useAppContext.ts` | Agent Context 最小暴露 |
| `features/interruptExample.md` | Interrupt 流程说明 |

## 集成方式

1. 复制 `01-runtime-starter` 为基座
2. 在 Client Component 中 `useCopilotAction` 注册 `frontendTools.ts` 中的工具
3. 用 `useCopilotReadable` / v2 `useAgentContext` 暴露页面状态

## Interrupt 示例流程

见 [interruptExample.md](features/interruptExample.md)

## 验收

- [ ] Agent 能回答「当前选中哪个商品」
- [ ] navigateTo 或 selectProduct 可演示
- [ ] 至少 1 次 HITL 确认
