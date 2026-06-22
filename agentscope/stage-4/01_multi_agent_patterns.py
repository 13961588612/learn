"""01_multi_agent_patterns.py - 多 Agent 模式"""

PATTERNS = {
    "sequential_handoff": "A 产出 Msg -> B.observe/reply",
    "specialist_routing": "路由 Agent 分派到专家",
    "critic_reviewer": "生成 + 审查两 Agent",
}


def main():
    print("=" * 50)
    print("01 - Multi-Agent Patterns")
    print("=" * 50)
    for k, v in PATTERNS.items():
        print(f"  {k}: {v}")
    print("\n  实现: showcase/02_multi_agent_handoff")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
