"""02_function_tool_schema.py - FunctionTool 与 docstring schema"""

from pydantic import BaseModel, Field

from agentscope.tool import FunctionTool, Toolkit


class SearchInput(BaseModel):
    query: str = Field(min_length=1, description="搜索关键词")


def search_internal_docs(query: str) -> str:
    """
    搜索公司内部文档（只读 mock）。

    Args:
        query: 关键词
    """
    docs = {"发布": "staging->prod", "故障": "先 rollback"}
    for k, v in docs.items():
        if query in k:
            return v
    return f"ERROR: 无匹配 {query!r}"


def main():
    print("=" * 50)
    print("02 - FunctionTool Schema")
    print("=" * 50)

    tool = FunctionTool(search_internal_docs, is_read_only=True)
    tk = Toolkit(tools=[tool])
    print(f"  tool name: {tool.name}")
    print(f"  schema keys: {list(tool.input_schema.get('properties', {}).keys())}")
    print(f"  toolkit registered: ok")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
