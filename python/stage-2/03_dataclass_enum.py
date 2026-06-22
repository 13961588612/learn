"""
03_dataclass_enum.py - dataclasses、Enum、NamedTuple

学习要点:
1. @dataclass 自动生成 __init__、__repr__ 等
2. Enum 表达有限状态集合
3. NamedTuple 轻量不可变记录
"""

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import NamedTuple


class OrderStatus(Enum):
    PENDING = auto()
    PAID = auto()
    SHIPPED = auto()
    CANCELLED = auto()


class Point(NamedTuple):
    x: int
    y: int


@dataclass
class Order:
    id: int
    product: str
    status: OrderStatus = OrderStatus.PENDING
    tags: list[str] = field(default_factory=list)


def main():
    print("=" * 50)
    print("03 - Dataclass & Enum")
    print("=" * 50)

    o = Order(id=1, product="Keyboard", tags=["device"])
    print(f"Order: {o}")

    o.status = OrderStatus.PAID
    print(f"status = {o.status.name}")

    p = Point(3, 4)
    print(f"Point: {p}, x={p.x}")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
