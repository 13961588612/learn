"""
04_properties_protocol.py - @property、描述符入门、Protocol 预览

学习要点:
1. @property 把方法暴露为只读属性
2. Protocol 结构化子类型（duck typing + 类型检查）
"""

from typing import Protocol, runtime_checkable  # Protocol 定义结构化接口


class SupportsArea(Protocol):
    """只要实现了 area() 方法，静态类型检查就视为 SupportsArea（鸭子类型 + 类型）"""
    def area(self) -> float: ...


@runtime_checkable
class Drawable(Protocol):
    """加 @runtime_checkable 后可用 isinstance(obj, Drawable) 做运行时检查"""
    def draw(self) -> str: ...


class Rectangle:
    def __init__(self, width: float, height: float):
        self._width = width   # 单下划线：约定为内部属性
        self._height = height

    @property
    def width(self) -> float:
        # @property 把方法变为只读属性：rect.width 而非 rect.width()
        return self._width

    @property
    def area(self) -> float:
        return self._width * self._height


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2  # ** 幂运算

    def draw(self) -> str:
        return f"Circle(r={self.radius})"


def print_area(shape: SupportsArea) -> None:
    # 参数类型 SupportsArea：Circle 和 Rectangle 都满足（有 area 方法）
    print(f"  area = {shape.area():.2f}")


def main():
    print("=" * 50)
    print("04 - Properties & Protocol")
    print("=" * 50)

    rect = Rectangle(4, 5)
    print(f"rect.width={rect.width}, rect.area={rect.area}")  # 属性式访问

    shapes: list[SupportsArea] = [rect, Circle(2)]
    for s in shapes:
        print_area(s)

    c = Circle(1)
    print(f"is Drawable: {isinstance(c, Drawable)}")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
