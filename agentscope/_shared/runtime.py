"""AgentScope 2.x 运行时工厂 — lab 与 showcase 共用"""

from __future__ import annotations

import os

from agentscope.agent import Agent
from agentscope.credential import DashScopeCredential, OpenAICredential
from agentscope.model import DashScopeChatModel, OpenAIChatModel
from agentscope.tool import Toolkit

from .env import load_env


def build_chat_model():
    """按可用 Key 创建 ChatModel（优先 OpenAI，其次 DashScope）"""
    load_env()
    if os.getenv("OPENAI_API_KEY"):
        cred = OpenAICredential(api_key=os.environ["OPENAI_API_KEY"])
        base_url = os.getenv("OPENAI_BASE_URL")
        if base_url:
            cred = OpenAICredential(
                api_key=os.environ["OPENAI_API_KEY"],
                base_url=base_url,
            )
        model_name = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
        return OpenAIChatModel(credential=cred, model=model_name, stream=True)
    if os.getenv("DASHSCOPE_API_KEY"):
        cred = DashScopeCredential(api_key=os.environ["DASHSCOPE_API_KEY"])
        model_name = os.getenv("DASHSCOPE_MODEL", "qwen-plus")
        return DashScopeChatModel(credential=cred, model=model_name, stream=True)
    raise RuntimeError("未配置 OPENAI_API_KEY 或 DASHSCOPE_API_KEY")


def build_agent(
    name: str,
    system_prompt: str,
    toolkit: Toolkit | None = None,
    **kwargs,
) -> Agent:
    model = build_chat_model()
    return Agent(
        name=name,
        system_prompt=system_prompt,
        model=model,
        toolkit=toolkit or Toolkit(),
        **kwargs,
    )
