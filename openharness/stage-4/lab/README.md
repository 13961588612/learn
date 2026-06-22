# Stage-4 Lab · P3 Multi-Agent / Memory / Task 实操

> **查阅手册**：[09-Memory与Multi-Agent](../../lab/manual/09-Memory与Multi-Agent.md) · [故障排查](../../lab/manual/99-故障排查索引.md)

## 实验

| # | 内容 |
|---|------|
| 1 | 长会话：同一 thread 多轮 tool 调用，观察 context 增长 |
| 2 | MEMORY.md：在项目根创建 `.openharness/MEMORY.md`，重启会话验证跨会话记忆 |
| 3 | Coordinator：发起「调研 + 汇总」类任务，观察子 Agent / Task 输出 |
| 4 | `--max-turns 5` 熔断实验 |
| 5 | 与 LangGraph 对比笔记（workbook） |

## 脚本

```bash
uv run python scripts/01_seed_memory_md.py
uv run python scripts/02_max_turns_prompt.py
```

## 验收

- [ ] 子 Agent 或 Task 分工可演示
- [ ] MEMORY.md 被 Harness 读取（/resume 或新会话可见）
- [ ] max-turns 触发时有明确终止行为
