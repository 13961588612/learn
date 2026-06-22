"""
07_vs_langgraph.py - OpenHarness coordinator vs LangGraph 子图

学习要点:
1. Harness：运行时多 Agent 协调
2. LangGraph：应用内 StateGraph 编排
3. 复杂子流程可下沉 LangGraph + MCP 暴露
"""


COMPARISON = [
    ("编排位置", "Harness coordinator / Task", "LangGraph StateGraph"),
    ("状态持久化", "MEMORY.md / session", "Checkpointer"),
    ("适用场景", "统一 Gateway、Tool 治理", "复杂业务分支、HITL"),
    ("集成方式", "MCP 调用 LangGraph 服务", "同进程或独立 API"),
]


def main():
    print("=" * 50)
    print("07 - vs LangGraph")
    print("=" * 50)

    for dim, oh, lg in COMPARISON:
        print(f"\n  [{dim}]")
        print(f"    OpenHarness: {oh}")
        print(f"    LangGraph:   {lg}")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
