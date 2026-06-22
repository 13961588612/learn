"""
02_subagent_isolation.py - 子 Agent 上下文隔离

学习要点:
1. 每个子 Agent 独立 messages 列表
2. 主 Agent 只接收摘要，不泄漏全文
"""

from dataclasses import dataclass, field


@dataclass
class SubAgent:
    name: str
    messages: list[str] = field(default_factory=list)

    def run(self, task: str) -> str:
        self.messages.append(f"task: {task}")
        self.messages.append("... internal reasoning ...")
        summary = f"[{self.name}] 完成: {task[:30]}..."
        return summary


def main():
    print("=" * 50)
    print("02 - Subagent Isolation")
    print("=" * 50)

    research = SubAgent("research")
    main_context: list[str] = ["user: 调研竞品 A 和 B"]

    for topic in ("竞品 A", "竞品 B"):
        summary = research.run(topic)
        main_context.append(summary)

    print(f"  主上下文条数: {len(main_context)}")
    print(f"  子 Agent 内部条数: {len(research.messages)} (不进入主上下文)")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
