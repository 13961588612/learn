"""Post-tool 审计 Middleware 示例 — showcase / stage-2 二开参考"""

from __future__ import annotations

import json
from collections.abc import AsyncGenerator, Callable
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from agentscope.middleware import MiddlewareBase


class AuditMiddleware(MiddlewareBase):
    """在 on_acting 记录 tool 调用摘要（脱敏）"""

    def __init__(self, log_dir: Path | None = None) -> None:
        self.log_dir = log_dir
        if log_dir:
            log_dir.mkdir(parents=True, exist_ok=True)

    async def on_acting(
        self,
        agent: Any,
        input_kwargs: dict,
        next_handler: Callable[..., AsyncGenerator],
    ) -> AsyncGenerator:
        tool = input_kwargs.get("tool")
        tool_name = getattr(tool, "name", "unknown")
        async for event in next_handler():
            yield event
        if self.log_dir is None:
            return
        record = {
            "ts": datetime.now(timezone.utc).isoformat(),
            "agent": agent.name,
            "tool": tool_name,
        }
        path = self.log_dir / f"audit_{datetime.now(timezone.utc).strftime('%Y%m%d')}.jsonl"
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
