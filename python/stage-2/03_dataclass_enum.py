"""
03_dataclass_enum.py - dataclasses、Enum、NamedTuple

学习要点:
1. @dataclass 自动生成 __init__、__repr__ 等
2. Enum 表达有限状态集合
3. NamedTuple 轻量不可变记录
"""

from dataclasses import dataclass, field  # field 用于复杂默认值（如可变 list）
from enum import Enum, auto              # auto() 自动分配递增整数值
from typing import NamedTuple            # 带字段名的 tuple 子类


class OrderStatus(Enum):
    # 枚举成员：PENDING、PAID 等是 OrderStatus 的实例，不是普通 str
    PENDING = auto()
    PAID = auto()
    SHIPPED = auto()
    CANCELLED = auto()


class Point(NamedTuple):
    # NamedTuple：不可变、可通过 p.x 访问字段（类似轻量 dataclass）
    x: int
    y: int


@dataclass
class Order:
    # @dataclass 自动生成 __init__、__repr__、__eq__ 等
    id: int
    product: str
    status: OrderStatus = OrderStatus.PENDING  # 不可变默认值可直接写
    # 可变默认值必须用 default_factory，否则所有实例共享同一 list
    tags: list[str] = field(default_factory=list)


def main():
    print("=" * 50)
    print("03 - Dataclass & Enum")
    print("=" * 50)

    o = Order(id=1, product="Keyboard", tags=["device"])
    print(f"Order: {o}")  # dataclass 自动生成可读 __repr__

    o.status = OrderStatus.PAID
    print(f"status = {o.status.name}")  # .name 取枚举成员名 "PAID"

    p = Point(3, 4)  # NamedTuple 按位置传参
    print(f"Point: {p}, x={p.x}")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
