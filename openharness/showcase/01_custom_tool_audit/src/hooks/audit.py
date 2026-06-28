"""Pre/Post Tool 审计 Hook 原型"""

import json                                    # dumps 序列化为 JSON 行
from dataclasses import asdict, dataclass      # asdict 把 dataclass 转为 dict
from datetime import datetime, timezone        # timezone.utc 表示 UTC 时区
from pathlib import Path                       # 面向对象的路径 API


# @dataclass 装饰器：为审计事件字段自动生成 __init__ 等
@dataclass
class AuditEvent:
    ts: str       # ISO 8601 时间戳
    phase: str    # "pre" 或 "post"
    tool: str
    allowed: bool
    detail: str


class AuditHook:
    def __init__(self, log_path: Path):
        self.log_path = log_path
        self.events: list[AuditEvent] = []  # 类型注解 list[AuditEvent]；内存中累积事件

    def pre_tool_use(self, tool: str, allowed: bool, detail: str = "") -> None:
        # -> None 表示无返回值；detail 默认空字符串
        self.events.append(AuditEvent(
            datetime.now(timezone.utc).isoformat(), "pre", tool, allowed, detail
        ))

    def post_tool_use(self, tool: str, success: bool, preview: str = "") -> None:
        self.events.append(AuditEvent(
            datetime.now(timezone.utc).isoformat(), "post", tool, success, preview[:80]
            # preview[:80] 切片：只保留前 80 字符，避免日志过长
        ))

    def flush(self) -> None:
        self.log_path.parent.mkdir(parents=True, exist_ok=True)
        # 列表推导：每条事件 asdict 后 dumps 为一行 JSON
        lines = [json.dumps(asdict(e), ensure_ascii=False) for e in self.events]
        # write_text 写文件；"\n".join 用换行连接；末尾加 \n
        self.log_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    # Path(__file__) 当前文件；parent 链向上到 showcase 根，再 / data / audit.log
    hook = AuditHook(Path(__file__).parent.parent.parent / "data" / "audit.log")
    hook.pre_tool_use("search_internal_docs", True)
    hook.post_tool_use("search_internal_docs", True, "found 2 docs")
    hook.flush()  # 把内存事件写入磁盘
    print(f"audit -> {hook.log_path}")
