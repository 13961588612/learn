# Stage-2 Lab · P1 Tool / Skill / Permission 实操

> **查阅手册**：[07-Skills与权限](../../lab/manual/07-Skills与权限.md) · [03-TUI](../../lab/manual/03-TUI与斜杠命令.md) · [故障排查](../../lab/manual/99-故障排查索引.md)

## 实验

| # | 内容 | 命令 / 操作 |
|---|------|-------------|
| 1 | 安装 showcase Skills 到项目 | `mkdir .openharness/skills && cp -r ../../showcase/02_company_skills/skills/* .openharness/skills/` |
| 2 | TUI `/skills` 验证加载 | 交互 `openh`，输入 `/skills` |
| 3 | 调用 Skill | 在 TUI 中 `@incident-response` 或 slash 命令（以版本为准） |
| 4 | 权限实验 | 请求写 `/etc` 或 `.env`，观察 default 模式拦截 |
| 5 | Plan 模式 | 大任务前 `/plan`，对比是否先出计划 |
| 6 | 对接 showcase | 运行 [01_custom_tool_audit](../../showcase/01_custom_tool_audit/) 并在会话中测试 Tool 设计 |

## 脚本

```bash
uv run python scripts/01_install_skills.py
uv run python scripts/02_verify_skills_list.py
```

## 验收

- [ ] 3 个公司 Skill 可见
- [ ] 1 次写操作被 permission 或 Hook 拦截
- [ ] experiments/ 有记录
