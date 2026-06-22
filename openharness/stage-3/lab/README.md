# Stage-3 Lab · P2 MCP + Plugin 实操

> **查阅手册**：[08-MCP与Plugin](../../lab/manual/08-MCP与Plugin.md) · [04-dry-run](../../lab/manual/04-dry-run与readiness.md) · [故障排查](../../lab/manual/99-故障排查索引.md)

## 实验

| # | 内容 |
|---|------|
| 1 | 配置 MCP：复制 `showcase/03_mcp_readonly_server/config/servers.json.example` 到 Harness MCP 配置目录 |
| 2 | `openh --dry-run` 检查 MCP readiness |
| 3 | 在会话中调用 `search_tickets` / `get_ticket` |
| 4 | 安装官方 plugin（如 security-guidance），`plugin enable` |
| 5 | 阅读 plugin Hook 源码并记录 |

## 脚本

```bash
uv run python scripts/01_mcp_dry_run.py
uv run python scripts/02_print_mcp_config_example.py
```

## 验收

- [ ] MCP Tool 在 Harness 可调且只读
- [ ] dry-run 能发现 MCP 配置错误
- [ ] 至少 1 个 plugin 启用记录
