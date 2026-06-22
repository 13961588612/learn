"""
05_iterators_context.py - 迭代器、with、上下文管理器、contextlib

学习要点:
1. 实现 __iter__/__next__ 或使用 yield
2. with 语句调用 __enter__/__exit__
3. contextlib.contextmanager 简化上下文管理器
"""

from contextlib import contextmanager
from typing import Iterator


class Countdown:
    def __init__(self, start: int):
        self.current = start

    def __iter__(self) -> "Countdown":
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


class ManagedResource:
    def __enter__(self) -> str:
        print("  [resource] 打开")
        return "connection"

    def __exit__(self, exc_type, exc, tb) -> bool:
        print("  [resource] 关闭")
        return False  # 不吞掉异常


@contextmanager
def temp_log(label: str) -> Iterator[None]:
    print(f"  [{label}] start")
    try:
        yield
    finally:
        print(f"  [{label}] end")


def main():
    print("=" * 50)
    print("05 - Iterators & Context")
    print("=" * 50)

    print("\n=== 自定义迭代器 ===")
    print(list(Countdown(3)))

    print("\n=== with 上下文 ===")
    with ManagedResource() as conn:
        print(f"  使用 {conn}")

    print("\n=== contextmanager ===")
    with temp_log("job"):
        print("  执行业务逻辑")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
