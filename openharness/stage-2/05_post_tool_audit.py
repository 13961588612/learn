"""
05_post_tool_audit.py - PostToolUse 审计日志

学习要点:
1. 结构化 audit 事件（谁、何时、何 Tool、参数摘要）
2. 不记录全量敏感参数
"""

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path


@dataclass
class AuditRecord:
    ts: str
    tool: str
    user_id: str
    args_summary: dict
    success: bool
    result_preview: str = ""


@dataclass
class AuditLogger:
    path: Path
    records: list[AuditRecord] = field(default_factory=list)

    def post_tool_use(
        self,
        tool: str,
        user_id: str,
        args: dict,
        success: bool,
        result: str,
    ) -> None:
        summary = {k: (v[:20] + "..." if isinstance(v, str) and len(v) > 20 else v) for k, v in args.items()}
        rec = AuditRecord(
            ts=datetime.now(timezone.utc).isoformat(),
            tool=tool,
            user_id=user_id,
            args_summary=summary,
            success=success,
            result_preview=result[:80],
        )
        self.records.append(rec)

    def flush(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        payload = [asdict(r) for r in self.records]
        self.path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    print("=" * 50)
    print("05 - PostToolUse Audit")
    print("=" * 50)

    log_path = Path(__file__).parent / "data" / "audit.jsonl.json"
    logger = AuditLogger(log_path)
    logger.post_tool_use("Read", "u001", {"path": "/project/README.md"}, True, "file content...")
    logger.post_tool_use("Write", "u001", {"path": "/prod/x"}, False, "permission denied")
    logger.flush()

    print(f"  审计记录 {len(logger.records)} 条 -> {log_path}")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
