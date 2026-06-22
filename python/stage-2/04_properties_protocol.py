"""
04_properties_protocol.py - @property、描述符入门、Protocol 预览

学习要点:
1. @property 把方法暴露为只读属性
2. Protocol 结构化子类型（duck typing + 类型检查）
"""

from typing import Protocol, runtime_checkable


class SupportsArea(Protocol):
    def area(self) -> float: ...


@runtime_checkable
class Drawable(Protocol):
    def draw(self) -> str: ...


class Rectangle:
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height

    @property
    def width(self) -> float:
        return self._width

    @property
    def area(self) -> float:
        return self._width * self._height


class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2

    def draw(self) -> str:
        return f"Circle(r={self.radius})"


def print_area(shape: SupportsArea) -> None:
    print(f"  area = {shape.area():.2f}")


def main():
    print("=" * 50)
    print("04 - Properties & Protocol")
    print("=" * 50)

    rect = Rectangle(4, 5)
    print(f"rect.width={rect.width}, rect.area={rect.area}")

    shapes: list[SupportsArea] = [rect, Circle(2)]
    for s in shapes:
        print_area(s)

    c = Circle(1)
    print(f"is Drawable: {isinstance(c, Drawable)}")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
