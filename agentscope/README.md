# AgentScope 多智能体框架学习计划

> **AgentScope 2.x**（阿里通义实验室）— Python 异步多 Agent 运行时。  
> 本轨道 = **概念脚本**（机制模拟 + API 实验）+ **Lab 实操** + **Showcase 二开**。

**版本**：本仓库练习基于 **`agentscope>=2.0`**（统一 `Agent` 类，非旧版 `ReActAgent`）。  
**实操手册**：[lab/README.md](lab/README.md) · [故障排查](lab/manual/99-故障排查索引.md)  
**延伸课表**：[../../base/agentscope/](../../base/agentscope/)（P0–P6 项目骨架）

---

## 为何 7 个阶段？

| Stage | 主题 | 概念脚本 | Lab / Showcase |
|-------|------|----------|----------------|
| **1** | P0 架构 · Msg · Agent Loop | 四层模块、Msg 块、事件流 | 首个 `Agent.reply` |
| **2** | P1 Toolkit · Middleware · 权限 | FunctionTool、审计 Hook | 只读 Tool + audit |
| **3** | P2 Model · State · 压缩 | 多 Provider、AgentState | 切换 OpenAI / DashScope |
| **4** | P3 多 Agent · Skills | 顺序 handoff、Skill 目录 | 双 Agent 协作 |
| **5** | P4 MCP · 结构化输出 | MCPClient、StructuredResponse | 只读 MCP |
| **6** | P5 Tracing · Bridge 原型 | OpenTelemetry、FastAPI 契约 | 本地 Bridge 冒烟 |
| **7** | P6 IntentGate 二开 | SSE 协议、会话路由 | 对接 IntentGate 适配器 |

---

## 快速开始

```bash
cd learn
uv sync --group agentscope-core

cp agentscope/.env.example agentscope/.env
# 填写 OPENAI_API_KEY 或 DASHSCOPE_API_KEY

uv run python agentscope/stage-1/01_agentscope_concepts.py
uv run python agentscope/stage-1/lab/scripts/01_first_reply.py
```

---

## 学习路径（双轨）

```
每个 Stage:
  01~N 概念脚本  →  lab/scripts + workbook  →  （可选）showcase/
```

---

## Stage 1 · P0 心智模型

| 类型 | 路径 |
|------|------|
| 指南 | [stage-1.md](stage-1.md) |
| 概念 | `stage-1/01` ~ `06` |
| Lab | [stage-1/lab/](stage-1/lab/README.md) |

---

## Stage 2 · P1 Tool / Middleware

| 类型 | 路径 |
|------|------|
| 指南 | [stage-2.md](stage-2.md) |
| Showcase | [showcase/01_readonly_toolkit_audit](showcase/01_readonly_toolkit_audit/) |

---

## Stage 3 · P2 Model / State

[stage-3.md](stage-3.md) · `stage-3/` · [lab/](stage-3/lab/README.md)

---

## Stage 4 · P3 Multi-Agent / Skills

[stage-4.md](stage-4.md) · [showcase/02_multi_agent_handoff](showcase/02_multi_agent_handoff/)

---

## Stage 5 · P4 MCP / Structured Output

[stage-5.md](stage-5.md) · [showcase/03_mcp_internal_api](showcase/03_mcp_internal_api/)

---

## Stage 6 · P5 Tracing / Bridge

[stage-6.md](stage-6.md)

---

## Stage 7 · P6 IntentGate 二开 Capstone

[stage-7.md](stage-7.md) · [showcase/04_intentgate_bridge](showcase/04_intentgate_bridge/)

---

## 依赖组（uv）

| 组 | 用途 |
|----|------|
| `agentscope-core` | `agentscope>=2.0` + dotenv，全阶段 |
| `agentscope-showcase` | FastAPI Bridge + httpx |

---

## 与兄弟轨道分工

| 轨道 | 定位 |
|------|------|
| `langchain/` | 业务编排图、LangGraph |
| `openharness/` | Harness 运行时、Gateway 治理 |
| `agentscope/` | **多 Agent 框架**、Toolkit、MCP、Bridge 二开 |
| `copilotkit/` | Web 客户端、A2UI |

推荐顺序：`python` → `langchain/stage-1` → **`agentscope/stage-1~7`** → `openharness` 或 IntentGate capstone。
