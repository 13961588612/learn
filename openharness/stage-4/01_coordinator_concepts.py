"""
01_coordinator_concepts.py - Coordinator / 子 Agent

学习要点:
1. coordinator 负责 spawn 子 Agent、Team、Task
2. 主 Agent 协调，子 Agent 上下文隔离
"""


def main():
    print("=" * 50)
    print("01 - Coordinator Concepts")
    print("=" * 50)

    print("""
  [User Query]
       |
  [Coordinator / Main Agent]
    /    |    \\
 [Research] [Code] [Review]  <- 子 Agent，独立上下文
       |
  [汇总结果 -> User]
    """)

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
