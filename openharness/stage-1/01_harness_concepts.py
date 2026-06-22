"""
01_harness_concepts.py - 四层架构与十子系统

学习要点:
1. OpenHarness = Agent 运行时壳，不是业务 Agent 框架
2. 四层：能力 / 安全 / 协作 / 基础设施
3. 十子系统职责速览
"""

LAYERS = {
    "能力层": ["tools", "skills"],
    "安全层": ["permissions", "hooks"],
    "协作扩展层": ["mcp", "plugins", "coordinator", "tasks"],
    "基础设施层": ["engine", "config", "memory", "prompts", "ui"],
}


def main():
    print("=" * 50)
    print("01 - Harness Concepts")
    print("=" * 50)

    print("\n=== 核心理念 ===")
    print("The model is the agent. The code is the harness.")
    print("模型负责「想」；Harness 负责「手、眼、记忆、安全边界」。")

    print("\n=== 四层架构 ===")
    for layer, subs in LAYERS.items():
        print(f"  {layer}: {', '.join(subs)}")

    print("\n=== 与 LangChain 分工 ===")
    print("  LangChain  → 应用内编排 Agent 业务逻辑")
    print("  OpenHarness → 统一运行时、Tool 治理、Gateway、审计")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
