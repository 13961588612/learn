"""
05_compaction_sim.py - 长会话 Auto-Compaction 模拟

学习要点:
1. 上下文超长时摘要旧消息
2. 保留最近 N 轮 + 摘要
"""

from dataclasses import dataclass


@dataclass
class Message:
    role: str
    content: str


def compact(messages: list[Message], keep_last: int = 4) -> list[Message]:
    if len(messages) <= keep_last:
        return messages
    old = messages[:-keep_last]
    recent = messages[-keep_last:]
    summary = Message("system", f"[Compacted {len(old)} messages: 早期对话已摘要]")
    return [summary] + recent


def main():
    print("=" * 50)
    print("05 - Compaction Sim")
    print("=" * 50)

    msgs = [Message("user" if i % 2 == 0 else "assistant", f"msg-{i}") for i in range(12)]
    print(f"  压缩前: {len(msgs)}")
    compacted = compact(msgs)
    print(f"  压缩后: {len(compacted)}")
    for m in compacted:
        print(f"    {m.role}: {m.content[:50]}")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
