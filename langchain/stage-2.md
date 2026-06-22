# 阶段二：LangGraph 状态图编排 - 学习指南

> **LangGraph 0.4.x** · 基于 StateGraph 的有状态多步骤工作流

## 项目结构

```
.                         # 项目根（study/learn）
├── README.md
├── docs/README.md
├── python/
└── langchain/
    ├── README.md             # 完整学习计划（4 阶段）
    ├── stage-1.md            # 阶段一指南
    ├── stage-2.md            # 当前文件：阶段二指南
    ├── stage-1/              # 阶段一：LangChain 核心基础
    │   ├── .env
    │   ├── model.py
    │   └── 01_...py ~ 12_...py
    └── stage-2/              # 阶段二：LangGraph 状态图编排
        ├── .env.example
        ├── model.py
        └── 01_...py ~ 10_...py
```

## 启动学习

```bash
# 1. 在项目根目录（阶段一已 uv sync 可跳过）
uv sync

# 2. 配置 API Key（可从 stage-1 复制 .env）
copy langchain\stage-1\.env langchain\stage-2\.env

# 3. 按顺序运行练习
uv run python langchain/stage-2/01_state_graph_basics.py
uv run python langchain/stage-2/02_conditional_edges.py
uv run python langchain/stage-2/03_parallel_send.py
uv run python langchain/stage-2/04_checkpointing.py
uv run python langchain/stage-2/05_human_in_the_loop.py
uv run python langchain/stage-2/06_streaming.py
uv run python langchain/stage-2/07_subgraph.py
uv run python langchain/stage-2/08_supervisor_pattern.py
uv run python langchain/stage-2/09_map_reduce_pattern.py
uv run python langchain/stage-2/10_agent_final.py
```

## 练习脚本速览

| 编号 | 文件 | 核心知识点 | 需 API |
|------|------|-----------|:---:|
| 01 | `01_state_graph_basics.py` | StateGraph / Node / Edge / TypedDict State | |
| 02 | `02_conditional_edges.py` | add_conditional_edges / 规则路由 / LLM 路由 | 部分 |
| 03 | `03_parallel_send.py` | Send API 并行 fan-out / operator.add 聚合 | |
| 04 | `04_checkpointing.py` | MemorySaver / SqliteSaver / get_state / update_state | |
| 05 | `05_human_in_the_loop.py` | interrupt() / interrupt_before / Command(resume) | |
| 06 | `06_streaming.py` | stream_mode: values / updates / debug | |
| 07 | `07_subgraph.py` | 子图 compile 后嵌入主图 | |
| 08 | `08_supervisor_pattern.py` | Supervisor 调度多 Worker 循环协作 | ✓ |
| 09 | `09_map_reduce_pattern.py` | Map-Reduce: 分块 → 并行分析 → 汇总 | 部分 |
| 10 | `10_agent_final.py` | **综合验收**: 5 节点 + HITL + Checkpoint + Stream | 部分 |

## 学习目标

完成阶段二全部练习后，你将掌握 LangGraph 的核心编排能力：

- **StateGraph** — 用 TypedDict 定义状态，节点函数返回 partial update
- **条件路由** — add_conditional_edges 实现动态分支
- **并行执行** — Send API 实现 Map 阶段的 fan-out
- **Checkpointing** — 任意节点断点恢复，thread_id 会话隔离
- **Human-in-the-Loop** — interrupt 暂停等待人工，Command 恢复
- **Streaming** — 逐步观察图执行进度
- **Subgraph** — 模块化拆分复杂工作流
- **设计模式** — Supervisor / Map-Reduce 等经典 Agent 架构

## 验收标准

能设计并实现一个包含 **3+ 节点**的多步智能体工作流，支持 **人机协同** 和 **断点恢复**（见 `10_agent_final.py`）。

## 与阶段一的关系

| 阶段一 (LangChain) | 阶段二 (LangGraph) |
|-------------------|-------------------|
| LCEL Chain 管道 | StateGraph 有状态图 |
| create_agent 黑盒 | 手写节点 + 边，完全可控 |
| checkpointer + thread_id | 同样的 checkpoint 机制，更底层 |
| stream_mode='messages' | stream_mode='updates'/'values' |

`create_agent` 底层就是 LangGraph StateGraph；阶段二让你理解并手写这些编排逻辑。

## 推荐资源

| 资源 | 链接 |
|------|------|
| LangGraph 官方文档 | https://docs.langchain.com/oss/python/langgraph |
| Graph API 参考 | https://langchain-ai.github.io/langgraph/reference/graphs/ |
| Human-in-the-Loop | https://docs.langchain.com/oss/python/langgraph/interrupts |
