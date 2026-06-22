"""02_bridge_contract.py - IntentGate Bridge REST 契约"""

ROUTES = [
    "POST /v1/sessions/{session_id}/messages  -> SSE AgentReply",
    "POST /v1/sessions/{session_id}/actions   -> SSE AgentReply",
]


def main():
    print("=" * 50)
    print("02 - Bridge Contract")
    print("=" * 50)
    for r in ROUTES:
        print(f"  {r}")
    print("\n  参考: langchain/practice/intentgate/adapters/agentscope.py")
    print("  实现: showcase/04_intentgate_bridge")
    print("\n[OK] 完成")
if __name__ == "__main__":
    main()
