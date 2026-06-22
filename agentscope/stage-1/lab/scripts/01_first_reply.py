"""Lab 01: 首次 Agent.reply"""

import asyncio
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from _shared.env import require_llm_or_guide  # noqa: E402
from _shared.runtime import build_agent  # noqa: E402
from agentscope.message import UserMsg  # noqa: E402

LAB_DIR = Path(__file__).resolve().parents[1]


async def _run():
    agent = build_agent(
        name="lab-assistant",
        system_prompt="你是学习助手，用简体中文简短回答。",
    )
    msg = UserMsg("user", "用一句话介绍 AgentScope。")
    reply = await agent.reply(msg)
    return reply.get_text_content()


def main():
    print("=" * 50)
    print("Lab 01 - first reply")
    print("=" * 50)
    if not require_llm_or_guide("Agent.reply"):
        return
    text = asyncio.run(_run())
    print(f"  回复: {text[:200]}")
    out = LAB_DIR / "experiments"
    out.mkdir(exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    (out / f"first_reply_{ts}.json").write_text(
        json.dumps({"reply": text}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print("\n[OK] lab 01 完成")


if __name__ == "__main__":
    main()
