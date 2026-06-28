"""
06_stream_json_events.py - 解析 stream-json 事件流

学习要点:
1. 非交互模式 --output-format stream-json
2. 识别 content_block_delta、tool_use 等事件类型
"""

import json  # loads 将 JSON 字符串解析为 Python 对象


# 模块级常量：模拟 NDJSON 流中每行一个 JSON 对象的事件列表
SAMPLE_EVENTS = [
    {"type": "message_start", "message": {"role": "assistant"}},
    {"type": "content_block_delta", "delta": {"text": "正在查询"}},
    {"type": "content_block_start", "content_block": {"type": "tool_use", "name": "Read"}},
    {"type": "content_block_delta", "delta": {"partial_json": "{\"path\":"}},
    {"type": "message_stop"},
]


def parse_events(lines: list[str]) -> None:
    """
    逐行解析 NDJSON 事件并打印关键字段。
    lines: list[str] 每行一个 JSON；-> None 表示无返回值。
    """
    for line in lines:
        line = line.strip()  # 去除首尾空白与换行
        if not line:           # 空行跳过
            continue
        try:
            event = json.loads(line)  # 将 JSON 字符串转为 dict
        except json.JSONDecodeError:
            print(f"  非 JSON 行: {line[:60]}")
            continue  # 跳过无法解析的行，继续下一行
        etype = event.get("type", "unknown")  # .get(key, default) 安全取值
        print(f"  event: {etype}")
        # 短路求值：先判断 etype，再检查 delta 中是否有 text
        if etype == "content_block_delta" and "text" in event.get("delta", {}):
            print(f"    text: {event['delta']['text']!r}")  # !r 用 repr 显示，保留引号
        if etype == "content_block_start":
            block = event.get("content_block", {})
            if block.get("type") == "tool_use":
                print(f"    tool: {block.get('name')}")


def main():
    print("=" * 50)
    print("06 - stream-json Events")
    print("=" * 50)
    print("\n=== 模拟 NDJSON 事件流 ===")
    # 列表推导式：[表达式 for 变量 in 可迭代对象]
    lines = [json.dumps(e) for e in SAMPLE_EVENTS]
    parse_events(lines)
    print("\n[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
