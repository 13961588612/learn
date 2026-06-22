# 学习轨道与子项目约定

**Learn** 是一个**多轨道学习仓库**：根目录下每个一级子目录对应一条独立的学习线或技术栈，彼此工具链分离、文档自洽，可按需选学。

---

## 当前与规划中的轨道

| 目录 | 技术栈 | 包管理 / 工具 | 状态 |
|------|--------|---------------|------|
| [`python/`](../python/) | Python 语言与工程化 | 根目录 uv | stage-1/2 可用 |
| [`langchain/`](../langchain/) | LangChain / LangGraph | 同上 | stage-1/2 可用 |
| [`openharness/`](../openharness/) | OpenHarness Agent 后端 | 同上 | stage-1~4 可用 |
| `react/`（规划） | React 前端 | 子目录内 `package.json` + pnpm/npm | 待建 |
| `typescript/`（规划） | TypeScript 基础 | 子目录内 `package.json` + pnpm/npm | 待建 |

后续可在根目录继续增加其他子目录（如 `vue/`、`go/` 等），遵循下文约定即可。

---

## 目录约定

```
learn/                          # 仓库根（多轨道，非单一语言项目）
├── README.md                   # 总入口：轨道索引 + 各轨道快速开始
├── docs/
│   ├── README.md               # 文档中心
│   └── tracks.md               # 本文件：子项目约定
│
├── pyproject.toml              # 仅 Python 轨道共用
├── uv.lock
├── .python-version
│
├── python/                     # 轨道 A：自带 README、stage-N、showcase
├── langchain/                  # 轨道 B
├── react/                      # 轨道 C（未来）：自带 package.json、README
└── typescript/                 # 轨道 D（未来）
```

**原则**

1. **一级子目录 = 一条轨道**：不在根目录混放多种语言的练习脚本。
2. **工具链就近放置**：Python 共用根 `pyproject.toml`；Node/TS 各轨道在**自己的子目录**内维护 `package.json`（或 monorepo 时再评估是否用 pnpm workspace）。
3. **文档入口**：每个轨道根目录必须有 `README.md`；阶段指南用 `stage-N.md` 或子目录内 README。
4. **环境文件不提交**：各轨道的 `.env`、`.env.local` 仅本地使用，写入根 `.gitignore`。
5. **不强制统一运行时**：学 Python 只需 `uv`；学 React 只需进入 `react/` 安装 Node 依赖，无需 `uv sync`。

---

## Python 轨道（`python/`、`langchain/`）

- 依赖定义在根 [`pyproject.toml`](../pyproject.toml) 的 `[dependency-groups]`，按阶段命名，例如：
  - `langchain-stage-1`、`langchain-stage-2`
  - 未来 `python-stage-1`、`python-stage-4` 等
- 安装：`uv sync` 或 `uv sync --group <组名>`
- 运行：`uv run python <轨道>/stage-N/xx_script.py`

新增 Python 阶段时：在 `pyproject.toml` 增加 dependency-group，在对应轨道目录增加脚本与 `stage-N.md`，**不要**在子目录再放 `requirements.txt`。

---

## Node / TypeScript 轨道（规划，如 `react/`、`typescript/`）

建议在子目录内自包含，例如：

```
react/
├── README.md           # 本轨道学习计划与快速开始
├── package.json
├── pnpm-lock.yaml      # 或 package-lock.json
├── tsconfig.json
├── stage-1/
└── showcase/
```

- 安装与运行均在子目录内完成：

```bash
cd react
pnpm install
pnpm dev
```

- 若多个 JS 轨道共享依赖，可后续在根目录增加 `pnpm-workspace.yaml`，将 `react/`、`typescript/` 列为 workspace packages；**初期单轨道独立 `package.json` 即可**。

---

## 新增一条轨道的 checklist

- [ ] 在 `learn/` 下新建一级目录（如 `react/`）
- [ ] 编写该目录 `README.md`（目标、阶段、快速开始）
- [ ] 选用对应工具链配置文件（Python → 根 `pyproject.toml` 加 group；Node → 子目录 `package.json`）
- [ ] 在 [`docs/README.md`](README.md) 与根 [`README.md`](../README.md) 的轨道表中登记
- [ ] 确认根 [`.gitignore`](../.gitignore) 已覆盖该栈产物（如 `node_modules/`）

---

## 与外部实战项目

Python 智能体实战仍在 [`../langchain/practice/`](../langchain/practice/)（study 仓库内 sibling monorepo）。前端类实战若与 `react/` 轨道相关，可在该轨道 README 中链接到具体仓库或目录。
