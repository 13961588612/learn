"""
01_classes_basics.py - 类、实例、classmethod / staticmethod

学习要点:
1. __init__ 构造实例，self 指向当前实例
2. @classmethod 接收 cls，@staticmethod 无隐式首参
3. 对比 Java：Python 无 public/private 关键字，约定 _ 前缀表示内部
"""


class Counter:
    total_created = 0

    def __init__(self, name: str):
        self.name = name
        self.value = 0
        Counter.total_created += 1

    def increment(self, step: int = 1) -> None:
        self.value += step

    @classmethod
    def from_string(cls, raw: str) -> "Counter":
        name, value = raw.split(":")
        counter = cls(name=name)
        counter.value = int(value)
        return counter

    @staticmethod
    def is_positive(n: int) -> bool:
        return n > 0


def main():
    print("=" * 50)
    print("01 - Classes Basics")
    print("=" * 50)

    c1 = Counter("requests")
    c1.increment(3)
    print(f"{c1.name} = {c1.value}")

    c2 = Counter.from_string("errors:5")
    print(f"{c2.name} = {c2.value}")

    print(f"Counter.total_created = {Counter.total_created}")
    print(f"Counter.is_positive(-1) = {Counter.is_positive(-1)}")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
