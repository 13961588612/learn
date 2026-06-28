"""
01_classes_basics.py - 类、实例、classmethod / staticmethod

学习要点:
1. __init__ 构造实例，self 指向当前实例
2. @classmethod 接收 cls，@staticmethod 无隐式首参
3. 对比 Java：Python 无 public/private 关键字，约定 _ 前缀表示内部
"""


class Counter:
    # 类变量：所有实例共享
    total_created = 0

    def __init__(self, name: str):
        # self 指向当前实例；__init__ 在实例化时自动调用
        self.name = name      # 实例属性
        self.value = 0
        Counter.total_created += 1  # 通过类名访问类变量

    def increment(self, step: int = 1) -> None:
        # 实例方法：第一个参数必须是 self
        self.value += step

    @classmethod
    def from_string(cls, raw: str) -> "Counter":
        # classmethod：首参 cls 是类本身，常用于替代构造器
        name, value = raw.split(":")  # 解包 split 结果
        counter = cls(name=name)      # cls(...) 等价于 Counter(...)
        counter.value = int(value)
        return counter

    @staticmethod
    def is_positive(n: int) -> bool:
        # staticmethod：无 self/cls，逻辑上属于类命名空间但不依赖实例或类状态
        return n > 0


def main():
    print("=" * 50)
    print("01 - Classes Basics")
    print("=" * 50)

    c1 = Counter("requests")  # 调用 Counter.__init__
    c1.increment(3)           # 等价于 Counter.increment(c1, 3)
    print(f"{c1.name} = {c1.value}")

    c2 = Counter.from_string("errors:5")  # 类方法构造
    print(f"{c2.name} = {c2.value}")

    print(f"Counter.total_created = {Counter.total_created}")
    print(f"Counter.is_positive(-1) = {Counter.is_positive(-1)}")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
