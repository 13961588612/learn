"""
01_mcp_concepts.py - MCP 角色与 Tool 暴露

学习要点:
1. MCP Server 暴露 tools/resources
2. Harness 作为 MCP Client 调用
3. 内部系统主接入方式
"""


def main():
    print("=" * 50)
    print("01 - MCP Concepts")
    print("=" * 50)

    print("""
  [业务系统 API] <---> [MCP Server] <--stdio/HTTP--> [OpenHarness mcp/]
                                                          |
                                                    [Agent Loop]
    """)

    print("  LangChain @tool 包装路径:")
    print("    @tool -> MCP Server -> openh mcp 配置 -> Harness 调用")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
