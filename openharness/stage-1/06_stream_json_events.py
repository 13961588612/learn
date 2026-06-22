"""
06_stream_json_events.py - 解析 stream-json 事件流

学习要点:
1. 非交互模式 --output-format stream-json
2. 识别 content_block_delta、tool_use 等事件类型
"""

import json


SAMPLE_EVENTS = [
    {"type": "message_start", "message": {"role": "assistant"}},
    {"type": "content_block_delta", "delta": {"text": "正在查询"}},
    {"type": "content_block_start", "content_block": {"type": "tool_use", "name": "Read"}},
    {"type": "content_block_delta", "delta": {"partial_json": "{\"path\":"}},
    {"type": "message_stop"},
]


def parse_events(lines: list[str]) -> None:
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            print(f"  非 JSON 行: {line[:60]}")
            continue
        etype = event.get("type", "unknown")
        print(f"  event: {etype}")
        if etype == "content_block_delta" and "text" in event.get("delta", {}):
            print(f"    text: {event['delta']['text']!r}")
        if etype == "content_block_start":
            block = event.get("content_block", {})
            if block.get("type") == "tool_use":
                print(f"    tool: {block.get('name')}")


def main():
    print("=" * 50)
    print("06 - stream-json Events")
    print("=" * 50)
    print("\n=== 模拟 NDJSON 事件流 ===")
    lines = [json.dumps(e) for e in SAMPLE_EVENTS]
    parse_events(lines)
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
