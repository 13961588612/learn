"""Pre/Post Tool 审计 Hook 原型"""

import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path


@dataclass
class AuditEvent:
    ts: str
    phase: str
    tool: str
    allowed: bool
    detail: str


class AuditHook:
    def __init__(self, log_path: Path):
        self.log_path = log_path
        self.events: list[AuditEvent] = []

    def pre_tool_use(self, tool: str, allowed: bool, detail: str = "") -> None:
        self.events.append(AuditEvent(
            datetime.now(timezone.utc).isoformat(), "pre", tool, allowed, detail
        ))

    def post_tool_use(self, tool: str, success: bool, preview: str = "") -> None:
        self.events.append(AuditEvent(
            datetime.now(timezone.utc).isoformat(), "post", tool, success, preview[:80]
        ))

    def flush(self) -> None:
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        lines = [json.dumps(asdict(e), ensure_ascii=False) for e in self.events]
        self.log_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    hook = AuditHook(Path(__file__).parent.parent.parent / "data" / "audit.log")
    hook.pre_tool_use("search_internal_docs", True)
    hook.post_tool_use("search_internal_docs", True, "found 2 docs")
    hook.flush()
    print(f"audit -> {hook.log_path}")
