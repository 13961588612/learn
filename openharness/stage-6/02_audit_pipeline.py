"""
02_audit_pipeline.py - Hook -> 结构化审计 -> 存储
"""

import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone


@dataclass
class AuditRecord:
    ts: str
    user_id: str
    tool: str
    allowed: bool
    args_hash: str


def emit_audit(user_id: str, tool: str, allowed: bool, args: dict) -> AuditRecord:
    return AuditRecord(
        datetime.now(timezone.utc).isoformat(),
        user_id,
        tool,
        allowed,
        str(hash(json.dumps(args, sort_keys=True)))[:12],
    )


def main():
    print("=" * 50)
    print("02 - Audit Pipeline")
    print("=" * 50)
    rec = emit_audit("u1", "Write", False, {"path": "/prod/x"})
    print(json.dumps(asdict(rec), ensure_ascii=False))
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
