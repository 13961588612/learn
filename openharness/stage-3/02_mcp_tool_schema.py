"""
02_mcp_tool_schema.py - MCP Tool JSON Schema

学习要点:
1. MCP tools/list 返回 name + inputSchema
2. 与 Pydantic model_json_schema 对齐
"""

from pydantic import BaseModel, Field  # BaseModel=数据模型基类；Field=字段元数据/默认值


class SearchTicketsInput(BaseModel):
    # str 类型注解；Field(description=...) 写入 JSON Schema 的 description
    keyword: str = Field(description="工单标题关键词")
    # default="open" 表示可选字段，未传参时使用默认值
    status: str = Field(default="open", description="open|closed")


def main():
    print("=" * 50)   # 字符串 * 整数：重复 50 次
    print("02 - MCP Tool Schema")
    print("=" * 50)

    # model_json_schema() 生成符合 JSON Schema 规范的字典，可直接作为 inputSchema
    schema = SearchTicketsInput.model_json_schema()  # dict
    # 字典字面量 {} 构造 MCP Tool 描述；键值对用冒号分隔
    mcp_tool = {  # dict
        "name": "search_tickets",
        "description": "Search internal tickets (read-only)",
        "inputSchema": schema,  # 引用上面 Pydantic 生成的 schema
    }

    # f-string 嵌入表达式；dict['key'] 按键取值
    print(f"  tool name: {mcp_tool['name']}")
    # .get('required') 安全取值，键不存在时返回 None 而非抛 KeyError
    print(f"  required: {schema.get('required')}")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
