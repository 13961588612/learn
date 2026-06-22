"""Lab 02: reply_stream 事件统计"""

import asyncio
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from _shared.env import require_llm_or_guide  # noqa: E402
from _shared.runtime import build_agent  # noqa: E402
from agentscope.message import UserMsg  # noqa: E402


async def _run():
    agent = build_agent(name="lab", system_prompt="简短回答。")
    counts: dict[str, int] = {}
    async for evt in agent.reply_stream(UserMsg("user", "说 hi")):
        name = type(evt).__name__
        counts[name] = counts.get(name, 0) + 1
    return counts


def main():
    print("=" * 50)
    print("Lab 02 - reply_stream events")
    print("=" * 50)
    if not require_llm_or_guide("reply_stream"):
        return
    counts = asyncio.run(_run())
    for k, v in sorted(counts.items()):
        print(f"  {k}: {v}")
    print("\n[OK] lab 02 完成")


if __name__ == "__main__":
    main()
