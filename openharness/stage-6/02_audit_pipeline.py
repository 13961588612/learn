"""
02_audit_pipeline.py - Hook -> 结构化审计 -> 存储
"""

import json                                    # dumps 序列化 dict；sort_keys 保证哈希稳定
from dataclasses import asdict, dataclass      # asdict 把 dataclass 转为 dict
from datetime import datetime, timezone        # timezone.utc 表示 UTC 时区


# @dataclass 装饰器：为审计记录字段自动生成 __init__ 等
@dataclass
class AuditRecord:
    ts: str          # ISO 8601 时间戳
    user_id: str
    tool: str        # 工具名
    allowed: bool    # 是否允许执行
    args_hash: str   # 参数摘要哈希（截断）


def emit_audit(user_id: str, tool: str, allowed: bool, args: dict) -> AuditRecord:
    return AuditRecord(
        datetime.now(timezone.utc).isoformat(),  # 当前 UTC 时间，isoformat() 转字符串
        user_id,
        tool,
        allowed,
        # hash(...) 整数哈希；str(...) 转字符串；[:12] 切片取前 12 字符
        str(hash(json.dumps(args, sort_keys=True)))[:12],
    )


def main():
    print("=" * 50)   # 字符串 * 整数：重复 50 次
    print("02 - Audit Pipeline")
    print("=" * 50)
    rec = emit_audit("u1", "Write", False, {"path": "/prod/x"})
    # asdict(rec) 转 dict；dumps 转 JSON；ensure_ascii=False 保留中文
    print(json.dumps(asdict(rec), ensure_ascii=False))
    print("\n[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
