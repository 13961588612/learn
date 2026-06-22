# OpenHarness 实操手册（Lab 总入口）

> **用途**：安装、CLI/TUI、配置、集成、运维的**查阅手册**；做 stage lab 时遇到问题时先查 [manual/99-故障排查索引.md](manual/99-故障排查索引.md)。

本目录与各 stage 的 `stage-N/lab/` **互补**：

| 类型 | 路径 | 作用 |
|------|------|------|
| **本手册** | `openharness/lab/manual/` | 命令速查、配置路径、故障树、按主题翻阅 |
| **阶段实验** | `stage-1/lab/` … `stage-7/lab/` | 按学习顺序动手 + workbook 观察题 |
| **概念脚本** | `stage-N/01_*.py` | Python 模拟理解机制 |
| **架构笔记** | [notes/harness-architecture.md](../notes/harness-architecture.md) | Engine / Loop 原理 |

---

## 快速开始（5 分钟）

```bash
cd learn
uv sync --group openharness-cli

openh --version          # Windows；Unix 用 oh
openh setup              # 配置 Provider / API Key
openh --dry-run          # 不调用模型、不执行 Tool

cd openharness/stage-1/lab
uv run python scripts/01_check_install.py
```

---

## 手册目录

| 章 | 文档 | 何时查阅 |
|----|------|----------|
| 1 | [安装与配置](manual/01-安装与配置.md) | 首次安装、目录结构、环境变量 |
| 2 | [CLI 命令速查](manual/02-CLI命令速查.md) | 忘记子命令、全局 flag |
| 3 | [TUI 与斜杠命令](manual/03-TUI与斜杠命令.md) | 交互模式、`/skills` `/plan` |
| 4 | [dry-run 与 readiness](manual/04-dry-run与readiness.md) | blocked / warning 含义 |
| 5 | [Provider 与 Profile](manual/05-Provider与Profile.md) | 多环境、Gateway URL |
| 6 | [输出格式与集成](manual/06-输出格式与集成.md) | json、stream-json、CI |
| 7 | [Skills 与权限](manual/07-Skills与权限.md) | SKILL.md、path_rules |
| 8 | [MCP 与 Plugin](manual/08-MCP与Plugin.md) | servers.json、plugin enable |
| 9 | [Memory 与 Multi-Agent](manual/09-Memory与Multi-Agent.md) | MEMORY.md、Task、max-turns |
| 10 | [Gateway 与程序化 API](manual/10-Gateway与程序化API.md) | 非 TUI 集成、Webhook |
| 11 | [部署运维与发布](manual/11-部署运维与发布.md) | compose、checklist、SRE |
| **99** | [**故障排查索引**](manual/99-故障排查索引.md) | **按现象查原因与修复** |

---

## 阶段 Lab 对照

| Stage | 实验目录 | 手册章节 |
|-------|----------|----------|
| 1 · P0 | [stage-1/lab](../stage-1/lab/README.md) | 1–4、6、3 |
| 2 · P1 | [stage-2/lab](../stage-2/lab/README.md) | 7 |
| 3 · P2 | [stage-3/lab](../stage-3/lab/README.md) | 8 |
| 4 · P3 | [stage-4/lab](../stage-4/lab/README.md) | 9 |
| 5 · P4 | [stage-5/lab](../stage-5/lab/README.md) | 6、10 |
| 6 · P5 | [stage-6/lab](../stage-6/lab/README.md) | 11 |
| 7 · P6 | [stage-7/lab](../stage-7/lab/README.md) | 11、99 |

---

## 实验记录约定

- 各 stage lab 的 `experiments/` 存放 CLI 输出 JSON（由 `_shared/cli.py` 辅助脚本生成）
- workbook 观察题答案写在 `experiments/*-notes.md`
- 手册中的命令可复制到项目根 `learn/` 或具体 lab 目录执行

---

## 相关链接

- [cli-lab-guide.md](../notes/cli-lab-guide.md) — Lab 流程说明
- [openharness/README.md](../README.md) — 七阶段学习路径
- [base/openharness/](../../../base/openharness/) — 14 周完整课表
