"""
09_plan_mode_concept.py - default vs plan 模式

学习要点:
1. plan 模式：大改前先输出计划，用户确认后再执行写操作
2. default：写操作需逐项确认
"""

from enum import Enum


class PermissionMode(str, Enum):
    DEFAULT = "default"
    AUTO = "auto"
    PLAN = "plan"


def should_auto_approve(mode: PermissionMode, tool: str, is_write: bool) -> bool:
    if mode == PermissionMode.AUTO:
        return True
    if mode == PermissionMode.PLAN and not is_write:
        return True  # 只读自动，写需计划批准后
    return False


def main():
    print("=" * 50)
    print("09 - Plan Mode Concept")
    print("=" * 50)

    for mode in PermissionMode:
        read_ok = should_auto_approve(mode, "Read", False)
        write_ok = should_auto_approve(mode, "Write", True)
        print(f"  {mode.value:8} Read={read_ok} Write={write_ok}")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
