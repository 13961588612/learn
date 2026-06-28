"""
02_subagent_isolation.py - 子 Agent 上下文隔离

学习要点:
1. 每个子 Agent 独立 messages 列表
2. 主 Agent 只接收摘要，不泄漏全文
"""

from dataclasses import dataclass, field  # field 用于可变默认值（如 list）


@dataclass
class SubAgent:
    name: str
    # default_factory=list 每次实例化创建新列表，避免共享同一 list 对象
    messages: list[str] = field(default_factory=list)

    def run(self, task: str) -> str:
        # list.append 原地追加；子 Agent 内部消息不返回给主上下文
        self.messages.append(f"task: {task}")
        self.messages.append("... internal reasoning ...")
        # task[:30] 字符串切片取前 30 字符；... 表示截断
        summary = f"[{self.name}] 完成: {task[:30]}..."
        return summary  # 主 Agent 只收到摘要字符串


def main():
    print("=" * 50)
    print("02 - Subagent Isolation")
    print("=" * 50)

    research = SubAgent("research")  # dataclass 按字段顺序构造
    main_context: list[str] = ["user: 调研竞品 A 和 B"]  # 主 Agent 可见的上下文

    for topic in ("竞品 A", "竞品 B"):  # 元组可迭代
        summary = research.run(topic)
        main_context.append(summary)  # 只追加摘要，不追加 research.messages

    print(f"  主上下文条数: {len(main_context)}")       # len() 列表长度
    print(f"  子 Agent 内部条数: {len(research.messages)} (不进入主上下文)")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
