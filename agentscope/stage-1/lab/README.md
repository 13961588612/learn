# Stage-1 Lab · P0 首个 Agent

> **手册**：[lab/manual/01-安装与配置.md](../../lab/manual/01-安装与配置.md) · [99-故障排查](../../lab/manual/99-故障排查索引.md)

## 前置

```bash
uv sync --group agentscope-core
cp ../../.env.example ../../.env   # 在 agentscope/ 下
```

## 实验

| # | 脚本 / 文档 | 内容 |
|---|-------------|------|
| 1 | [workbook/01-first-reply.md](workbook/01-first-reply.md) | 首次 `Agent.reply` |
| 2 | `scripts/01_first_reply.py` | 单轮问答 |
| 3 | `scripts/02_reply_stream_events.py` | 流式事件计数 |
| 4 | workbook | 手绘 Agent Loop |

## 运行

```bash
cd learn
uv run python agentscope/stage-1/lab/scripts/01_first_reply.py
```

## 验收

- [ ] 有 API Key 时 reply 成功
- [ ] experiments/ 有输出记录
- [ ] 能解释 Msg 与 reply 的关系
