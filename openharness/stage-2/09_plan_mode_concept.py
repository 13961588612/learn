"""
09_plan_mode_concept.py - default vs plan 模式

学习要点:
1. plan 模式：大改前先输出计划，用户确认后再执行写操作
2. default：写操作需逐项确认
"""

from enum import Enum  # Enum 定义一组命名常量，成员可比较、可迭代


class PermissionMode(str, Enum):
    """
    权限模式枚举。继承 str 使成员值同时是 str，便于 JSON 序列化。
    成员名大写，值为小写字符串。
    """

    DEFAULT = "default"
    AUTO = "auto"
    PLAN = "plan"


def should_auto_approve(mode: PermissionMode, tool: str, is_write: bool) -> bool:
    """
    判断给定模式下 Tool 调用是否可自动批准（无需用户确认）。
    is_write=True 表示写类操作（Write、Edit 等）。
    """
    if mode == PermissionMode.AUTO:
        return True  # 全自动模式：全部放行
    if mode == PermissionMode.PLAN and not is_write:
        return True  # plan 模式：只读自动，写需计划批准后
    return False  # default 或 plan 下的写操作需确认


def main():
    """遍历三种模式，对比 Read/Write 是否自动批准。"""
    print("=" * 50)
    print("09 - Plan Mode Concept")
    print("=" * 50)

    # 直接迭代 Enum 类得到所有成员
    for mode in PermissionMode:
        read_ok = should_auto_approve(mode, "Read", False)
        write_ok = should_auto_approve(mode, "Write", True)
        # {mode.value:8} 取枚举的 str 值并左对齐宽 8
        print(f"  {mode.value:8} Read={read_ok} Write={write_ok}")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
