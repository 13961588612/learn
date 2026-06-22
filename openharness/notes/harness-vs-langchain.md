# OpenHarness ↔ LangChain 对照

> 详细版：[`../../base/openharness/notes/harness-vs-langchain-map.md`](../../base/openharness/notes/harness-vs-langchain-map.md)

| LangChain / LangGraph | OpenHarness | 关键差异 |
|----------------------|-------------|----------|
| `@tool` / StructuredTool | 内置 Tool + 自定义 Tool + MCP Tool | Harness 统一 Tool Registry |
| System Prompt | CLAUDE.md + prompts 组装 | 多层 prompt 来源 |
| DeepAgents `skills/` | `.openharness/skills/` SKILL.md | 同为 Markdown 目录规范 |
| LangGraph StateGraph | coordinator / Task | 图在应用层 vs 运行时协调 |
| Memory / Checkpointer | MEMORY.md + Auto-Compaction | 跨会话文件 vs 图状态 |
| FastAPI 自建 Gateway | ohmo + stream-json | Harness 自带通道扩展点 |

## 互补路径

```
LangChain Tool  ──包装为──▶  MCP Server  ──注册到──▶  OpenHarness
LangGraph 复杂子流程  ──下沉为──▶  MCP / 独立服务  ──▶  Harness 调用
```

## 何时用哪个

- **LangChain**：RAG、LCEL、LangGraph 业务编排、DeepAgents
- **OpenHarness**：统一 CLI/Gateway、Tool 治理、Skills 发布、权限审计、MCP 接入
