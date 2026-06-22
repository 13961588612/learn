# AgentScope 专业示范

| 目录 | 阶段 | 说明 |
|------|------|------|
| [01_readonly_toolkit_audit/](01_readonly_toolkit_audit/) | P1 | 只读 Tool + Audit Middleware |
| [02_multi_agent_handoff/](02_multi_agent_handoff/) | P3 | Researcher -> Writer |
| [03_mcp_internal_api/](03_mcp_internal_api/) | P4 | 只读工单 MCP 预备 |
| [04_intentgate_bridge/](04_intentgate_bridge/) | P6 | FastAPI SSE Bridge 二开 |

```bash
uv sync --group agentscope-core
uv sync --group agentscope-showcase   # Bridge
```

学习顺序：stage-1~2 + **01** -> stage-4 + **02** -> stage-5 + **03** -> stage-7 + **04**
