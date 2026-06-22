# Learn 文档中心

**Learn** 是**多轨道分阶段学习仓库**：根目录下各一级子目录为独立学习线（Python、LangChain、未来的 React/TS 等），工具链按轨道分离。

**项目路径**：`study/learn/`  
**子项目约定**：[tracks.md](tracks.md)

---

## 仓库结构

```
.                               # 项目根（study/learn）
├── README.md                   # 总入口、轨道索引
├── docs/
│   ├── README.md               # 本文件
│   └── tracks.md               # 多轨道与子项目约定
├── pyproject.toml              # Python 轨道共用（uv）
├── uv.lock
├── .python-version
├── python/                     # Python 语言学习
├── langchain/                  # LangChain / LangGraph
├── react/                      # （规划）React，自带 package.json
└── typescript/                 # （规划）TypeScript
```

---

## 文档与代码索引

| 路径 | 说明 | 状态 |
|------|------|------|
| [tracks.md](tracks.md) | 多轨道约定、新增子目录 checklist | 必读 |
| [../README.md](../README.md) | 总 README、轨道表、Python 快速开始 | 入口 |
| [../python/README.md](../python/README.md) | Python 分阶段目录清单 | 规划已定 |
| [../python/stage-1.md](../python/stage-1.md) | 阶段一：语言基础 | 可用 |
| [../python/stage-2.md](../python/stage-2.md) | 阶段二：面向对象与标准库 | 可用 |
| [../langchain/README.md](../langchain/README.md) | LangChain + LangGraph + DeepAgents 学习计划 | 可用 |
| [../langchain/stage-1.md](../langchain/stage-1.md) | 阶段一：LangChain 核心基础 | 可用 |
| [../openharness/README.md](../openharness/README.md) | OpenHarness 七阶段 + lab + showcase | 可用 |
| [../openharness/lab/README.md](../openharness/lab/README.md) | **OpenHarness 实操手册**（命令 / 配置 / 排错） | 必读 |
| [../openharness/stage-1.md](../openharness/stage-1.md) | P0 Harness 心智模型 + CLI Lab | 可用 |
| [../openharness/notes/cli-lab-guide.md](../openharness/notes/cli-lab-guide.md) | OpenHarness CLI/TUI 实验流程 | 必读 |
| [../agentscope/README.md](../agentscope/README.md) | AgentScope 七阶段 + lab + showcase | 可用 |
| [../agentscope/lab/README.md](../agentscope/lab/README.md) | AgentScope 实操手册 | 必读 |
| [../agentscope/stage-1.md](../agentscope/stage-1.md) | P0 Msg + Agent Loop | 可用 |
| [../copilotkit/README.md](../copilotkit/README.md) | CopilotKit 七阶段 + showcase | 可用 |

---

## 推荐阅读顺序

### 零基础 / Java 转 Python

1. `python/stage-1` → `python/stage-2`（待编写）  
2. `langchain/stage-1`  
3. `langchain/stage-2`  
4. `python/showcase`（待编写）→ 再进入外部实战项目

### 已有 Python，直接学智能体

1. `langchain/README.md` 通读  
2. `langchain/stage-1` 脚本按序运行  
3. `langchain/stage-2`  
4. 外部：[`../langchain/practice/aethermind`](../langchain/practice/aethermind)、[`../langchain/practice/intentgate`](../langchain/practice/intentgate)

### 速查

- Java 背景：`langchain/Java 程序员必备：Python 速查手册 (3).md`

---

## 快速开始（LangChain 轨道，当前最完整）

```bash
# 在项目根目录
uv sync

# 配置 API Key（编辑 langchain/stage-1/.env）
# OPENAI_API_KEY=sk-xxx

uv run python langchain/stage-1/01_chat_models.py
```

阶段二：

```bash
uv run python langchain/stage-2/01_state_graph_basics.py
```

---

## 环境要求

### Python 轨道（python/、langchain/）

| 项 | 版本 |
|----|------|
| Python | 3.11+（`.python-version`） |
| 包管理 | [uv](https://docs.astral.sh/uv/)（根 `pyproject.toml`） |
| LangChain | v1.2.x（dependency-group `langchain-stage-1`） |
| LangGraph | 0.4.x（dependency-group `langchain-stage-2`） |

API Key：至少配置一个 LLM Provider（见 `langchain/stage-1/.env`）。

### Node / TS 轨道（规划）

在对应子目录（如 `react/`）内使用 Node.js LTS + pnpm/npm，**无需**根目录 `uv sync`。详见 [tracks.md](tracks.md)。

---

## 与 langchain monorepo 的关系

本仓库侧重**学习与练习**；同级目录 [`../langchain/`](../langchain/) 中的**生产级实践**项目：

| 目录 | 关系 |
|------|------|
| [`../langchain/practice/aethermind/`](../langchain/practice/aethermind/) | 智能体平台实战，建议学完 langchain stage-1/2 后进入 |
| [`../langchain/practice/intentgate/`](../langchain/practice/intentgate/) | 多通道卡片网关，建议掌握 Python 异步 + FastAPI 后进入 |
| [`../langchain/docs/aethermind/`](../langchain/docs/aethermind/)、[`../langchain/docs/intentgate/`](../langchain/docs/intentgate/) | 上述项目的正式文档 |

---

## 项目 checklist

- [x] 将 `learn/` 提升为独立项目根，保留 `python/`、`langchain/` 子目录  
- [x] 根目录 `README.md` 指向 `docs/README.md`（本文件）  
- [x] 删除或忽略 `__pycache__`、`.env`（勿提交密钥）  
- [x] 依赖统一由根目录 `pyproject.toml` + `uv.lock` 管理（按阶段 dependency-groups）
- [x] 更新文档中的路径：`learn/langchain/...` → `langchain/...`  
- [x] 多轨道约定文档 [tracks.md](tracks.md)（Python 用 uv，Node/TS 子目录自治）

---

## 版本

| 版本 | 日期 | 说明 |
|------|------|------|
| 0.3.0 | 2026-06-21 | 明确多轨道结构；新增 tracks.md；Python 用 uv、Node 子目录自治 |
