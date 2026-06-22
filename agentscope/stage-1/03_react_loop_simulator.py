"""
03_react_loop_simulator.py - ReAct 循环模拟（无 API）

学习要点:
1. reasoning -> tool_use -> acting -> 追加结果
2. max_iters 熔断
"""

from dataclasses import dataclass


@dataclass
class Step:
    kind: str
    detail: str


def simulate_react(user_query: str, max_iters: int = 5) -> list[Step]:
    trace: list[Step] = []
    trace.append(Step("reasoning", f"理解: {user_query}"))
    trace.append(Step("tool_use", "search_docs(query=发布)"))
    trace.append(Step("acting", "命中 D1 发布流程"))
    trace.append(Step("reasoning", "信息足够，生成答案"))
    trace.append(Step("reply", "staging -> prod 需 CR"))
    if len(trace) > max_iters:
        trace.append(Step("exceed_max_iters", "熔断"))
    return trace


def main():
    print("=" * 50)
    print("03 - ReAct Loop Simulator")
    print("=" * 50)

    for i, step in enumerate(simulate_react("发布流程是什么"), 1):
        print(f"  {i}. [{step.kind}] {step.detail}")

    print("\n  对照 Agent.reply() 真实行为做 lab 01")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
