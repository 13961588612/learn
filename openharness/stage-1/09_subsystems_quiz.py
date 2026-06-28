"""
09_subsystems_quiz.py - 十子系统对照自测

学习要点:
1. 每个子系统一句话职责
2. 公司后端重点子系统
"""

# 模块级常量：子系统名 -> 一句话职责
SUBSYSTEMS = {
    "engine": "Agent Loop 调度",
    "tools": "内置 + 自定义 Tool 目录",
    "skills": "按需加载 SKILL.md",
    "plugins": "命令 + Hook + 子 Agent 包",
    "permissions": "写/执行前门禁",
    "hooks": "Pre/Post Tool 生命周期",
    "commands": "/plan /commit 等斜杠命令",
    "mcp": "外部 Tool 协议客户端",
    "memory": "MEMORY.md 跨会话",
    "coordinator": "子 Agent / Team / Task",
}


def main():
    """打印十子系统对照表与公司后端重点列表。"""
    print("=" * 50)
    print("09 - Subsystems Quiz")
    print("=" * 50)

    print("\n=== 十子系统 ===")
    for name, desc in SUBSYSTEMS.items():  # .items() 遍历键值对
        # {name:14} 左对齐占 14 字符宽度，便于列对齐
        print(f"  {name:14} {desc}")

    company_focus = ["engine", "tools", "skills", "plugins", "permissions", "hooks", "mcp", "coordinator"]
    print("\n=== 公司后端重点 ===")
    print(", ".join(company_focus))  # join 将列表元素用逗号连接

    print("\n[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
