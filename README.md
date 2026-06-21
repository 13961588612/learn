# Learn — 多轨道分阶段学习

面向 AI 应用 / 全栈工程的分阶段练习仓库：**按技术栈分目录**、**编号脚本循序渐进**、**阶段指南** + **专业示范**。

完整文档见 **[docs/README.md](docs/README.md)**；子项目约定见 **[docs/tracks.md](docs/tracks.md)**。

---

## 学习轨道

| 目录 | 说明 | 工具链 | 状态 |
|------|------|--------|------|
| [`python/`](python/README.md) | Python 语言、类型、异步、FastAPI、showcase | uv（根目录） | stage-1/2 可用 |
| [`langchain/`](langchain/README.md) | LangChain 核心 + LangGraph 编排 | uv（根目录） | stage-1/2 可用 |
| [`openharness/`](openharness/README.md) | OpenHarness Agent 后端 / Gateway | uv（根目录） | stage-1~4 + showcase 可用 |
| `react/` | React 前端（规划） | 子目录 `package.json` | 待建 |
| `typescript/` | TypeScript 基础（规划） | 子目录 `package.json` | 待建 |

各轨道**独立选学**；Python 类轨道共用根目录 `pyproject.toml`，Node/TS 类轨道在各自子目录内管理依赖。

---

## Python 轨道 · 快速开始（阶段一）

stage-1 / stage-2 **无需额外依赖**，标准库即可：

```bash
uv run python python/stage-1/01_hello_types.py
# 按编号至 09，详见 python/stage-1.md

uv run python python/stage-2/01_classes_basics.py
# 按编号至 09，详见 python/stage-2.md
```

---

## Python 轨道 · LangChain（阶段一）

```bash
# 在项目根目录（study/learn）
uv sync                          # 安装默认组 langchain-stage-1
# 编辑 langchain/stage-1/.env，填入 OPENAI_API_KEY 等

uv run python langchain/stage-1/01_chat_models.py
```

进入练习目录后也可：

```bash
cd langchain/stage-1
uv run python 01_chat_models.py
```

LangGraph 阶段二：

```bash
uv run python langchain/stage-2/01_state_graph_basics.py
```

仅学阶段二：`uv sync --group langchain-stage-2`

详见 [langchain/stage-1.md](langchain/stage-1.md)。

---

## OpenHarness 轨道 · 快速开始

```bash
uv sync --group openharness-stage-1   # 或 stage-2 / showcase

uv run python openharness/stage-1/01_harness_concepts.py
uv run python openharness/stage-1/10_stage1_final.py
```

专业示范见 [openharness/showcase/README.md](openharness/showcase/README.md)。  
完整 14 周课表见 [`../base/openharness/`](../base/openharness/)。

---

## Python 学习路径

```
python/stage-1 → stage-2 → stage-3 → stage-4 → showcase/
        ↓（已有 Python 可跳过）
langchain/stage-1 → stage-2 → （DeepAgents 见 langchain/README 阶段三）
        ↓
openharness/stage-1 → stage-4 → showcase/ → base/openharness P5–P6
```

---

## 仓库结构

```
.
├── README.md
├── docs/
│   ├── README.md       # 文档中心
│   └── tracks.md       # 多轨道 / 子项目约定
├── pyproject.toml      # Python 轨道共用（uv）
├── uv.lock
├── .python-version
├── python/             # Python 轨道
├── langchain/          # LangChain 轨道
├── openharness/        # OpenHarness 轨道
└── react/ …            # 未来 JS/TS 轨道（各自 package.json）
```

---

## 环境要求（按轨道）

| 轨道 | 要求 |
|------|------|
| Python / LangChain / OpenHarness | Python 3.11+、uv；LangChain 需 LLM Key；OpenHarness 可选 CLI |
| React / TS（规划） | Node.js LTS、pnpm 或 npm（在对应子目录安装） |

---

## 许可与说明

- 练习脚本仅供学习，`.env` 勿提交。
- 新增子目录请遵循 [docs/tracks.md](docs/tracks.md)。
