"""
02_typing_advanced.py - Generic、Literal、TypedDict、Callable

学习要点:
1. Generic 让容器类型携带元素类型信息
2. Literal 限定为若干固定字面量值
3. TypedDict 描述 dict 的键与值类型（结构化字典）
4. Callable[[参数类型...], 返回类型] 描述函数签名
"""

from typing import Callable, Generic, Literal, TypedDict, TypeVar

T = TypeVar("T")  # 泛型类型变量


class Box(Generic[T]):
    """Generic[T]：Box 可装任意类型，且类型检查器能追踪内部元素类型"""

    def __init__(self, value: T) -> None:
        self.value = value

    def get(self) -> T:
        return self.value


class UserRow(TypedDict):
    # TypedDict：类似「带固定键的 dict」，比 dataclass 轻，常用于 JSON 解析中间态
    id: int
    name: str
    role: Literal["admin", "editor", "viewer"]  # 只能是这三个字符串之一


def apply_twice(fn: Callable[[int], int], value: int) -> int:
    # Callable[[int], int]：接收 int、返回 int 的可调用对象
    return fn(fn(value))


def demo_generic():
    print("\n=== Generic ===")
    int_box = Box(42)
    str_box = Box("hello")
    print(f"int_box.get() = {int_box.get()}, type hint 为 int")
    print(f"str_box.get() = {str_box.get()!r}, type hint 为 str")


def demo_literal_typeddict():
    print("\n=== Literal / TypedDict ===")
    row: UserRow = {"id": 1, "name": "Alice", "role": "admin"}
    print(f"UserRow: {row}")
    # row["role"] = "guest"  # mypy 会报错：不在 Literal 允许范围内


def demo_callable():
    print("\n=== Callable ===")
    result = apply_twice(lambda x: x + 1, 10)
    print(f"apply_twice(x+1, 10) = {result}")


def main():
    print("=" * 50)
    print("02 - Typing Advanced")
    print("=" * 50)
    demo_generic()
    demo_literal_typeddict()
    demo_callable()
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
