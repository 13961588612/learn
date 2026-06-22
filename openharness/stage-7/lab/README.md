# Stage-7 Lab · P6 部署与运维实操

> **查阅手册**：[11-部署运维与发布](../../lab/manual/11-部署运维与发布.md) · [故障排查](../../lab/manual/99-故障排查索引.md)

## 实验

| # | 内容 |
|---|------|
| 1 | 编写 Dockerfile / compose 生产清单（参考 base/p6-deploy-ops） |
| 2 | 配置健康检查端点与 MCP 探活 |
| 3 | 密钥：仅 K8s Secret / .env，禁止进镜像 |
| 4 | 发布 checklist：dry-run -> staging -> prod |
| 5 | 模拟 SRE 问答：MCP 超时、profile 失效 |

## 脚本

```bash
uv run python scripts/01_release_checklist.py
```

## 验收

- [ ] 运行手册 1 页纸 + 故障树
- [ ] 作品集含 Skills + MCP + Gateway demo
