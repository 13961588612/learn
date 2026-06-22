"""
02_inheritance.py - 继承、多态、super()、抽象基类 abc

学习要点:
1. 子类 override 父类方法实现多态
2. super() 调用父类实现
3. abc.ABC + @abstractmethod 定义接口
"""

from abc import ABC, abstractmethod


class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> str:
        ...


class EmailNotifier(Notifier):
    def send(self, message: str) -> str:
        return f"[EMAIL] {message}"


class SmsNotifier(Notifier):
    def send(self, message: str) -> str:
        return f"[SMS] {message}"


class LoggingNotifier(Notifier):
    """装饰器模式：包装另一个 Notifier 并记录日志"""

    def __init__(self, wrapped: Notifier):
        self.wrapped = wrapped

    def send(self, message: str) -> str:
        result = self.wrapped.send(message)
        return f"{result} (logged)"


def notify_all(notifiers: list[Notifier], message: str) -> None:
    for n in notifiers:
        print(n.send(message))


def main():
    print("=" * 50)
    print("02 - Inheritance")
    print("=" * 50)

    notifiers: list[Notifier] = [
        EmailNotifier(),
        LoggingNotifier(SmsNotifier()),
    ]
    notify_all(notifiers, "服务已重启")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
