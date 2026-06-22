"""
01_gateway_concepts.py - Gateway / ohmo / 多通道概念
"""

CHANNELS = [
    ("CLI/TUI", "openh 交互"),
    ("stream-json", "程序化集成、脚本、BFF"),
    ("ohmo Gateway", "飞书/Slack/Webhook 等 IM 通道"),
    ("HTTP Webhook", "内部系统回调（showcase/04）"),
]


def main():
    print("=" * 50)
    print("01 - Gateway Concepts")
    print("=" * 50)
    for name, desc in CHANNELS:
        print(f"  {name:14} {desc}")
    print("\n  公司典型: IM -> Gateway -> Harness -> stream 回传")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
