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
    age: int = 30
    price: float = 19.99
    name: str = "Alice"
    active: bool = True
    nothing = None

    print(f"name={name!r}, type={type(name).__name__}")
    print(f"age={age}, price={price:.2f}, active={active}, nothing={nothing}")


def demo_is_vs_eq():
    print("\n=== is vs == ===")
    a = [1, 2, 3]
    b = [1, 2, 3]
    c = a

    print(f"a == b: {a == b}")   # True，值相同
    print(f"a is b: {a is b}")   # False，不是同一对象
    print(f"a is c: {a is c}")   # True，同一引用

    # 小整数缓存：Python 会复用 -5~256 的 int 对象
    x, y = 256, 256
    print(f"256 is 256: {x is y}")

    p, q = 257, 257
    print(f"257 is 257: {p is q}")  # CPython 下通常为 False


def demo_truthiness():
    print("\n=== 真值测试 ===")
    falsy = [0, 0.0, "", [], {}, set(), None, False]
    for v in falsy:
        print(f"bool({v!r:8}) -> {bool(v)}")


def demo_fstrings():
    print("\n=== f-string ===")
    user = "Bob"
    score = 87.456
    print(f"用户 {user} 得分 {score:.1f}")
    print(f"表达式: {2 + 3 = }")  # Python 3.8+ 调试写法


def main():
    print("=" * 50)
    print("01 - Hello Types")
    print("=" * 50)
    demo_basic_types()
    demo_is_vs_eq()
    demo_truthiness()
    demo_fstrings()
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
