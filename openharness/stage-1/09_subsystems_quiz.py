"""
09_subsystems_quiz.py - 十子系统对照自测

学习要点:
1. 每个子系统一句话职责
2. 公司后端重点子系统
"""

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
    print("=" * 50)
    print("09 - Subsystems Quiz")
    print("=" * 50)

    print("\n=== 十子系统 ===")
    for name, desc in SUBSYSTEMS.items():
        print(f"  {name:14} {desc}")

    company_focus = ["engine", "tools", "skills", "plugins", "permissions", "hooks", "mcp", "coordinator"]
    print("\n=== 公司后端重点 ===")
    print(", ".join(company_focus))

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
