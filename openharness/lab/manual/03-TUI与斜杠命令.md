# 3 · TUI 与斜杠命令

[← 返回 Lab 总入口](../README.md)

---

## 3.1 进入 TUI

```bash
cd learn/openharness/stage-2/lab   # 若已安装 project skills
openh
```

TUI 适合：探索 Tool 选择、权限对话框、Skills、Plan 模式。  
自动化 / CI 用非交互 `-p`（见 [06-输出格式与集成.md](06-输出格式与集成.md)）。

---

## 3.2 常用斜杠命令

| 命令 | 用途 | Lab |
|------|------|-----|
| `/skills` | 列出已加载 Skills 及来源（user / project） | stage-1、2 |
| `/plan` | 进入计划模式，先出计划再执行 | stage-2 |
| `/resume` | 恢复上次会话（若有 thread 持久化） | stage-1、4、5 |
| `/help` | TUI 内置帮助 | — |

版本差异：以 TUI 内 `/help` 为准；手册列的是 lab 验收最低集合。

---

## 3.3 调用 Skill

方式因版本而异，常见：

1. 斜杠：`/incident-response`（Skill 名）
2. `@skill-name` 提及
3. 自然语言触发（依赖 SKILL.md 描述质量）

本仓库示例 Skills 位于：

```
learn/openharness/showcase/02_company_skills/skills/
├── incident-response/SKILL.md
├── release-checklist/SKILL.md
└── security-baseline/SKILL.md
```

安装到项目：

```bash
uv run python openharness/stage-2/lab/scripts/01_install_skills.py
# 等价：复制到 stage-2/lab/.openharness/skills/
```

在 **stage-2/lab 目录** 启动 `openh`，执行 `/skills` 应看到上述 3 个。

---

## 3.4 权限对话框（default 模式）

**实验步骤**（stage-2 lab）：

1. 确认 permission mode 为 `default`（非 auto）
2. 在 TUI 中让 Agent **写敏感路径**，例如：
   - 「请写入 `.env` 文件」
   - 「请修改 `/etc/hosts`」（Linux）或系统目录
3. 观察 Harness **拦截** 与返回给模型的错误信息

记录到 `experiments/05-tui-notes.md`（见 [stage-1 workbook](../../stage-1/lab/workbook/05-tui-commands.md)）。

---

## 3.5 Plan 模式 vs Default

| 模式 | 行为 | 适用 |
|------|------|------|
| **default** | 模型可直接发起 tool_use | 日常开发 |
| **plan** | 先输出计划，再逐步执行 | 大改动、发布、故障处理 |

对比实验：同一任务（如「整理 lab 目录并写 README」）分别用 default 与 `/plan` 执行，记录步骤差异。

---

## 3.6 TUI 记录模板

```markdown
# TUI 实验记录 — YYYY-MM-DD

## 环境
- openh 版本：
- cwd：
- profile：

## /skills
- 列出：
- 来源 user / project：

## 权限实验
- 请求操作：
- 结果：允许 / 拒绝
- 模型收到的反馈摘要：

## Plan vs Default
- 差异一句话：
```

---

## 3.7 对应实验

- [stage-1/lab/workbook/05-tui-commands.md](../../stage-1/lab/workbook/05-tui-commands.md)
- [stage-2/lab/README.md](../../stage-2/lab/README.md)
- 故障：[99-故障排查索引.md](99-故障排查索引.md) → 「/skills 为空」
