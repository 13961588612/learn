"""
06_decorators.py - 函数装饰器、带参装饰器、functools

学习要点:
1. 装饰器本质是接受函数、返回函数的闭包
2. @wraps 保留原函数元信息
3. 带参装饰器多一层工厂函数
"""

import functools
import time
from typing import Callable, TypeVar

F = TypeVar("F", bound=Callable)


def timer(func: F) -> F:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start) * 1000
        print(f"  [{func.__name__}] {elapsed:.2f} ms")
        return result

    return wrapper  # type: ignore[return-value]


def repeat(times: int) -> Callable[[F], F]:
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result

        return wrapper  # type: ignore[return-value]

    return decorator


@timer
def compute_sum(n: int) -> int:
    return sum(range(n))


@repeat(times=2)
def greet(name: str) -> str:
    msg = f"Hello, {name}!"
    print(f"  {msg}")
    return msg


def main():
    print("=" * 50)
    print("06 - Decorators")
    print("=" * 50)

    print(f"\ncompute_sum(1_000_000) = {compute_sum(1_000_000)}")
    print("\n=== 带参装饰器 ===")
    greet("Python")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
