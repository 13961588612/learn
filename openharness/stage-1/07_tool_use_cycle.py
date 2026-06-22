"""
07_tool_use_cycle.py - tool_use 消息循环

学习要点:
1. assistant tool_use → tool result → 下一轮 model
2. 消息列表是 Loop 的状态载体
"""

from typing import Any


def append_tool_result(messages: list[dict[str, Any]], tool_use_id: str, output: str) -> None:
    messages.append({
        "role": "user",
        "content": [{
            "type": "tool_result",
            "tool_use_id": tool_use_id,
            "content": output,
        }],
    })


def main():
    print("=" * 50)
    print("07 - Tool Use Cycle")
    print("=" * 50)

    messages: list[dict[str, Any]] = [
        {"role": "user", "content": "读取 config.json"},
    ]

    # 模拟 assistant 发起 tool_use
    tool_use_id = "toolu_001"
    messages.append({
        "role": "assistant",
        "content": [{
            "type": "tool_use",
            "id": tool_use_id,
            "name": "Read",
            "input": {"path": "config.json"},
        }],
    })
    print(f"  messages 长度: {len(messages)}")

    append_tool_result(messages, tool_use_id, '{"debug": true}')
    print(f"  追加 tool_result 后: {len(messages)}")
    print(f"  最后一条 role: {messages[-1]['role']}")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
