"""
05_post_tool_audit.py - PostToolUse 审计日志

学习要点:
1. 结构化 audit 事件（谁、何时、何 Tool、参数摘要）
2. 不记录全量敏感参数
"""

import json  # dumps 将 Python 对象序列化为 JSON 字符串
from dataclasses import asdict, dataclass, field  # asdict=实例转 dict；field=字段工厂
from datetime import datetime, timezone  # timezone.utc 表示 UTC 时区
from pathlib import Path  # 面向对象的路径操作


@dataclass
class AuditRecord:
    """单条审计记录的数据结构。"""

    ts: str              # ISO 格式时间戳
    tool: str            # Tool 名称
    user_id: str         # 操作用户 ID
    args_summary: dict   # 参数摘要（已截断）
    success: bool        # 是否成功
    result_preview: str = ""  # 带默认值的字段：未传参时使用 ""


@dataclass
class AuditLogger:
    """内存收集审计记录，flush 时写入文件。"""

    path: Path  # 输出文件路径
    # field(default_factory=list) 每个实例独立 list，避免可变默认参数陷阱
    records: list[AuditRecord] = field(default_factory=list)

    def post_tool_use(
        self,
        tool: str,
        user_id: str,
        args: dict,
        success: bool,
        result: str,
    ) -> None:
        """
        PostToolUse 回调：构造 AuditRecord 并追加到 records。
        -> None 表示无返回值。
        """
        # 字典推导：对字符串值超过 20 字符则截断并加 "..."
        summary = {k: (v[:20] + "..." if isinstance(v, str) and len(v) > 20 else v) for k, v in args.items()}
        rec = AuditRecord(
            ts=datetime.now(timezone.utc).isoformat(),  # UTC 当前时间 -> ISO 8601 字符串
            tool=tool,
            user_id=user_id,
            args_summary=summary,
            success=success,
            result_preview=result[:80],  # 切片取前 80 字符作为预览
        )
        self.records.append(rec)  # list.append 在末尾追加

    def flush(self) -> None:
        """将内存中的 records 写入 path 指定的 JSON 文件。"""
        # parents=True 创建中间目录；exist_ok 目录已存在不报错
        self.path.parent.mkdir(parents=True, exist_ok=True)
        # asdict 将 dataclass 实例递归转为普通 dict
        payload = [asdict(r) for r in self.records]
        # write_text 写字符串；ensure_ascii=False 保留中文；indent=2 美化缩进
        self.path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    """写入两条示例审计记录并 flush 到 data/。"""
    print("=" * 50)
    print("05 - PostToolUse Audit")
    print("=" * 50)

    # __file__ 当前脚本路径；.parent 父目录；/ 运算符拼接 Path
    log_path = Path(__file__).parent / "data" / "audit.jsonl.json"
    logger = AuditLogger(log_path)
    logger.post_tool_use("Read", "u001", {"path": "/project/README.md"}, True, "file content...")
    logger.post_tool_use("Write", "u001", {"path": "/prod/x"}, False, "permission denied")
    logger.flush()

    print(f"  审计记录 {len(logger.records)} 条 -> {log_path}")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
