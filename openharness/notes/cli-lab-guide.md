# OpenHarness CLI 实验（lab）— 使用练习说明

> **完整实操手册**（命令速查、配置路径、故障排查）：[`../lab/README.md`](../lab/README.md)  
> 遇问题先查：[`../lab/manual/99-故障排查索引.md`](../lab/manual/99-故障排查索引.md)

每个 stage 除 **概念脚本**（`01_*.py`）外，都有 **`lab/` 目录**：要求在已安装 `openharness-ai` 的本机 **真实操作 CLI/TUI**，并把观察记录到 `experiments/`。

## 通用流程

```bash
# 1. 安装 CLI（一次性）
cd learn
uv sync --group openharness-cli

# 2. 进入某阶段 lab
cd openharness/stage-1/lab

# 3. 按 README 顺序做实验 + 运行辅助脚本
uv run python scripts/01_check_install.py
uv run python scripts/02_run_dry_run.py
```

## 实验记录

- 每个 lab 脚本会在 `experiments/` 下生成 JSON（命令、输出摘要）
- _workbook_.md 中有**观察题**，请用中文填写到 `experiments/` 同名笔记

## Windows

PowerShell 中请使用 **`openh`**，避免与 `Out-Host` 别名冲突。

## 与 base/openharness 关系

| learn stage | base 项目 |
|-------------|-----------|
| stage-1 lab | p0-harness-lab |
| stage-2 lab | p1-custom-tool + p2-company-skills |
| stage-3 lab | p3-mcp-integration |
| stage-4 lab | p3-multi-agent-lab |
| stage-5 lab | p4-gateway-backend |
| stage-6 lab | p5-company-agent-platform |
| stage-7 lab | p6-deploy-ops |
