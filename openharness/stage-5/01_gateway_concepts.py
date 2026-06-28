"""
01_gateway_concepts.py - Gateway / ohmo / 多通道概念
"""

# 元组列表：每个元素是 (通道名, 说明) 的 2 元组
CHANNELS = [
    ("CLI/TUI", "openh 交互"),
    ("stream-json", "程序化集成、脚本、BFF"),
    ("ohmo Gateway", "飞书/Slack/Webhook 等 IM 通道"),
    ("HTTP Webhook", "内部系统回调（showcase/04）"),
]


def main():
    print("=" * 50)   # 字符串 * 整数：重复 50 次
    print("01 - Gateway Concepts")
    print("=" * 50)
    # for name, desc in CHANNELS：元组解包，依次遍历每个通道
    for name, desc in CHANNELS:
        # f-string：{name:14} 左对齐占 14 字符宽度
        print(f"  {name:14} {desc}")
    print("\n  公司典型: IM -> Gateway -> Harness -> stream 回传")
    print("\n[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
