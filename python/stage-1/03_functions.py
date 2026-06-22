"""
03_functions.py - 参数默认值、*args/**kwargs、lambda、作用域

学习要点:
1. 默认参数必须放在位置参数之后
2. *args 收集多余位置参数，**kwargs 收集多余关键字参数
3. lambda 仅适合单行简单表达式
4. LEGB 作用域规则（Local → Enclosing → Global → Built-in）
"""

from typing import Any


def greet(name: str, prefix: str = "Hello") -> str:
    return f"{prefix}, {name}!"


def demo_default_args():
    print("\n=== 默认参数 ===")
    print(greet("Alice"))
    print(greet("Bob", prefix="Hi"))


def sum_all(*args: int) -> int:
    return sum(args)


def demo_args():
    print("\n=== *args ===")
    print(f"sum_all(1,2,3) = {sum_all(1, 2, 3)}")


def build_profile(name: str, **kwargs: Any) -> dict[str, Any]:
    profile = {"name": name}
    profile.update(kwargs)
    return profile


def demo_kwargs():
    print("\n=== **kwargs ===")
    profile = build_profile("Carol", role="engineer", city="Shanghai")
    print(profile)


def demo_lambda():
    print("\n=== lambda ===")
    pairs = [("apple", 3), ("banana", 1), ("cherry", 2)]
    sorted_pairs = sorted(pairs, key=lambda x: x[1])
    print(f"按数量排序: {sorted_pairs}")


def demo_scope():
    print("\n=== 作用域 LEGB ===")
    x = "global"

    def outer():
        x = "enclosing"

        def inner():
            x = "local"
            print(f"  inner x = {x}")

        inner()
        print(f"  outer x = {x}")

    outer()
    print(f"global x = {x}")


def main():
    print("=" * 50)
    print("03 - Functions")
    print("=" * 50)
    demo_default_args()
    demo_args()
    demo_kwargs()
    demo_lambda()
    demo_scope()
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
