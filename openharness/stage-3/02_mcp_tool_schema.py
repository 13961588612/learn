"""
02_mcp_tool_schema.py - MCP Tool JSON Schema

学习要点:
1. MCP tools/list 返回 name + inputSchema
2. 与 Pydantic model_json_schema 对齐
"""

from pydantic import BaseModel, Field


class SearchTicketsInput(BaseModel):
    keyword: str = Field(description="工单标题关键词")
    status: str = Field(default="open", description="open|closed")


def main():
    print("=" * 50)
    print("02 - MCP Tool Schema")
    print("=" * 50)

    schema = SearchTicketsInput.model_json_schema()
    mcp_tool = {
        "name": "search_tickets",
        "description": "Search internal tickets (read-only)",
        "inputSchema": schema,
    }

    print(f"  tool name: {mcp_tool['name']}")
    print(f"  required: {schema.get('required')}")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
