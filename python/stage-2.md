# 阶段二：面向对象与标准库 - 学习指南

> **Python 3.11+** · 仅标准库

## 启动学习

```bash
uv run python python/stage-2/01_classes_basics.py
# ... 按编号至 09
uv run python python/stage-2/09_stage2_final.py
```

`09_stage2_final.py` 依赖同目录 `notes/` 包，请在 `python/stage-2/` 下运行或使用上述根目录命令。

## 练习脚本速览

| 编号 | 文件 | 核心知识点 |
|------|------|-----------|
| 01 | `01_classes_basics.py` | 类、classmethod、staticmethod |
| 02 | `02_inheritance.py` | 继承、多态、ABC |
| 03 | `03_dataclass_enum.py` | dataclass、Enum、NamedTuple |
| 04 | `04_properties_protocol.py` | @property、Protocol |
| 05 | `05_iterators_context.py` | 迭代器、with、contextmanager |
| 06 | `06_decorators.py` | 装饰器、functools.wraps |
| 07 | `07_stdlib_json_datetime.py` | json、datetime、zoneinfo |
| 08 | `08_stdlib_os_subprocess.py` | os.environ、subprocess |
| 09 | `09_stage2_final.py` | **综合**：notes 包 + JSON 存储 |

## 包结构（09 综合练习）

```
stage-2/
├── notes/
│   ├── __init__.py
│   ├── models.py      # Note 数据类
│   └── storage.py     # NoteStore 持久化
└── data/
    └── notes.json     # 运行后生成
```

## 验收标准

- [ ] 能实现带类与模块划分的小型包
- [ ] 理解 dataclass、Protocol、装饰器等工程常用特性
- [ ] 完成 notes 综合练习

## 下一步

[stage-3.md](stage-3.md)（typing、Pydantic、async）或 [../langchain/stage-1.md](../langchain/stage-1.md)。
