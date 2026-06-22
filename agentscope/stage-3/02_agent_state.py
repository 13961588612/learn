"""02_agent_state.py - AgentState 概念"""

from agentscope.state import AgentState


def main():
    print("=" * 50)
    print("02 - AgentState")
    print("=" * 50)
    state = AgentState()
    print(f"  新建 AgentState: {type(state).__name__}")
    print("  用途: 跨 reply 持久化上下文、Tool 状态注入")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
