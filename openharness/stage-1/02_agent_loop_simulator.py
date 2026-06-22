"""
02_agent_loop_simulator.py - Agent Loop 纯 Python 模拟

学习要点:
1. while 循环直到 stop_reason != tool_use
2. 每次 tool 执行结果追加到 messages
3. 对应 engine/ 伪代码
"""

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class Message:
    role: str
    content: str


@dataclass
class ToolCall:
    name: str
    args: dict[str, Any]


@dataclass
class AgentState:
    messages: list[Message] = field(default_factory=list)
    turn: int = 0


def fake_model(messages: list[Message], turn: int) -> tuple[str, list[ToolCall] | None]:
    """模拟模型：第 1 轮要 Tool，第 2 轮结束"""
    if turn == 0:
        return "tool_use", [ToolCall("get_time", {})]
    return "end_turn", None


TOOL_REGISTRY: dict[str, Callable[[dict], str]] = {
    "get_time": lambda _: "2026-06-21T12:00:00Z",
}


def run_agent_loop(max_turns: int = 10) -> AgentState:
    state = AgentState(messages=[Message("user", "现在几点？")])

    while state.turn < max_turns:
        stop_reason, tool_calls = fake_model(state.messages, state.turn)
        print(f"\n--- Turn {state.turn + 1} stop={stop_reason} ---")

        if stop_reason != "tool_use" or not tool_calls:
            state.messages.append(Message("assistant", "当前时间是 2026-06-21T12:00:00Z"))
            break

        for tc in tool_calls:
            print(f"  tool_call: {tc.name}({tc.args})")
            result = TOOL_REGISTRY[tc.name](tc.args)
            state.messages.append(Message("tool", result))
            print(f"  tool_result: {result}")

        state.turn += 1

    return state


def main():
    print("=" * 50)
    print("02 - Agent Loop Simulator")
    print("=" * 50)
    final = run_agent_loop()
    print(f"\n最终 messages 条数: {len(final.messages)}")
    print("[OK] 完成")


if __name__ == "__main__":
    main()
