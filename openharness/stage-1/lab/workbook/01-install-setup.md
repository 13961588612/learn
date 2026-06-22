# 实验 1：安装与 setup

## 步骤

1. 安装：`pip install openharness-ai` 或 `uv sync --group openharness-cli`
2. 检查版本：`openh --version`（Windows）或 `oh --version`
3. 初始化：`openh setup`，按提示配置至少一个 Provider
4. 运行：`uv run python scripts/01_check_install.py`

## 观察题（写入 experiments/01-install-notes.md）

1. setup 完成后配置目录在哪？（提示：`~/.openharness/`）
2. `--version` 输出中的版本号是多少？
3. 若 setup 失败，blocked 的 next action 是什么？

## 验收

- [ ] CLI 命令成功
- [ ] 已配置 API Key 或本地模型
