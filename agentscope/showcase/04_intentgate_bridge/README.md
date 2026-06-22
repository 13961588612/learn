# Showcase 04 · IntentGate Bridge（二开 Capstone）

FastAPI SSE，契约对齐 `intentgate/adapters/agentscope.py`。

```bash
uv sync --group agentscope-showcase
uv run python agentscope/showcase/04_intentgate_bridge/app/main.py

curl -N -X POST http://127.0.0.1:8090/v1/sessions/s1/messages \
  -H "Content-Type: application/json" \
  -d "{\"session_id\":\"s1\",\"text\":\"hello\"}"
```

Stage-7 验收：IntentGate `AgentScopeBackend(base_url="http://127.0.0.1:8090")` 联调。
