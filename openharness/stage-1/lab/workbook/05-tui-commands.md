# 实验 5：TUI 斜杠命令

## 步骤

1. 启动交互：`openh`（进入 TUI）
2. 依次尝试（以当前版本文档为准）：
   - `/skills` — 列出可用 Skills
   - `/plan` — 进入计划模式
   - `/resume` — 恢复会话（若有）
3. 触发一次 **权限对话框**（如让 Agent 写文件，观察 default 模式）

## 观察题

1. `/skills` 列出了哪些 skill？来源是 user 还是 project？
2. Plan 模式与 default 模式行为差异？
3. 权限拒绝时 Harness 返回给模型什么信息？

## 验收

- [ ] 文字记录或截图摘要写入 experiments/05-tui-notes.md
