# Python 分阶段学习与专业示范 — 目录清单

> **定位**：面向已有编程经验（尤其 Java 背景）、目标从事 AI 应用 / 后端工程的学习路径。  
> **组织方式**：对齐 `langchain/` — 总览 README + 各阶段 `stage-N.md` + `stage-N/` 编号练习脚本 + 独立 `showcase/` 综合示范。

**Python 版本**：3.11+（与 [`../langchain/practice/aethermind`](../langchain/practice/aethermind)、[`../langchain/practice/intentgate`](../langchain/practice/intentgate) 一致）

**依赖管理**：Python 轨道共用根目录 [uv](https://docs.astral.sh/uv/) + `pyproject.toml` 的 `dependency-groups`（各阶段编写时在根 `pyproject.toml` 增加 `python-stage-N` 组）。Node/TS 类轨道不在此管理，见 [../docs/tracks.md](../docs/tracks.md)。

---

## 1. 顶层目录结构（规划）

```
python/
├── README.md                 # 本文件：总学习计划、能力画像、阶段索引
├── stage-1.md                  # 阶段一学习指南
├── stage-2.md                  # 阶段二学习指南
├── stage-3.md                  # 阶段三学习指南
├── stage-4.md                  # 阶段四学习指南
├── showcase.md                 # 专业示范总览与运行说明
│
├── stage-1/                    # 阶段一：语言基础与编码习惯
│   ├── README.md               # 本阶段速查与运行顺序（可选，与 stage-1.md 互补）
│   └── 01_*.py ~ 09_*.py
│
├── stage-2/                    # 阶段二：面向对象与标准库
│   └── 01_*.py ~ 09_*.py
│
├── stage-3/                    # 阶段三：类型系统、异步与数据建模
│   ├── .env.example
│   └── 01_*.py ~ 08_*.py
│
├── stage-4/                    # 阶段四：测试、工程化与 Web 入门
│   ├── .env.example
│   └── 01_*.py ~ 09_*.py
│
└── showcase/                 # 专业示范（小项目级，非单文件脚本）
    ├── README.md
    ├── 01_cli_task_manager/    # Typer CLI + 持久化
    ├── 02_fastapi_notes_api/   # FastAPI + Pydantic + SQLite
    └── 03_async_worker/        # asyncio 队列 + 后台任务
```

**与 langchain 学习路径的关系**：

| 学完 Python 阶段 | 可顺畅进入 |
|------------------|------------|
| stage-1 ~ 2 | `langchain/stage-1` |
| stage-3 ~ 4 | `langchain/stage-2`、[`../langchain/practice/intentgate`](../langchain/practice/intentgate) |
| showcase | [`../langchain/practice/aethermind`](../langchain/practice/aethermind) 工程结构 |

---

## 2. 阶段总览

| 阶段 | 目录 | 周期（建议） | 目标 | 验收 |
|------|------|--------------|------|------|
| 一 | `stage-1/` | 第 1–2 周 | 语法、类型、函数、集合、文件、异常、导入 | 独立完成带文件读写的数据处理脚本 |
| 二 | `stage-2/` | 第 3–4 周 | 类、继承、装饰器、迭代器、标准库 | 实现小型可复用模块包 |
| 三 | `stage-3/` | 第 5–6 周 | typing、Pydantic、async/await、httpx | 异步拉取 API 并校验为结构化模型 |
| 四 | `stage-4/` | 第 7–8 周 | pytest、日志、配置、FastAPI 基础 | 带测试的迷你 REST 服务 |
| 示范 | `showcase/` | 第 9–10 周 | 接近生产的目录与分层 | 3 个可演示的小项目 |

---

## 3. 阶段一：`stage-1/` — 语言基础与编码习惯

| 编号 | 文件（规划） | 主题 |
|------|----------------|------|
| 01 | `01_hello_types.py` | 变量、基本类型、`is` vs `==`、f-string |
| 02 | `02_control_flow.py` | if/for/while、match（3.10+）、布尔与真值 |
| 03 | `03_functions.py` | 参数默认值、`*args`/`**kwargs`、lambda、作用域 |
| 04 | `04_collections.py` | list/dict/set/tuple、常用方法、浅拷贝 |
| 05 | `05_comprehensions.py` | 列表/字典推导、生成器表达式、`yield` 入门 |
| 06 | `06_files_paths.py` | `open`、`pathlib` 读写、编码 UTF-8 |
| 07 | `07_exceptions.py` | try/except/else/finally、自定义异常、EAFP |
| 08 | `08_imports_modules.py` | `import` 规则、`__name__`、虚拟环境概念 |
| 09 | `09_stage1_final.py` | **综合**：读 CSV/JSON → 聚合统计 → 写结果文件 |

**依赖**：无第三方包（仅标准库）。

---

## 4. 阶段二：`stage-2/` — 面向对象与标准库

| 编号 | 文件（规划） | 主题 |
|------|----------------|------|
| 01 | `01_classes_basics.py` | 类、实例、`@classmethod` / `@staticmethod` |
| 02 | `02_inheritance.py` | 继承、多态、`super()`、抽象基类 `abc` |
| 03 | `03_dataclass_enum.py` | `dataclasses`、`Enum`、`NamedTuple` |
| 04 | `04_properties_protocol.py` | `@property`、描述符入门、`Protocol` 预览 |
| 05 | `05_iterators_context.py` | 迭代器、`with`、上下文管理器、`contextlib` |
| 06 | `06_decorators.py` | 函数装饰器、带参装饰器、 functools |
| 07 | `07_stdlib_json_datetime.py` | `json`、`datetime`、`zoneinfo` |
| 08 | `08_stdlib_os_subprocess.py` | `os`、`pathlib` 进阶、`subprocess` 安全调用 |
| 09 | `09_stage2_final.py` | **综合**：小型 `notes` 包（类 + JSON 持久化） |

**依赖**：标准库为主。

---

## 5. 阶段三：`stage-3/` — 类型系统、异步与数据建模

| 编号 | 文件（规划） | 主题 |
|------|----------------|------|
| 01 | `01_typing_basics.py` | `Optional`、`Union`、类型别名、`mypy` 概念 |
| 02 | `02_typing_advanced.py` | `Generic`、`Literal`、`TypedDict`、`Callable` |
| 03 | `03_pydantic_models.py` | `BaseModel`、校验、嵌套模型、`model_dump` |
| 04 | `04_pydantic_settings.py` | `pydantic-settings`、`.env` 配置类 |
| 05 | `05_async_basics.py` | `async def`、`await`、`asyncio.gather` |
| 06 | `06_async_patterns.py` | 超时、取消、`TaskGroup`、与线程对比 |
| 07 | `07_httpx_async.py` | `httpx` 异步客户端、重试、超时 |
| 08 | `08_stage3_final.py` | **综合**：并发拉取多个 API → Pydantic 校验 → 汇总报告 |

**依赖（规划）**：`pydantic`、`pydantic-settings`、`httpx`。

---

## 6. 阶段四：`stage-4/` — 测试、工程化与 Web 入门

| 编号 | 文件（规划） | 主题 |
|------|----------------|------|
| 01 | `01_pytest_basics.py` | 用例、`assert`、参数化 |
| 02 | `02_pytest_fixtures.py` | fixture、conftest、临时目录 |
| 03 | `03_logging.py` | `logging` 层级、结构化字段、不与 print 混用 |
| 04 | `04_project_layout.py` | 包布局、`pyproject.toml`、可编辑安装概念 |
| 05 | `05_fastapi_hello.py` | 路由、请求体、`HTTPException` |
| 06 | `06_fastapi_dependencies.py` | `Depends`、生命周期、依赖注入 |
| 07 | `07_fastapi_pydantic_api.py` | 响应模型、OpenAPI、状态码 |
| 08 | `08_testing_fastapi.py` | `TestClient`、集成测试 |
| 09 | `09_stage4_final.py` | **综合**：带 CRUD + pytest 的迷你 API 单文件版 |

**依赖（规划）**：`pytest`、`fastapi`、`uvicorn`、`httpx`（TestClient）。

---

## 7. 专业示范：`showcase/` — 小项目级示范

每个子目录为**可独立运行**的小工程，目录内自带 `README.md`；依赖在根 `pyproject.toml` 对应 `python-showcase-*` 组（或 showcase 子目录内独立 `pyproject.toml`）。

| 目录 | 名称 | 示范要点 | 对标工程能力 |
|------|------|----------|--------------|
| `01_cli_task_manager/` | 命令行任务管理 | Typer/argparse、子命令、JSON 存储、错误提示 | 脚本与运维工具 |
| `02_fastapi_notes_api/` | 笔记 REST 服务 | 分层（api/schemas/service）、SQLite、Pydantic v2 | `intentgate` / `aethermind` API 风格 |
| `03_async_worker/` | 异步任务 Worker | `asyncio.Queue`、后台消费、优雅退出、日志 | Agent 网关、长连接侧车任务 |

**showcase 内建议结构（以 `02_fastapi_notes_api/` 为例）**：

```
02_fastapi_notes_api/
├── README.md
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   ├── service.py
│   └── db.py
└── tests/
    └── test_api.py
```

---

## 8. 文档文件说明

| 文件 | 作用 |
|------|------|
| `README.md` | 全阶段学习计划、能力画像、与 langchain/practice 的衔接 |
| `stage-N.md` | 对应阶段的详细指南、知识点勾选、运行命令（对齐 `langchain/stage-1.md`） |
| `showcase.md` | 三个示范项目的学习目标、演示步骤、扩展作业 |
| `stage-N/README.md` | 可选：仅本阶段脚本索引表（避免 stage-N.md 过长） |

---

## 9. 实施顺序（后续开发）

1. **P0**：创建 `stage-1/` ~ `stage-4/`、`showcase/` 空目录 + 在根 `pyproject.toml` 添加 `python-stage-N` dependency-groups 占位  
2. **P1**：`stage-1` 全套脚本 + `stage-1.md`  
3. **P2**：`stage-2`、`stage-3`  
4. **P3**：`stage-4`  
5. **P4**：`showcase/` 三个小项目  

---

## 10. 当前状态

| 块 | 状态 |
|----|------|
| 目录清单（本文） | ✅ 已确定 |
| `stage-1/` 代码 + `stage-1.md` | ✅ 可用 |
| `stage-2/` 代码 + `stage-2.md` | ✅ 可用 |
| `stage-3/` 代码 + `stage-3.md` | ✅ 可用 |
| `stage-4/` 代码 | ⬜ 待编写 |
| `showcase/` 示范工程 | ⬜ 待编写 |
| `stage-4.md` | ⬜ 待编写 |

---

## 版本

| 版本 | 日期 | 说明 |
|------|------|------|
| 0.3.0 | 2026-06-28 | stage-3 练习脚本与指南（typing、Pydantic、async、httpx） |
| 0.2.0 | 2026-06-21 | stage-1 / stage-2 练习脚本与指南 |
