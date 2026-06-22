# 3 · Toolkit 与 Middleware 二开

## FunctionTool

```python
from agentscope.tool import FunctionTool, Toolkit

def search_internal_docs(query: str) -> str:
    """只读搜索。Args: query: 关键词"""
    ...

toolkit = Toolkit(tools=[FunctionTool(search_internal_docs, is_read_only=True)])
agent = Agent(..., toolkit=toolkit)
```

## Audit Middleware

见 `_shared/audit_middleware.py` 与 `showcase/01_readonly_toolkit_audit/`。

Hook 点：`on_acting` 记录 tool 名；勿 log 全量 PII。

## 生产

- 只读 Tool：`is_read_only=True`
- 禁用危险内置 Tool 或 strict permission
- 失败返回 `ERROR: ...` 引导模型纠错

[← 返回](../README.md)
