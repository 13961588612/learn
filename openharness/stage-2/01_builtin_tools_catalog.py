"""
01_builtin_tools_catalog.py - 内置 Tool 分类与公司禁用清单

学习要点:
1. OpenHarness 内置 43+ Tool 按域分类
2. 公司场景常禁用 Bash、WebFetch 等
"""

# 字典字面量：键为分类名（str），值为该分类下的 Tool 名称列表
# 花括号 {} 定义 dict；列表 [] 定义 list
BUILTIN_CATEGORIES = {
    "File": ["Read", "Write", "Edit", "Glob", "Grep"],
    "Shell": ["Bash"],
    "Web": ["WebFetch", "WebSearch"],
    "Agent": ["Task", "TeamCreate", "SendMessage"],
    "MCP": ["mcp__*"],  # 通配符表示所有 MCP 前缀的 Tool
}

# 集合 set：无序、元素唯一；适合成员测试与去重
COMPANY_DENY = {"Bash", "WebFetch", "WebSearch"}


def main():
    """演示遍历分类字典并打印公司禁用清单。"""
    print("=" * 50)   # 字符串 * 整数：重复 50 次 "="
    print("01 - Builtin Tools Catalog")
    print("=" * 50)

    # .items() 返回 (键, 值) 元组的可迭代对象，用于同时遍历键和值
    for cat, tools in BUILTIN_CATEGORIES.items():
        # f-string 嵌入变量；', '.join(list) 用逗号+空格连接列表元素为单个字符串
        print(f"\n  [{cat}] {', '.join(tools)}")

    print(f"\n=== 公司建议禁用 ===")
    # sorted(set) 返回排序后的新列表，不修改原集合
    print(f"  {', '.join(sorted(COMPANY_DENY))}")
    print("  原因: 生产环境命令执行与任意 URL 访问风险")

    print("\n[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
