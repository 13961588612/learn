"""运行带审计 Middleware 的只读 Tool Agent"""

import asyncio
import importlib.util
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from agentscope.message import UserMsg  # noqa: E402
from agentscope.tool import FunctionTool, Toolkit  # noqa: E402

from _shared.audit_middleware import AuditMiddleware  # noqa: E402
from _shared.env import require_llm_or_guide  # noqa: E402
from _shared.runtime import build_agent  # noqa: E402

SHOWCASE = Path(__file__).resolve().parent
_tool_path = SHOWCASE / "src" / "tools" / "internal_docs.py"
_spec = importlib.util.spec_from_file_location("internal_docs", _tool_path)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
search_internal_docs = _mod.search_internal_docs


async def main_async():
    audit_dir = SHOWCASE / "audit_logs"
    tool = FunctionTool(search_internal_docs, is_read_only=True)
    toolkit = Toolkit(tools=[tool])
    agent = build_agent(
        name="audit-demo",
        system_prompt="你是内部助手。查文档必须用 search_internal_docs。",
        toolkit=toolkit,
        middlewares=[AuditMiddleware(audit_dir)],
    )
    reply = await agent.reply(UserMsg("user", "发布流程是什么？"))
    print(reply.get_text_content())
    print(f"\n  审计目录: {audit_dir}")


def main():
    print("=" * 50)
    print("Showcase 01 - Readonly Toolkit + Audit")
    print("=" * 50)
    if not require_llm_or_guide("showcase 01"):
        print("  离线演示 Tool:")
        print(" ", search_internal_docs("发布"))
        return
    asyncio.run(main_async())
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
