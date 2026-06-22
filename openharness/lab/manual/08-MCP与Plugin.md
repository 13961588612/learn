# 8 · MCP 与 Plugin

[← 返回 Lab 总入口](../README.md)

---

## 8.1 MCP 在 Harness 中的角色

**MCP（Model Context Protocol）** = 把外部系统（工单、文档、数据库只读视图）以 **Tool** 形式接到 Agent。

公司后端推荐：**只读 MCP 优先**；读写分 server。

---

## 8.2 配置位置

通常合并到用户级 OpenHarness 配置（具体文件名以官方文档为准）：

```
~/.openharness/
└── mcp/servers.json    # 或 settings 内 mcpServers 字段
```

本仓库示例：

```
learn/openharness/showcase/03_mcp_readonly_server/config/servers.json.example
```

打印示例：

```bash
cd learn
uv run python openharness/stage-3/lab/scripts/02_print_mcp_config_example.py
```

---

## 8.3 示例 servers.json

```json
{
  "mcpServers": {
    "company-tickets": {
      "command": "uv",
      "args": [
        "run",
        "python",
        "openharness/showcase/03_mcp_readonly_server/server.py"
      ],
      "env": {}
    }
  }
}
```

**注意**：

- `command` / `args` 的 cwd 通常是启动 `openh` 时的目录 → lab 中建议 **`cd learn`** 再启动
- Windows 路径可用正斜杠或转义反斜杠
- 改配置后重新 `openh --dry-run` 验证

---

## 8.4 dry-run 验证 MCP

```bash
cd learn
openh --dry-run
uv run python openharness/stage-3/lab/scripts/01_mcp_dry_run.py
```

blocked 时查看 next actions：常见为 command 找不到、server 启动超时、JSON schema 错误。

---

## 8.5 会话中调用 MCP Tool

1. 配置好 server 且 dry-run ready
2. `openh` 进入 TUI（cwd = `learn`）
3. Prompt 示例：
   - 「用 search_tickets 查 open 状态的工单」
   - 「get_ticket  id=TK-001」

Tool 名以 server 注册为准（见 [server.py](../../showcase/03_mcp_readonly_server/server.py)）。

Demo 模式（不启 stdio）：

```bash
uv run python openharness/showcase/03_mcp_readonly_server/server.py
# 加 --stdio 才走 MCP stdio 协议
```

---

## 8.6 Plugin

官方 Plugin（如 security-guidance）扩展 Hook / 提示：

```bash
openh plugin list
openh plugin enable <name>
```

实验：启用后重复一次「尝试写敏感文件」，对比 Hook 行为差异。

---

## 8.7 安全基线

| 规则 | 原因 |
|------|------|
| MCP 只读 | 降低 Agent 误写生产数据 |
| dry-run 必过 | 避免上线后才发现 server 起不来 |
| 超时与 reconnect | Harness 有 reconnect；业务侧仍要设 timeout |
| 独立 server | 读工单 vs 写工单分进程 |

---

## 8.8 对应实验

- [stage-3/lab/README.md](../../stage-3/lab/README.md)
- [showcase/03_mcp_readonly_server](../../showcase/03_mcp_readonly_server/README.md)
- base：[p3-mcp-integration](../../../../base/openharness/p3-mcp-integration/README.md)
- 故障：[99-故障排查索引.md](99-故障排查索引.md) → 「MCP server 启动失败」
