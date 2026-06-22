# 2 · CLI 命令速查

[← 返回 Lab 总入口](../README.md)

> 子命令以 `openh --help` 为准；下列为 lab 常用集合。

---

## 2.1 全局命令

| 命令 | 作用 |
|------|------|
| `openh --version` | 版本 |
| `openh --help` | 帮助 |
| `openh setup` | 初始化 / 配置 Provider |
| `openh --dry-run` | 环境自检，**不调用模型、不执行 Tool** |
| `openh` | 进入 **TUI** 交互模式 |
| `openh -p "..."` | **非交互** 单轮 prompt |
| `openh -p "..." --output-format json` | 非交互，单次 JSON 结果 |
| `openh -p "..." --output-format stream-json` | 非交互，流式 NDJSON 事件 |

---

## 2.2 dry-run 变体

```bash
openh --dry-run
openh --dry-run -p "Explain this repository" --output-format json
```

解读见 [04-dry-run与readiness.md](04-dry-run与readiness.md)。

---

## 2.3 Provider / Profile（名称以官方为准）

```bash
# 常见模式 — 若子命令不存在，用 setup 或编辑 profiles 目录
openh provider list
openh provider use <profile-name>
openh provider add <name> --provider openai --model gpt-4o ...
```

多环境示例见 [05-Provider与Profile.md](05-Provider与Profile.md)。

---

## 2.4 非交互集成常用 flag

```bash
openh -p "Reply with one word: pong" --output-format json
openh -p "List three files here" --output-format stream-json
openh -p "..." --max-turns 5          # 限制 Agent 轮数（若支持）
```

stage-5 lab 脚本：`stage-5/lab/scripts/01_noninteractive_json.py`

---

## 2.5 配置相关

```bash
openh config get <key>
openh config set <key> <value>
# 例：禁用不可信项目的 project skills
openh config set allow_project_skills false
```

---

## 2.6 Plugin（若版本提供）

```bash
openh plugin list
openh plugin enable <name>
openh plugin disable <name>
```

详见 [08-MCP与Plugin.md](08-MCP与Plugin.md)。

---

## 2.7 Gateway / ohmo（可选组件）

```bash
openh gateway --help    # 或 ohmo gateway — 以安装包为准
```

详见 [10-Gateway与程序化API.md](10-Gateway与程序化API.md)。  
探测脚本：`stage-5/lab/scripts/02_gateway_help_probe.py`

---

## 2.8 本仓库辅助脚本（统一从 learn 根执行）

```bash
cd learn
uv run python openharness/stage-1/lab/scripts/01_check_install.py
uv run python openharness/stage-1/lab/scripts/02_run_dry_run.py
uv run python openharness/stage-1/lab/scripts/03_run_stream_json.py
uv run python openharness/stage-2/lab/scripts/01_install_skills.py
uv run python openharness/stage-3/lab/scripts/01_mcp_dry_run.py
```

脚本通过 `_shared/cli.py` 自动选择 `openh` / `oh`，并将结果写入各 lab 的 `experiments/*.json`。

---

## 2.9 命令 → 阶段对照

| 你想做的事 | 优先命令 | Stage |
|------------|----------|-------|
| 检查环境 | `--dry-run` | 1 |
| 换模型后端 | `provider use` | 1 |
| 集成后端 API | `-p ... --output-format json/stream-json` | 1、5 |
| 公司流程 | TUI + Skills | 2 |
| 接内部系统 | MCP config + dry-run | 3 |
| 长会话 / 记忆 | MEMORY.md、max-turns | 4 |
| IM / Webhook | Gateway + showcase | 5–6 |
