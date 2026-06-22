"""
model.py - 统一模型工厂函数

提供 getModel(temperature) 函数，返回配置好的聊天模型实例。
优先 DeepSeek，回退 OpenAI。
"""

import os
from dotenv import load_dotenv

load_dotenv()

from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI


def getModel(temperature: float = 0.7):
    """获取聊天模型实例（DeepSeek 优先，OpenAI 回退）"""
    deepseek_key = os.getenv("DEEPSEEK_API_KEY")
    if deepseek_key:
        base_url = os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com")
        try:
            from langchain_deepseek import ChatDeepSeek

            return ChatDeepSeek(
                model="deepseek-chat",
                api_key=deepseek_key,
                temperature=temperature,
            )  # type: ignore[no-any-return]
        except ImportError:
            return ChatOpenAI(
                model="deepseek-chat",
                base_url=base_url + "/v1" if not base_url.endswith("/v1") else base_url,
                api_key=deepseek_key,
                temperature=temperature,
            )

    openai_key = os.getenv("OPENAI_API_KEY")
    if openai_key:
        return init_chat_model("openai:gpt-4o-mini", temperature=temperature)

    raise ValueError(
        "请在 .env 中配置 DEEPSEEK_API_KEY 或 OPENAI_API_KEY\n"
        "可从 ../stage-1/.env 复制配置"
    )
