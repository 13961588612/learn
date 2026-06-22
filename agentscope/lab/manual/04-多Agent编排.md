# 4 · 多 Agent 编排

## 顺序 Handoff（2.x 推荐）

```python
msg_a = await researcher.reply(UserMsg("user", task))
await writer.observe(msg_a)
msg_b = await writer.reply(None)
```

## 模式

| 模式 | 说明 |
|------|------|
| sequential | A -> B -> C |
| specialist | 路由到专家 Agent |
| critic | 生成 + 审查 |

示例：`showcase/02_multi_agent_handoff/pipeline.py`

[← 返回](../README.md)
