"""
07_exceptions.py - try/except/else/finally、自定义异常、EAFP

学习要点:
1. EAFP（Easier to Ask Forgiveness than Permission）Python 风格
2. else 在没有异常时执行，finally 无论如何都执行
3. 自定义异常继承 Exception
"""


class ValidationError(Exception):
    """业务校验失败；自定义异常应继承 Exception（或其子类）"""

    def __init__(self, field: str, message: str):
        self.field = field  # 附加业务字段，便于调用方处理
        # super().__init__(...) 调用父类 Exception 的构造，设置异常消息
        super().__init__(f"{field}: {message}")


def parse_age(text: str) -> int:
    try:
        age = int(text)  # 非数字字符串会抛出 ValueError
    except ValueError as e:
        # raise ... from e 链式异常，保留原始 traceback
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
        except ValidationError as e:  # 只捕获 ValidationError 及其子类
            print(f"  校验失败: {e}")
        else:
            # else：try 块无异常时执行（不是「否则」的意思）
            print(f"  成功: age={age}")
        finally:
            # finally：无论是否异常都会执行，常用于清理资源
            print("  (finally: 清理或日志)")


def demo_eafp():
    print("\n=== EAFP vs LBYL ===")
    data = {"name": "Eve"}

    # EAFP：先尝试，失败再处理（Python 惯用）
    try:
        city = data["city"]  # 键不存在时抛 KeyError
    except KeyError:
        city = "未知"
    print(f"EAFP city = {city}")

    # LBYL：先检查再行动（Java 等语言更常见）
    city2 = data["city"] if "city" in data else "未知"  # 三元表达式
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
