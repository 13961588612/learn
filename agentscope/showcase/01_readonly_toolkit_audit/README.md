# Showcase 01 · 只读 Tool + 审计 Middleware

P1 专业示范：FunctionTool + `AuditMiddleware` + 结构化 docstring。

```bash
cd learn
uv sync --group agentscope-core
uv run python agentscope/showcase/01_readonly_toolkit_audit/run_agent.py
```

## 结构

```
01_readonly_toolkit_audit/
├── src/tools/internal_docs.py
├── run_agent.py
├── audit_logs/          # 运行时生成
└── tests/test_tool.py
```

## 验收

- [ ] Tool 被模型选中（有 API 时）
- [ ] `audit_logs/*.jsonl` 有 tool 记录
