# Stage-1 Lab · P0 安装与 CLI 实操

> **查阅手册**：[lab/manual/01-安装与配置.md](../../lab/manual/01-安装与配置.md) · [04-dry-run](../../lab/manual/04-dry-run与readiness.md) · [故障排查](../../lab/manual/99-故障排查索引.md)

> **目标**：在本机跑通 OpenHarness，而不只读 Python 模拟代码。

## 前置

```bash
uv sync --group openharness-cli
openh setup          # 或 oh setup
```

## 实验顺序

| # | 文档 / 脚本 | 实操内容 | 验收 |
|---|-------------|----------|------|
| 1 | [workbook/01-install-setup.md](workbook/01-install-setup.md) | 安装、`--version`、`setup` | CLI 可用 |
| 2 | `scripts/01_check_install.py` | 自动检查并记录 | experiments 有 JSON |
| 3 | [workbook/02-dry-run.md](workbook/02-dry-run.md) | `openh --dry-run` | 能解释 readiness |
| 4 | `scripts/02_run_dry_run.py` | dry-run + json 输出 | |
| 5 | [workbook/03-provider-switch.md](workbook/03-provider-switch.md) | 配置 2 个 profile 并切换 | 同 prompt 换后端 |
| 6 | [workbook/04-stream-json.md](workbook/04-stream-json.md) | `-p ... --output-format stream-json` | 识别事件类型 |
| 7 | [workbook/05-tui-commands.md](workbook/05-tui-commands.md) | TUI：`/skills` `/plan` `/resume` | 文字记录 |
| 8 | [workbook/06-engine-reading.md](workbook/06-engine-reading.md) | 精读 engine/ Agent Loop | 手绘 while 循环 |

## 运行辅助脚本

```bash
cd learn/openharness/stage-1/lab
uv run python scripts/01_check_install.py
uv run python scripts/02_run_dry_run.py
uv run python scripts/03_run_stream_json.py
```

## P0 总验收

- [ ] 完成全部 workbook 观察题
- [ ] `experiments/` 至少 3 条 CLI 记录
- [ ] 能手绘 Agent Loop（不查阅代码）

## 下一步

[stage-2/lab](../stage-2/lab/README.md)
