"""
03_programmatic_client.py - 封装 stream-json 客户端（教学）
"""

import json
from typing import Iterator


def parse_ndjson_lines(text: str) -> Iterator[dict]:
    for line in text.splitlines():
        line = line.strip()
        if line:
            yield json.loads(line)


SAMPLE = "\n".join([
    '{"type":"message_start"}',
    '{"type":"content_block_delta","delta":{"text":"Hello"}}',
    '{"type":"message_stop"}',
])


def main():
    print("=" * 50)
    print("03 - Programmatic Client")
    print("=" * 50)
    for ev in parse_ndjson_lines(SAMPLE):
        print(f"  {ev['type']}")
    print("\n  生产: subprocess openh -p ... --output-format stream-json")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
