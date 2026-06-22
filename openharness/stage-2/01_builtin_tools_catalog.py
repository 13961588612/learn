"""
01_builtin_tools_catalog.py - 内置 Tool 分类与公司禁用清单

学习要点:
1. OpenHarness 内置 43+ Tool 按域分类
2. 公司场景常禁用 Bash、WebFetch 等
"""

BUILTIN_CATEGORIES = {
    "File": ["Read", "Write", "Edit", "Glob", "Grep"],
    "Shell": ["Bash"],
    "Web": ["WebFetch", "WebSearch"],
    "Agent": ["Task", "TeamCreate", "SendMessage"],
    "MCP": ["mcp__*"],
}

COMPANY_DENY = {"Bash", "WebFetch", "WebSearch"}


def main():
    print("=" * 50)
    print("01 - Builtin Tools Catalog")
    print("=" * 50)

    for cat, tools in BUILTIN_CATEGORIES.items():
        print(f"\n  [{cat}] {', '.join(tools)}")

    print(f"\n=== 公司建议禁用 ===")
    print(f"  {', '.join(sorted(COMPANY_DENY))}")
    print("  原因: 生产环境命令执行与任意 URL 访问风险")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
