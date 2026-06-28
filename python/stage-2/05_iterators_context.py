"""
05_iterators_context.py - 迭代器、with、上下文管理器、contextlib

学习要点:
1. 实现 __iter__/__next__ 或使用 yield
2. with 语句调用 __enter__/__exit__
3. contextlib.contextmanager 简化上下文管理器
"""

from contextlib import contextmanager  # 用生成器快速写上下文管理器
from typing import Iterator


class Countdown:
    """自定义迭代器：实现 __iter__ 和 __next__"""

    def __init__(self, start: int):
        self.current = start

    def __iter__(self) -> "Countdown":
        return self  # 迭代器协议：__iter__ 返回迭代器对象本身

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration  # 迭代结束信号，for 循环会捕获并停止
        value = self.current
        self.current -= 1
        return value


class ManagedResource:
    """上下文管理器：支持 with 语句"""

    def __enter__(self) -> str:
        # with 块开始时调用；返回值赋给 as 后的变量
        print("  [resource] 打开")
        return "connection"

    def __exit__(self, exc_type, exc, tb) -> bool:
        # with 块结束时调用；exc_* 为异常信息（无异常时为 None）
        print("  [resource] 关闭")
        return False  # 返回 False/None：异常继续传播；True 则吞掉异常


@contextmanager
def temp_log(label: str) -> Iterator[None]:
    """
    @contextmanager 把含 yield 的生成器变为上下文管理器：
    yield 之前 = __enter__，yield 之后（finally）= __exit__
    """
    print(f"  [{label}] start")
    try:
        yield  # yield 处暂停，with 块在此执行
    finally:
        print(f"  [{label}] end")


def main():
    print("=" * 50)
    print("05 - Iterators & Context")
    print("=" * 50)

    print("\n=== 自定义迭代器 ===")
    print(list(Countdown(3)))  # list() 消费迭代器得到 [3, 2, 1]

    print("\n=== with 上下文 ===")
    with ManagedResource() as conn:
        print(f"  使用 {conn}")

    print("\n=== contextmanager ===")
    with temp_log("job"):
        print("  执行业务逻辑")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
