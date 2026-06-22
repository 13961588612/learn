# 阶段一：语言基础与编码习惯 - 学习指南

> **Python 3.11+** · 仅标准库 · 面向有 Java 等编程经验的学习者

## 启动学习

stage-1 **无需额外依赖**，在项目根目录直接运行：

```bash
uv run python python/stage-1/01_hello_types.py
uv run python python/stage-1/02_control_flow.py
# ... 按编号顺序至 09
uv run python python/stage-1/09_stage1_final.py
```

或进入目录：

```bash
cd python/stage-1
uv run python 01_hello_types.py
```

## 练习脚本速览

| 编号 | 文件 | 核心知识点 |
|------|------|-----------|
| 01 | `01_hello_types.py` | 基本类型、`is` vs `==`、f-string |
| 02 | `02_control_flow.py` | if/for/while、`match/case`、短路逻辑 |
| 03 | `03_functions.py` | 默认参数、`*args`/`**kwargs`、作用域 |
| 04 | `04_collections.py` | list/dict/set/tuple、浅拷贝 |
| 05 | `05_comprehensions.py` | 推导式、生成器、`yield` |
| 06 | `06_files_paths.py` | `pathlib`、UTF-8 读写 |
| 07 | `07_exceptions.py` | try/except、自定义异常、EAFP |
| 08 | `08_imports_modules.py` | import、`__name__`、`demo_module` |
| 09 | `09_stage1_final.py` | **综合**：CSV 聚合 → JSON 报告 |

## 验收标准

- [ ] 能独立编写带文件读写的数据处理脚本
- [ ] 理解 Python 与 Java 在类型、缩进、异常风格上的差异
- [ ] 完成 `09_stage1_final.py` 并查看 `data/report.json`

## 下一步

进入 [stage-2.md](stage-2.md)（面向对象与标准库），或已有基础可直接学 [../langchain/stage-1.md](../langchain/stage-1.md)。
