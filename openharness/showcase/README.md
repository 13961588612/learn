# OpenHarness 专业示范

对应 [`../../base/openharness/`](../../base/openharness/) P1–P5 项目骨架的可运行精简版。

| 目录 | 阶段 | 说明 |
|------|------|------|
| [01_custom_tool_audit/](01_custom_tool_audit/) | P1 | 只读 Tool + 审计 Hook + 测试 |
| [02_company_skills/](02_company_skills/) | P2 | 3 个 SKILL.md |
| [03_mcp_readonly_server/](03_mcp_readonly_server/) | P2–P3 | stdio JSON-RPC 工单 MCP |
| [04_gateway_webhook/](04_gateway_webhook/) | P4–P5 | FastAPI Webhook + stream 模拟 |

## 依赖

```bash
uv sync --group openharness-showcase
```

## 学习顺序

stage-1 → stage-2 → **01, 02** → stage-3 → **03** → stage-4 → **04** → base/openharness P5–P6
