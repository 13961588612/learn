"""
01_hello_types.py - 变量、基本类型、is vs ==、f-string

学习要点:
1. Python 动态类型与 Java 静态类型的差异
2. 基本类型: int / float / str / bool / None
3. `is` 比较身份，`==` 比较值
4. f-string 格式化（推荐于 % 与 .format）
"""


def demo_basic_types():
    print("\n=== 基本类型 ===")
    # 变量名: 类型 是类型注解，运行时不会强制校验，供 IDE / mypy 使用
    age: int = 30
    price: float = 19.99
    name: str = "Alice"
    active: bool = True
    nothing = None  # None 是空值单例，类型为 NoneType

    # !r 调用 repr()，输出带引号的字符串字面量形式
    # type(x).__name__ 取类型名字符串，如 "str"
    print(f"name={name!r}, type={type(name).__name__}")
    # :.2f 格式化为保留两位小数的浮点数
    print(f"age={age}, price={price:.2f}, active={active}, nothing={nothing}")


def demo_is_vs_eq():
    print("\n=== is vs == ===")
    a = [1, 2, 3]
    b = [1, 2, 3]  # 内容与 a 相同，但是新创建的对象
    c = a          # c 与 a 指向同一对象（同一引用）

    print(f"a == b: {a == b}")   # True：比较值（元素是否相等）
    print(f"a is b: {a is b}")   # False：比较身份（是否同一对象 id）
    print(f"a is c: {a is c}")   # True：c 是 a 的别名

    # CPython 对小整数 (-5~256) 做对象缓存，is 可能为 True
    x, y = 256, 256
    print(f"256 is 256: {x is y}")

    # 超出缓存范围时通常创建不同对象
    p, q = 257, 257
    print(f"257 is 257: {p is q}")  # CPython 下通常为 False


def demo_truthiness():
    print("\n=== 真值测试 ===")
    # 以下值在布尔上下文中均为 False（falsy）
    falsy = [0, 0.0, "", [], {}, set(), None, False]
    for v in falsy:
        # :8 左对齐占 8 字符宽；bool(v) 显式转为 True/False
        print(f"bool({v!r:8}) -> {bool(v)}")


def demo_fstrings():
    print("\n=== f-string ===")
    user = "Bob"
    score = 87.456
    print(f"用户 {user} 得分 {score:.1f}")  # :.1f 保留一位小数
    # Python 3.8+ 调试写法：同时输出表达式及其值
    print(f"表达式: {2 + 3 = }")


def main():
    print("=" * 50)   # 字符串 * 整数：重复 50 次
    print("01 - Hello Types")
    print("=" * 50)
    demo_basic_types()
    demo_is_vs_eq()
    demo_truthiness()
    demo_fstrings()
    print("\n[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
