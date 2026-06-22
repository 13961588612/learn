# 阶段一：LangChain 核心基础 - 学习指南

> **LangChain v1.2.x** · 使用最新 `create_agent` / `langchain.messages` / `langchain.tools` / `langchain-chroma`

## 项目结构总览

```
study/
├── learn/                              # ← 本学习项目（独立）
│   ├── README.md
│   ├── docs/README.md
│   ├── python/                         # Python 语言学习
│   └── langchain/                      # LangChain 学习
│       ├── README.md                   # 完整学习计划（4 阶段）
│       ├── stage-1.md                  # 当前文件：阶段一指南
│       ├── stage-2.md                  # 阶段二指南
│       ├── stage-1/                    # 阶段一：LangChain 练习
│       │   ├── .env                    # API Key 配置
│       │   ├── model.py                # 模型工厂
│       │   ├── 01_chat_models.py       # 多 Provider 模型切换
│       │   ├── ...                     # 02 ~ 11
│       │   └── 12_structured_output.py # 结构化输出
│       └── stage-2/                    # 阶段二：LangGraph 练习
│           ├── model.py
│           └── 01_...py ~ 10_...py
│
└── langchain/                          # ← 实践 monorepo
    └── practice/                       # 生产级实践项目
        ├── aethermind/                 # AetherMind 智能体平台
        └── intentgate/                 # IntentGate 多通道卡片网关
```

## 启动学习

```bash
# 1. 在项目根目录安装依赖
uv sync

# 2. 配置 API Key（至少配置一个）
# 编辑 langchain/stage-1/.env，填入:
#   OPENAI_API_KEY=sk-xxx
#   (可选) ANTHROPIC_API_KEY / GOOGLE_API_KEY

# 3. 按顺序运行练习
uv run python langchain/stage-1/01_chat_models.py
uv run python langchain/stage-1/02_prompt_templates.py
uv run python langchain/stage-1/03_tools.py
uv run python langchain/stage-1/04_chains_lcel.py
uv run python langchain/stage-1/05_memory.py
uv run python langchain/stage-1/06_rag.py
uv run python langchain/stage-1/07_callbacks.py
uv run python langchain/stage-1/08_streaming.py
uv run python langchain/stage-1/09_agent_final.py
uv run python langchain/stage-1/10_check_pointer.py
uv run python langchain/stage-1/11_stream_memory.py
uv run python langchain/stage-1/12_structured_output.py
```

## 练习脚本速览

| 编号 | 文件 | 核心知识点 | 需 API |
|------|------|-----------|:---:|
| 01 | `stage-1/01_chat_models.py` | `init_chat_model` 统一接口，支持 OpenAI / Anthropic / Google / Ollama 多 Provider 切换 | ✓ |
| 02 | `stage-1/02_prompt_templates.py` | ChatPromptTemplate / Few-shot prompting / MessagesPlaceholder / PipelinePrompt | 部分 |
| 03 | `stage-1/03_tools.py` | `@tool` 装饰器 / StructuredTool / `model.bind_tools()` 工具绑定 | 部分 |
| 04 | `stage-1/04_chains_lcel.py` | `\|` 管道操作符 / RunnableParallel 并行 / RunnablePassthrough 透传 / RunnableLambda 自定义函数 | ✓ |
| 05 | `stage-1/05_memory.py` | RunnableWithMessageHistory 历史管理 / SummaryMemory 摘要压缩 / trim_messages 智能裁剪 | 部分 |
| 06 | `stage-1/06_rag.py` | Document Loader → Text Splitter → Embeddings → VectorStore → Retriever → QA 完整链路 | ✓ |
| 07 | `stage-1/07_callbacks.py` | BaseCallbackHandler 自定义回调 / Token 计数 / LangSmith 全链路追踪 | ✓ |
| 08 | `stage-1/08_streaming.py` | `.stream()` / `.astream()` / `.astream_events()` / stream_mode 六种模式对比 | ✓ |
| 09 | `stage-1/09_agent_final.py` | **综合验收 (v1)**: `create_agent` + Checkpointer 记忆 + `stream_mode='updates'` | ✓ |
| 10 | `stage-1/10_check_pointer.py` | `InMemorySaver` / `SqliteSaver`、`get_state` / `update_state`、摘要写回、历史裁剪 | 部分 |
| 11 | `stage-1/11_stream_memory.py` | Agent + checkpointer + `stream_mode='messages'` 逐 token 流式多轮记忆 | ✓ |
| 12 | `stage-1/12_structured_output.py` | `with_structured_output` / `response_format` / Pydantic / ToolStrategy | ✓ |

## 学习目标

完成阶段一全部练习后，你将掌握 LangChain v1 的核心抽象：

- **Chat Models** — 用统一的 `init_chat_model` 接口调用任意 LLM（OpenAI/Claude/Gemini/Ollama）
- **Prompt Templates** — 结构化提示模板、Few-shot 少样本引导、对话历史动态注入
- **Tools** — 用 `@tool` 装饰器定义工具，让 LLM 自主选择调用
- **Chains (LCEL)** — 用 `|` 管道串联组件，并行执行，透传数据
- **Memory** — 对话历史管理（RunnableWithMessageHistory / checkpointer）、摘要压缩、智能裁剪
- **RAG** — 从文档加载到向量检索到增强生成的完整流水线
- **Callbacks** — 自定义回调监控耗时和 Token，集成 LangSmith 全链路追踪
- **Streaming** — 逐 Token 实时输出，6 种 stream_mode，支持 SSE/WebSocket 等场景

## 验收标准

能独立完成一个 **RAG + Tool Use + Memory** 的单智能体问答系统（使用 `create_agent` + `checkpointer` + `stream_mode`）。

## v1 vs 旧版本速查

| 旧写法 | v1 新写法 |
|--------|-----------|
| `langchain_core.messages.HumanMessage` | `langchain.messages.HumanMessage` |
| `langchain_core.tools.tool` | `langchain.tools.tool` |
| `langchain_core.callbacks.BaseCallbackHandler` | `langchain.callbacks.BaseCallbackHandler` |
| `langgraph.prebuilt.create_react_agent` | `langchain.agents.create_agent` |
| `langchain_community.vectorstores.Chroma` | `langchain_chroma.Chroma` |
| `RunnableWithMessageHistory` (Agent) | `checkpointer + thread_id` |
| `AgentExecutor` / 手写执行循环 | `create_agent` 自动处理 |
| `stream_mode='values'` only | `values` / `updates` / `messages` / `custom` / `debug` |

## 下一步

完成阶段一后，进入 [stage-2.md](stage-2.md) 学习 LangGraph 状态图编排。
