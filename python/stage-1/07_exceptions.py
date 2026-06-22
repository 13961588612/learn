"""
07_exceptions.py - try/except/else/finally、自定义异常、EAFP

学习要点:
1. EAFP（Easier to Ask Forgiveness than Permission）Python 风格
2. else 在没有异常时执行，finally 无论如何都执行
3. 自定义异常继承 Exception
"""


class ValidationError(Exception):
    """业务校验失败"""

    def __init__(self, field: str, message: str):
        self.field = field
        super().__init__(f"{field}: {message}")


def parse_age(text: str) -> int:
    try:
        age = int(text)
    except ValueError as e:
        raise ValidationError("age", f"必须是整数，收到 {text!r}") from e

    if age < 0 or age > 150:
        raise ValidationError("age", "超出合理范围 0-150")
    return age


def demo_try_except():
    print("\n=== try / except / else / finally ===")
    for raw in ["25", "abc", "-1"]:
        print(f"\n输入: {raw!r}")
        try:
            age = parse_age(raw)
        except ValidationError as e:
            print(f"  校验失败: {e}")
        else:
            print(f"  成功: age={age}")
        finally:
            print("  (finally: 清理或日志)")


def demo_eafp():
    print("\n=== EAFP vs LBYL ===")
    data = {"name": "Eve"}

    # EAFP: 直接尝试，捕获 KeyError
    try:
        city = data["city"]
    except KeyError:
        city = "未知"
    print(f"EAFP city = {city}")

    # LBYL (Look Before You Leap): Java 更常见
    city2 = data["city"] if "city" in data else "未知"
    print(f"LBYL city = {city2}")


def main():
    print("=" * 50)
    print("07 - Exceptions")
    print("=" * 50)
    demo_try_except()
    demo_eafp()
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
