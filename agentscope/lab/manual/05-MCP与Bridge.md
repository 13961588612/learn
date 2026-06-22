# 5 · MCP 与 Bridge

## MCP

`Toolkit(mcps=[MCPClient(...)])` — 见官方文档与 `showcase/03`。

## IntentGate Bridge

契约（对齐 `intentgate/adapters/agentscope.py`）：

```
POST /v1/sessions/{id}/messages  -> SSE data: {AgentReply JSON}
POST /v1/sessions/{id}/actions   -> SSE
```

运行：

```bash
uv sync --group agentscope-showcase
uv run python agentscope/showcase/04_intentgate_bridge/app/main.py
```

[← 返回](../README.md)
