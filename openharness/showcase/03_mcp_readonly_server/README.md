# 03_mcp_readonly_server · 只读工单 MCP

对应 **P2–P3** · [`../../base/openharness/p3-mcp-integration`](../../base/openharness/p3-mcp-integration)

## 运行（模拟模式）

```bash
uv run python openharness/showcase/03_mcp_readonly_server/server.py
```

## Harness 配置

复制 `config/servers.json.example` 到 OpenHarness MCP 配置目录，按官方文档注册。

## Tools（只读）

- `search_tickets` - 关键词搜索
- `get_ticket` - 按 ID 查询
