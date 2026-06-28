"""
07_tool_use_cycle.py - tool_use 消息循环

学习要点:
1. assistant tool_use → tool result → 下一轮 model
2. 消息列表是 Loop 的状态载体
"""

from typing import Any  # Any 表示任意类型，用于 JSON 风格的消息 dict


def append_tool_result(messages: list[dict[str, Any]], tool_use_id: str, output: str) -> None:
    """
    向 messages 追加一条 user 角色的 tool_result 块。
    messages 为可变列表，原地 append，无返回值（-> None）。
    """
    messages.append({
        "role": "user",
        "content": [{  # content 为块列表，符合 Anthropic API 消息格式
            "type": "tool_result",
            "tool_use_id": tool_use_id,
            "content": output,
        }],
    })


def main():
    print("=" * 50)
    print("07 - Tool Use Cycle")
    print("=" * 50)

    # 显式类型注解：消息列表，元素为 str 键的字典
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
    print(f"  最后一条 role: {messages[-1]['role']}")  # [-1] 取列表最后一个元素

    print("\n[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
