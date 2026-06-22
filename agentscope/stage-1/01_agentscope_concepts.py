"""
01_agentscope_concepts.py - AgentScope 2.x 架构与定位

学习要点:
1. AgentScope = 多 Agent 应用框架（非 Harness 壳）
2. 核心：Msg / Agent / Toolkit / Model / Middleware
3. 与 LangChain、OpenHarness 分工
"""

MODULES = {
    "message": "统一 Msg 与 ContentBlock",
    "agent": "Agent.reply / reply_stream / observe",
    "tool": "Toolkit、FunctionTool、MCP、Skills",
    "model": "多 Provider ChatModel",
    "middleware": "on_acting 等 Hook 二开点",
    "permission": "Tool 权限决策",
}


def main():
    print("=" * 50)
    print("01 - AgentScope Concepts (v2)")
    print("=" * 50)

    print("\n=== 定位 ===")
    print("  AgentScope → 构建多 Agent 应用、Tool/MCP、Bridge")
    print("  LangChain  → 业务图编排")
    print("  OpenHarness → 统一运行时与治理")

    print("\n=== 核心模块 ===")
    for k, v in MODULES.items():
        print(f"  {k}: {v}")

    print("\n=== 2.x 变化 ===")
    print("  统一 Agent 类（旧版 ReActAgent 已合并）")
    print("  Middleware 替代部分 Hook 场景")
    print("  Toolkit 集成 MCP + Skills")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
