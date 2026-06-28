"""
06_decorators.py - 函数装饰器、带参装饰器、functools

学习要点:
1. 装饰器本质是接受函数、返回函数的闭包
2. @wraps 保留原函数元信息
3. 带参装饰器多一层工厂函数
"""

import functools  # 提供 @wraps，把原函数的 __name__、__doc__ 等复制到 wrapper
import time       # perf_counter() 用于高精度计时
from typing import Callable, TypeVar  # Callable=可调用类型；TypeVar=泛型类型变量

# TypeVar("F", bound=Callable) 定义类型变量 F，约束为「任意可调用对象（函数）」
# 装饰器输入 func: F、输出 wrapper: F，类型检查器才能理解「装饰前后函数类型一致」
F = TypeVar("F", bound=Callable)


def timer(func: F) -> F:
    """
    无参装饰器：给 func 包一层，调用前后计时并打印耗时。
    类型 (func: F) -> F 表示：接收一个函数，返回同类型的包装函数。
    """

    # @functools.wraps(func) 装饰 wrapper，把 func 的元信息（__name__、__doc__ 等）复制过来
    # 否则 wrapper.__name__ 会是 "wrapper" 而不是原函数名
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # *args   收集所有位置参数为元组，如 (1, 2)
        # **kwargs 收集所有关键字参数为字典，如 {"key": "val"}
        # 这样 wrapper 能转发任意签名的原函数
        start = time.perf_counter()          # 返回浮点秒数，适合性能测量
        result = func(*args, **kwargs)       # 调用原函数；* / ** 解包转发参数
        elapsed = (time.perf_counter() - start) * 1000  # 转为毫秒
        # f-string：{func.__name__} 取函数名；{elapsed:.2f} 保留两位小数
        print(f"  [{func.__name__}] {elapsed:.2f} ms")
        return result  # 必须返回原函数结果，否则调用方拿不到返回值

    return wrapper  # type: ignore[return-value]
    # wrapper 与 F 在静态类型上不完全等价，用 ignore 抑制检查器告警


def repeat(times: int) -> Callable[[F], F]:
    """
    带参装饰器工厂：先接收配置 times，再返回真正的装饰器。
    返回类型 Callable[[F], F] 含义：
      - Callable[参数列表, 返回值]
      - [F] 表示装饰器接收一个类型为 F 的函数
      - 最后的 F 表示装饰器返回包装后的函数
    不能写 -> F，因为 repeat(2) 返回的是 decorator，还不是包装后的业务函数。
    """

    def decorator(func: F) -> F:
        # 这一层才是「标准装饰器」：(func: F) -> F

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            # range(times) 生成 0..times-1；_ 表示循环变量不使用
            for _ in range(times):
                result = func(*args, **kwargs)  # 重复调用，只保留最后一次返回值
            return result

        return wrapper  # type: ignore[return-value]

    return decorator  # repeat(times=2) 的返回值，等待下一步 decorator(greet)


# @timer 是语法糖，完全等价于：
#   def compute_sum(n: int) -> int: ...
#   compute_sum = timer(compute_sum)
@timer
def compute_sum(n: int) -> int:
    # n: int 参数注解；-> int 返回值注解（运行时不会强制校验，供 IDE / mypy 使用）
    return sum(range(n))  # range(n) 生成 0..n-1，再求和


# @repeat(times=2) 等价于：greet = repeat(times=2)(greet)
# 先调用 repeat(2) 得到 decorator，再 decorator(greet) 得到 wrapper
@repeat(times=2)
def greet(name: str) -> str:
    msg = f"Hello, {name}!"  # f-string 在字符串中嵌入变量
    print(f"  {msg}")
    return msg


def main():
    print("=" * 50)   # 字符串 * 整数：重复 50 次
    print("06 - Decorators")
    print("=" * 50)

    # 1_000_000 中下划线仅为可读性，值等于 1000000
    print(f"\ncompute_sum(1_000_000) = {compute_sum(1_000_000)}")
    print("\n=== 带参装饰器 ===")
    greet("Python")  # 因 times=2，内部会打印两次 Hello
    print("\n[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
