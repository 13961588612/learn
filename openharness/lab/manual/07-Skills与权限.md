# 7 · Skills 与权限

[← 返回 Lab 总入口](../README.md)

---

## 7.1 Skills 是什么

Skills = 组织级 **SKILL.md** 流程文档，Harness 注入上下文，供模型按公司规范行事。

与 Tool 区别：

| | Skill | Tool |
|---|-------|------|
| 本质 | 知识与流程 | 可执行能力 |
| 格式 | `skills/<name>/SKILL.md` | Python / MCP function |
| 典型 | 发布 checklist、故障 Runbook | 查库、写文件 |

---

## 7.2 目录结构

```
.openharness/skills/
└── incident-response/
    └── SKILL.md
```

SKILL.md 应包含：何时触发、步骤、禁止事项、相关联系人/链接（示例见 showcase）。

---

## 7.3 安装本仓库示例 Skills

```bash
cd learn
uv run python openharness/stage-2/lab/scripts/01_install_skills.py
cd openharness/stage-2/lab
openh
/skills
```

验证脚本（探测 CLI help + 提示 TUI 记录）：

```bash
uv run python openharness/stage-2/lab/scripts/02_verify_skills_list.py
```

---

## 7.4 权限 permission

### 模式

| mode | 行为 | 环境 |
|------|------|------|
| **default** | 敏感操作弹窗 / 规则拦截 | 开发、staging、**生产推荐** |
| **plan** | 先计划后执行 | 大变更 |
| **auto** | 少拦截 | **仅本地实验**；生产禁止 |

### settings.json 片段

```json
{
  "permission": {
    "mode": "default",
    "path_rules": [
      {"pattern": "/etc/*", "allow": false},
      {"pattern": "~/.ssh/*", "allow": false},
      {"pattern": "**/.env", "allow": false}
    ],
    "denied_commands": ["rm -rf", "DROP TABLE"]
  }
}
```

位置：用户级 `~/.openharness/settings.json` 或项目 `.openharness/settings.json`。

---

## 7.5 Hook 与审计（概念 → showcase）

PostToolUse Hook 是**审计主挂载点**（见 showcase `01_custom_tool_audit`）：

```
tool 调用 → permission → pre_hook → execute → post_hook → audit log
```

生产要求：写操作必须 PostToolUse；参数摘要 + 脱敏。

---

## 7.6 公司 Skills 治理

- 独立 Git 仓库 + tag 发布
- 不可信仓库：`openh config set allow_project_skills false`
- 用户调用：`/skill-name` 或 `@skill-name`

---

## 7.7 实验清单（stage-2）

- [ ] 3 个 showcase Skills 在 `/skills` 可见
- [ ] 触发 `incident-response` 类 Skill 一次
- [ ] 写 `.env` 或系统路径被拦截
- [ ] `/plan` 与 default 行为对比
- [ ] 对接 [01_custom_tool_audit](../../showcase/01_custom_tool_audit/)

---

## 7.8 对应实验

- [stage-2/lab/README.md](../../stage-2/lab/README.md)
- [showcase/02_company_skills](../../showcase/02_company_skills/README.md)
- 故障：[99-故障排查索引.md](99-故障排查索引.md) → 「Skills 不显示」「权限不生效」
