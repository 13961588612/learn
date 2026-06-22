"""01_model_providers.py - 支持的 ChatModel 列表"""

PROVIDERS = [
    "OpenAIChatModel",
    "DashScopeChatModel",
    "DeepSeekChatModel",
    "AnthropicChatModel",
    "GeminiChatModel",
    "OllamaChatModel",
    "MoonshotChatModel",
]


def main():
    print("=" * 50)
    print("01 - Model Providers")
    print("=" * 50)
    for p in PROVIDERS:
        print(f"  - {p}")
    print("\n  工厂: _shared/runtime.build_chat_model()")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
