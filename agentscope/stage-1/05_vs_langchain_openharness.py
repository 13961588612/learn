"""
05_vs_langchain_openharness.py - 三框架分工
"""

COMPARISON = [
    ("LangChain/LangGraph", "图编排、State、Checkpoint", "复杂业务流程"),
    ("AgentScope", "多 Agent、Toolkit、MCP、Bridge", "Agent 应用与二开"),
    ("OpenHarness", "Harness、Skills 治理、Gateway", "公司统一运行时"),
]


def main():
    print("=" * 50)
    print("05 - Framework Map")
    print("=" * 50)
    for name, focus, when in COMPARISON:
        print(f"\n  {name}")
        print(f"    专注: {focus}")
        print(f"    何时: {when}")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
