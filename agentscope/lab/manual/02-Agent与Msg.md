# 2 · Agent 与 Msg

## AgentScope 2.x

```python
from agentscope.agent import Agent
from agentscope.message import UserMsg

reply = await agent.reply(UserMsg("user", "你好"))
text = reply.get_text_content()
```

## reply vs reply_stream

| API | 用途 |
|-----|------|
| `reply()` | 集成同步、取最终 Msg |
| `reply_stream()` | Gateway SSE、统计 AgentEvent |

## Msg 规则

- 用户消息：`UserMsg(name, content)`
- 内容块：`TextBlock`、`ToolCallBlock` 等
- 多 Agent：用 `observe()` 共享上下文

[← 返回](../README.md)
