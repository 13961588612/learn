"""
01_mcp_concepts.py - MCP 角色与 Tool 暴露

学习要点:
1. MCP Server 暴露 tools/resources
2. Harness 作为 MCP Client 调用
3. 内部系统主接入方式
"""


def main():
    print("=" * 50)   # 字符串 * 整数：重复 50 次，用作分隔线
    print("01 - MCP Concepts")
    print("=" * 50)

    # 三引号字符串可跨行，保留换行与缩进，适合打印 ASCII 架构图
    print("""
  [业务系统 API] <---> [MCP Server] <--stdio/HTTP--> [OpenHarness mcp/]
                                                          |
                                                    [Agent Loop]
    """)

    print("  LangChain @tool 包装路径:")
    print("    @tool -> MCP Server -> openh mcp 配置 -> Harness 调用")

    print("\n[OK] 完成")  # \n 换行符


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
