# 阶段一：Harness 心智模型 + 本地跑通（P0）

> 对应 [`../../base/openharness/p0-harness-lab`](../../base/openharness/p0-harness-lab)

## 双轨学习

1. **概念脚本**（理解架构，无需 CLI）
2. **[lab/](stage-1/lab/README.md) 实操**（安装 `openharness-ai`、setup、dry-run、TUI）— **必做**

## 安装 CLI

```bash
cd learn
uv sync --group openharness-cli
openh setup
```

## 概念脚本

```bash
uv run python openharness/stage-1/01_harness_concepts.py
uv run python openharness/stage-1/10_stage1_final.py
```

## Lab

```bash
cd openharness/stage-1/lab
uv run python scripts/01_check_install.py
uv run python scripts/02_run_dry_run.py
uv run python scripts/03_run_stream_json.py
# 并完成 workbook/01~06 观察题
```

## P0 验收

- [ ] 概念：`10_stage1_final.py`
- [ ] **Lab**：dry-run 解读、profile 切换、stream-json、TUI 命令记录
- [ ] `lab/experiments/` 至少 3 条 CLI 记录

## 下一步

[stage-2.md](stage-2.md)
