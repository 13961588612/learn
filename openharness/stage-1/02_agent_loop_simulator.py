"""
02_agent_loop_simulator.py - Agent Loop 纯 Python 模拟

学习要点:
1. while 循环直到 stop_reason != tool_use
2. 每次 tool 执行结果追加到 messages
3. 对应 engine/ 伪代码
"""

from dataclasses import dataclass, field  # @dataclass 自动生成 __init__；field 配置可变默认值
from typing import Any, Callable  # Any=任意类型；Callable[[参数], 返回值]=可调用对象类型


# @dataclass 装饰器：自动生成 __init__、__repr__ 等，省去手写样板代码
@dataclass
class Message:
    """单条对话消息：role 标识说话方，content 为文本内容。"""
    role: str      # 类型注解：str 表示字符串
    content: str


@dataclass
class ToolCall:
    """模型请求的一次工具调用：name 为工具名，args 为参数字典。"""
    name: str
    args: dict[str, Any]  # dict[str, Any]：键 str、值任意类型的字典


@dataclass
class AgentState:
    """Agent 循环的状态载体：消息历史 + 当前轮次。"""
    # field(default_factory=list) 避免可变默认值陷阱（不能写 messages: list = []）
    messages: list[Message] = field(default_factory=list)
    turn: int = 0


def fake_model(messages: list[Message], turn: int) -> tuple[str, list[ToolCall] | None]:
    """
    模拟模型：第 1 轮要 Tool，第 2 轮结束。
    返回 tuple[str, list[ToolCall] | None]：stop_reason 与可选的 tool_calls 列表。
    """
    if turn == 0:
        return "tool_use", [ToolCall("get_time", {})]
    return "end_turn", None


# 模块级常量：工具名 -> 可调用对象的注册表
# Callable[[dict], str] 表示接收 dict、返回 str 的函数
TOOL_REGISTRY: dict[str, Callable[[dict], str]] = {
    "get_time": lambda _: "2026-06-21T12:00:00Z",  # lambda _: 忽略未使用的参数
}


def run_agent_loop(max_turns: int = 10) -> AgentState:
    """
    模拟 Agent 主循环：模型决策 -> 执行 tool -> 追加结果 -> 下一轮。
    max_turns: int = 10 为默认参数；-> AgentState 为返回值类型注解。
    """
    state = AgentState(messages=[Message("user", "现在几点？")])

    while state.turn < max_turns:
        stop_reason, tool_calls = fake_model(state.messages, state.turn)
        print(f"\n--- Turn {state.turn + 1} stop={stop_reason} ---")

        # 非 tool_use 或无 tool_calls 时结束循环
        if stop_reason != "tool_use" or not tool_calls:
            state.messages.append(Message("assistant", "当前时间是 2026-06-21T12:00:00Z"))
            break  # 跳出 while 循环

        for tc in tool_calls:
            print(f"  tool_call: {tc.name}({tc.args})")
            result = TOOL_REGISTRY[tc.name](tc.args)  # 字典下标访问 + 函数调用
            state.messages.append(Message("tool", result))
            print(f"  tool_result: {result}")

        state.turn += 1

    return state


def main():
    print("=" * 50)
    print("02 - Agent Loop Simulator")
    print("=" * 50)
    final = run_agent_loop()
    print(f"\n最终 messages 条数: {len(final.messages)}")  # len() 获取列表长度
    print("[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
