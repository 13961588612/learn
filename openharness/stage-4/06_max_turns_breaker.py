"""
06_max_turns_breaker.py - tool 死循环熔断

学习要点:
1. --max-turns 限制 Agent Loop 轮数
2. 同一 Tool 重复调用检测
"""

from collections import Counter


def should_break(turn: int, max_turns: int, tool_history: list[str], repeat_limit: int = 5) -> tuple[bool, str]:
    if turn >= max_turns:
        return True, f"max_turns={max_turns}"
    counts = Counter(tool_history)
    for name, cnt in counts.items():
        if cnt >= repeat_limit:
            return True, f"repeated tool {name} x{cnt}"
    return False, "continue"


def main():
    print("=" * 50)
    print("06 - Max Turns Breaker")
    print("=" * 50)

    history = ["Read", "Read", "Read", "Read", "Read"]
    broken, reason = should_break(turn=5, max_turns=20, tool_history=history)
    print(f"  repeat case: break={broken} reason={reason}")

    broken2, reason2 = should_break(turn=25, max_turns=20, tool_history=["Grep"])
    print(f"  max_turns case: break={broken2} reason={reason2}")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
