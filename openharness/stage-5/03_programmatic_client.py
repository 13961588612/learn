"""
03_programmatic_client.py - 封装 stream-json 客户端（教学）
"""

import json                        # loads() 解析 JSON 字符串为 dict
from typing import Iterator        # Iterator[dict] 表示逐条 yield dict 的生成器


def parse_ndjson_lines(text: str) -> Iterator[dict]:
    # -> Iterator[dict]：生成器函数，调用方可用 for 循环逐行消费
    for line in text.splitlines():  # str
        line = line.strip()  # str
        if line:
            yield json.loads(line)  # yield 惰性产出；loads 解析单行 JSON 为 dict


# str.join(iterable)：用换行符连接列表中的字符串
SAMPLE = "\n".join([
    '{"type":"message_start"}',
    '{"type":"content_block_delta","delta":{"text":"Hello"}}',
    '{"type":"message_stop"}',
])


def main():
    print("=" * 50)   # 字符串 * 整数：重复 50 次
    print("03 - Programmatic Client")
    print("=" * 50)
    # for ev in parse_ndjson_lines(...)：迭代生成器，ev 为每条 stream 事件
    for ev in parse_ndjson_lines(SAMPLE):  # dict
        print(f"  {ev['type']}")   # dict 键访问，取事件类型字段
    print("\n  生产: subprocess openh -p ... --output-format stream-json")
    print("\n[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
