"""
02_msg_blocks.py - Msg 与 ContentBlock

学习要点:
1. UserMsg / AssistantMsg 工厂
2. TextBlock、ToolCallBlock 等块结构
3. get_text_content() 提取文本
"""

from agentscope.message import TextBlock, UserMsg, AssistantMsg


def main():
    print("=" * 50)
    print("02 - Msg Blocks")
    print("=" * 50)

    user = UserMsg("alice", "查询发布流程")
    print(f"  user role={user.role} text={user.get_text_content()}")

    assistant = AssistantMsg(
        "bot",
        [TextBlock(text="我先查内部文档。")],
    )
    print(f"  assistant blocks={len(assistant.content)}")

    print("\n=== 约定 ===")
    print("  Agent 间只传 Msg，不裸传 str")
    print("  Tool 结果封装为 ToolResultBlock（由框架生成）")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
