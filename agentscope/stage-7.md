# 阶段七：IntentGate 二开 Capstone（P6）

```bash
uv sync --group agentscope-showcase
uv run python agentscope/showcase/04_intentgate_bridge/app/main.py
```

对接：`langchain/practice/intentgate` · `AgentScopeBackend`

手册：[lab/manual/05-MCP与Bridge.md](lab/manual/05-MCP与Bridge.md)

## 验收

- [ ] Bridge `/health` 200
- [ ] curl messages 收到 SSE
- [ ] IntentGate 配置 base_url 联调（可选）
