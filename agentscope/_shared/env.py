"""环境变量与 API 可用性检测 — 各 stage lab 共用"""

from __future__ import annotations

import os
from pathlib import Path

from dotenv import load_dotenv

AGENTSCOPE_ROOT = Path(__file__).resolve().parents[1]
LEARN_ROOT = AGENTSCOPE_ROOT.parent


def load_env() -> None:
    """加载 learn 根与 agentscope 轨道的 .env"""
    load_dotenv(LEARN_ROOT / ".env", override=False)
    load_dotenv(AGENTSCOPE_ROOT / ".env", override=False)


def has_openai() -> bool:
    load_env()
    return bool(os.getenv("OPENAI_API_KEY"))


def has_dashscope() -> bool:
    load_env()
    return bool(os.getenv("DASHSCOPE_API_KEY"))


def has_any_llm() -> bool:
    return has_openai() or has_dashscope()


def require_llm_or_guide(step: str) -> bool:
    if has_any_llm():
        return True
    print(f"  [跳过] {step}")
    print("  配置: 复制 agentscope/.env.example -> .env")
    print("  填写 OPENAI_API_KEY 或 DASHSCOPE_API_KEY")
    print("  安装: uv sync --group agentscope-core")
    return False
