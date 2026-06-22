"""
04_event_stream_concepts.py - reply_stream 事件类型（概念）

学习要点:
1. reply() 消费全部事件得最终 Msg
2. reply_stream() 产出 AgentEvent 供集成
"""

EVENT_TYPES = [
    "ReplyStartEvent",
    "ModelCallStartEvent",
    "TextBlockDeltaEvent",
    "ToolCallStartEvent",
    "ToolResultEndEvent",
    "ReplyEndEvent",
]


def main():
    print("=" * 50)
    print("04 - Event Stream Concepts")
    print("=" * 50)

    print("\n=== 常见 AgentEvent ===")
    for e in EVENT_TYPES:
        print(f"  - {e}")

    print("\n=== 集成建议 ===")
    print("  Gateway SSE: 订阅 reply_stream，映射为前端事件")
    print("  批处理: 用 reply() 取最终 Msg")

    print("\n  Lab: stage-1/lab/scripts/02_reply_stream_events.py")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
