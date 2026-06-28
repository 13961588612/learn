"""
01_harness_concepts.py - 四层架构与十子系统

学习要点:
1. OpenHarness = Agent 运行时壳，不是业务 Agent 框架
2. 四层：能力 / 安全 / 协作 / 基础设施
3. 十子系统职责速览
"""

# 模块级常量：字典字面量，键为层名、值为子系统名列表
LAYERS = {
    "能力层": ["tools", "skills"],
    "安全层": ["permissions", "hooks"],
    "协作扩展层": ["mcp", "plugins", "coordinator", "tasks"],
    "基础设施层": ["engine", "config", "memory", "prompts", "ui"],
}


def main():
    """打印四层架构与 LangChain 分工说明。"""
    print("=" * 50)   # 字符串 * 整数：重复 50 次，生成分隔线
    print("01 - Harness Concepts")
    print("=" * 50)

    print("\n=== 核心理念 ===")
    print("The model is the agent. The code is the harness.")
    print("模型负责「想」；Harness 负责「手、眼、记忆、安全边界」。")

    print("\n=== 四层架构 ===")
    # .items() 返回 (键, 值) 元组的可迭代对象，用于遍历字典
    for layer, subs in LAYERS.items():
        # ', '.join(subs) 将列表元素用逗号连接成单个字符串
        print(f"  {layer}: {', '.join(subs)}")

    print("\n=== 与 LangChain 分工 ===")
    print("  LangChain  → 应用内编排 Agent 业务逻辑")
    print("  OpenHarness → 统一运行时、Tool 治理、Gateway、审计")

    print("\n[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
