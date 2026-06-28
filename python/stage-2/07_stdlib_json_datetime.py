"""
07_stdlib_json_datetime.py - json、datetime、zoneinfo

学习要点:
1. json.dumps/loads 与 ensure_ascii=False 处理中文
2. datetime 与 ISO 8601 字符串互转
3. zoneinfo 处理时区（3.9+ 标准库）
"""

import json
from datetime import datetime, timedelta, timezone  # timezone.utc 等
from zoneinfo import ZoneInfo  # IANA 时区名，如 "Asia/Shanghai"


def demo_json():
    print("\n=== json ===")
    payload = {"user": "Frank", "roles": ["admin", "editor"], "score": 98.5}
    # dumps：Python 对象 → JSON 字符串
    text = json.dumps(payload, ensure_ascii=False, indent=2)
    print(text)
    # loads：JSON 字符串 → Python 对象
    restored = json.loads(text)
    print(f"反序列化 roles = {restored['roles']}")


def demo_datetime():
    print("\n=== datetime ===")
    now_utc = datetime.now(timezone.utc)  # 带时区信息的 UTC 时间
    print(f"UTC now: {now_utc.isoformat()}")  # ISO 8601 格式字符串

    shanghai = ZoneInfo("Asia/Shanghai")
    local = now_utc.astimezone(shanghai)  # 转换到指定时区
    # strftime 自定义格式；%Z 时区缩写
    print(f"上海时间: {local.strftime('%Y-%m-%d %H:%M:%S %Z')}")

    deadline = local + timedelta(days=7)  # 日期运算
    print(f"七天后: {deadline.date()}")  # .date() 只取日期部分


def main():
    print("=" * 50)
    print("07 - json & datetime")
    print("=" * 50)
    demo_json()
    demo_datetime()
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
