# AgentScope 架构速查（2.x）

## 核心模块

| 模块 | 职责 |
|------|------|
| `message` | `Msg`、`UserMsg`、ContentBlock（Text/ToolCall/ToolResult） |
| `agent` | 统一 `Agent`：reply / reply_stream / observe |
| `tool` | `Toolkit`、`FunctionTool`、MCP、Skills、内置 Read/Write/Bash |
| `model` | `OpenAIChatModel`、`DashScopeChatModel` 等 |
| `middleware` | `on_reply` / `on_acting` / `on_reasoning` 审计与扩展 |
| `permission` | Tool 级权限决策 |
| `mcp` | `MCPClient` 接入外部系统 |
| `skill` | Agent Skills 目录加载 |

## Agent Loop（2.x）

```
reply(inputs) ->
  reasoning (model call) ->
  acting (tool calls, permission, middleware) ->
  循环直至产出最终 Msg
```

与 OpenHarness 对比：**AgentScope 是应用层多 Agent 框架**；OpenHarness 是统一 Harness 壳。

## 二开挂载点

1. **FunctionTool** — 公司业务 Tool
2. **Middleware** — 审计、限流、Tracing
3. **Toolkit(mcps=...)** — MCP 只读接入
4. **FastAPI Bridge** — 对接 IntentGate / 自研 Gateway
