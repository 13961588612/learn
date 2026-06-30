"""
05_compaction_sim.py - 长会话 Auto-Compaction 模拟

学习要点:
1. 上下文超长时摘要旧消息
2. 保留最近 N 轮 + 摘要
"""

from dataclasses import dataclass


@dataclass
class Message:
    role: str      # "user" | "assistant" | "system"
    content: str


def compact(messages: list[Message], keep_last: int = 4) -> list[Message]:
    # keep_last=4 默认保留最近 4 条；带默认值的参数可省略
    if len(messages) <= keep_last:
        return messages  # 未超长则原样返回（同一列表对象）
    # 负索引切片：[:-keep_last] 除最后 keep_last 条外的全部
    old = messages[:-keep_last]  # list[Message]
    # [-keep_last:] 最后 keep_last 条
    recent = messages[-keep_last:]  # list[Message]
    summary = Message("system", f"[Compacted {len(old)} messages: 早期对话已摘要]")  # Message
    # [summary] + recent 列表拼接，摘要放最前
    return [summary] + recent


def main():
    print("=" * 50)
    print("05 - Compaction Sim")
    print("=" * 50)

    # 列表推导式：[表达式 for 变量 in 可迭代 if 条件]
    # i % 2 == 0 偶数索引为 user，奇数为 assistant
    msgs = [Message("user" if i % 2 == 0 else "assistant", f"msg-{i}") for i in range(12)]  # list[Message]
    print(f"  压缩前: {len(msgs)}")
    compacted = compact(msgs)  # list[Message]
    print(f"  压缩后: {len(compacted)}")
    for m in compacted:  # Message
        print(f"    {m.role}: {m.content[:50]}")  # [:50] 截断显示

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
