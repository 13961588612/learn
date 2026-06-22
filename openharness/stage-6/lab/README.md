# Stage-6 Lab · P5 公司统一后端 MVP 实操

> **查阅手册**：[11-部署运维与发布](../../lab/manual/11-部署运维与发布.md) · [故障排查](../../lab/manual/99-故障排查索引.md)

## 实验

| # | 内容 |
|---|------|
| 1 | 阅读 [`../../base/openharness/docker-compose.yml`](../../base/openharness/docker-compose.yml) |
| 2 | 本地 `docker compose up -d`（Postgres 等，可选） |
| 3 | 整合 config + skills + MCP + audit 目录为一键启动脚本 |
| 4 | 新同事 30 分钟跑通 checklist（workbook） |
| 5 | 模拟 JWT onRequest（见 stage-5 gateway + 鉴权笔记） |

## 脚本

```bash
uv run python scripts/01_compose_checklist.py
```

## 验收

- [ ] 一条命令联调 Gateway + Harness + MCP（或文档等价流程）
- [ ] 审计日志可追踪完整 tool 链
