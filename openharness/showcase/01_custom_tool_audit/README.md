# 01_custom_tool_audit · 只读 Tool + 审计 Hook

对应 **P1** · [`../../base/openharness/p1-custom-tool`](../../base/openharness/p1-custom-tool)

## 结构

```
01_custom_tool_audit/
├── README.md
├── src/
│   ├── tools/
│   │   └── internal_docs.py
│   └── hooks/
│       └── audit.py
└── tests/
    └── test_tool_schema.py
```

## 运行

```bash
cd learn
uv sync --group openharness-showcase

uv run python openharness/showcase/01_custom_tool_audit/src/tools/internal_docs.py
uv run python openharness/showcase/01_custom_tool_audit/tests/test_tool_schema.py
```

## 验收

- [ ] Pydantic 校验输入
- [ ] docstring 含 When to use / Do NOT
- [ ] Hook 产生 audit 记录
