"""
01_toolkit_concepts.py - Toolkit 组成

学习要点:
1. tools / mcps / skills_or_loaders / tool_groups
2. 内置 Read Write Bash 等
"""

from agentscope.tool import Bash, Glob, Read, Toolkit, Write


def main():
    print("=" * 50)
    print("01 - Toolkit Concepts")
    print("=" * 50)

    tk = Toolkit()
    print("  空 Toolkit 创建成功")
    print("\n=== 内置 Tool 类（按需注册）===")
    for cls in (Read, Write, Glob, Bash):
        print(f"  - {cls.__name__}")

    print("\n=== 生产建议 ===")
    print("  只读业务用 FunctionTool(is_read_only=True)")
    print("  危险内置 Tool 生产环境禁用或 strict permission")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
