# 阶段三：类型系统、异步与数据建模 - 学习指南

> **Python 3.11+** · 依赖：`pydantic`、`pydantic-settings`、`httpx`

## 安装依赖

在项目根目录执行（不安装 LangChain 默认组）：

```bash
uv sync --no-default-groups --group python-stage-3
```

`uv run` 默认会同步 `default-groups`（当前为 `langchain-stage-1`）。若只想用 stage-3 环境，请加 `--no-default-groups`：

```bash
uv run --no-default-groups python python/stage-3/01_typing_basics.py
```

依赖安装到根目录 `.venv/`（见 [README.md](README.md) 依赖管理说明）。

## 启动学习

```bash
uv run python python/stage-3/01_typing_basics.py
# ... 按编号至 08
uv run python python/stage-3/08_stage3_final.py
```

`04_pydantic_settings.py` 可选配置：

```bash
cd python/stage-3
cp .env.example .env   # Windows: copy .env.example .env
uv run python 04_pydantic_settings.py
```

## 练习脚本速览

| 编号 | 文件 | 核心知识点 |
|------|------|-----------|
| 01 | `01_typing_basics.py` | Optional、Union、`X \| Y`、类型别名 |
| 02 | `02_typing_advanced.py` | Generic、Literal、TypedDict、Callable |
| 03 | `03_pydantic_models.py` | BaseModel、Field 校验、嵌套、`model_dump` |
| 04 | `04_pydantic_settings.py` | BaseSettings、`.env` 加载 |
| 05 | `05_async_basics.py` | `async`/`await`、`asyncio.gather` |
| 06 | `06_async_patterns.py` | 超时、取消、TaskGroup、`to_thread` |
| 07 | `07_httpx_async.py` | AsyncClient、MockTransport、重试 |
| 08 | `08_stage3_final.py` | **综合**：并发 API + Pydantic + JSON 报告 |

## 数据文件（08 综合练习）

```
stage-3/
├── data/
│   ├── api_scores.json      # 模拟「分数 API」
│   ├── api_activity.json    # 模拟「活跃 API」
│   └── report.json          # 运行 08 后生成
└── .env.example
```

## 验收标准

- [ ] 理解静态类型注解与 Pydantic 运行时校验的区别
- [ ] 能编写 `async def` 并用 `gather` 并发等待
- [ ] 能用 httpx 异步客户端请求（或 MockTransport 测试）
- [ ] 完成 `08_stage3_final.py` 并查看 `data/report.json`

## 下一步

[stage-4.md](stage-4.md)（pytest、FastAPI）或 [../langchain/stage-2.md](../langchain/stage-2.md)。
