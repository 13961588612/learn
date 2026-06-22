"""03_openai_compatible.py - OpenAI 兼容 Gateway"""

import os

from agentscope.credential import OpenAICredential


def main():
    print("=" * 50)
    print("03 - OpenAI Compatible")
    print("=" * 50)
    base = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    print(f"  base_url 示例: {base}")
    cred = OpenAICredential(api_key="sk-demo", base_url=base)
    print(f"  credential type: {cred.type}")
    print("\n  公司 Gateway: 设 OPENAI_BASE_URL + OPENAI_API_KEY")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
