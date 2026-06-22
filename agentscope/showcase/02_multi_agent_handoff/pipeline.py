"""Researcher -> Writer 双 Agent handoff"""

import asyncio
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from agentscope.message import UserMsg  # noqa: E402
from _shared.env import require_llm_or_guide  # noqa: E402
from _shared.runtime import build_agent  # noqa: E402


async def run_pipeline(task: str) -> str:
    researcher = build_agent(
        name="researcher",
        system_prompt="你是调研员。用 3 条 bullet 列出要点，不要写长文。",
    )
    writer = build_agent(
        name="writer",
        system_prompt="你是写作者。根据上一条 assistant 消息写 80 字摘要。",
    )
    research_msg = await researcher.reply(UserMsg("user", task))
    await writer.observe(research_msg)
    final = await writer.reply(None)
    return final.get_text_content()


def main():
    print("=" * 50)
    print("Showcase 02 - Multi-Agent Handoff")
    print("=" * 50)
    if not require_llm_or_guide("multi-agent"):
        print("  离线: researcher -> writer handoff 见 stage-4/02")
        return
    text = asyncio.run(run_pipeline("AgentScope 2.x 核心模块有哪些？"))
    print(text)
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
