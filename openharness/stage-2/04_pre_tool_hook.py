"""
04_pre_tool_hook.py - PreToolUse 拦截

学习要点:
1. Hook 在 execute 前运行
2. 敏感路径、写操作拦截
"""

from dataclasses import dataclass  # @dataclass 自动生成 __init__ 等样板方法
from typing import Callable  # Callable[[参数类型], 返回类型] 表示可调用对象


@dataclass
class ToolCall:
    """
    一次 Tool 调用的最小表示。
    @dataclass 根据类属性自动生成 __init__、__repr__ 等。
    """

    name: str       # Tool 名称，如 "Write"
    args: dict      # 参数字典，如 {"path": "/tmp/log.txt"}


# 元组字面量：不可变序列，适合常量前缀列表
SENSITIVE_PATHS = ("/etc", "/prod", ".env")


def pre_tool_use(call: ToolCall) -> tuple[bool, str]:
    """
    PreToolUse 钩子：执行前检查是否允许。
    返回 (allowed, reason) 元组；tuple[bool, str] 为类型注解。
    """
    if call.name == "Write":
        # .get(key, default) 安全取 dict 值，缺失时返回 default
        path = call.args.get("path", "")
        for prefix in SENSITIVE_PATHS:
            # str.startswith(prefix) 判断路径是否以敏感前缀开头
            if path.startswith(prefix):
                return False, f"blocked: 禁止写入 {path}"
    return True, "ok"


def run_with_hook(call: ToolCall, executor: Callable[[ToolCall], str]) -> str:
    """
    带 Hook 的执行包装：先 pre_tool_use，通过后再调用 executor。
    Callable[[ToolCall], str] 表示接收 ToolCall、返回 str 的函数。
    """
    # 元组解包：allowed 为 bool，reason 为 str
    allowed, reason = pre_tool_use(call)
    if not allowed:
        return f"ERROR: {reason}"
    return executor(call)  # 调用传入的执行函数


def main():
    """演示允许与拦截两种 Write 路径。"""
    print("=" * 50)
    print("04 - PreToolUse Hook")
    print("=" * 50)

    # 嵌套函数：fake_exec 仅在 main 内可见，模拟真实 Tool 执行
    def fake_exec(c: ToolCall) -> str:
        return f"written {c.args.get('path')}"

    # 列表字面量，元素为 ToolCall 实例
    cases = [
        ToolCall("Write", {"path": "/tmp/log.txt"}),
        ToolCall("Write", {"path": "/prod/config.yaml"}),
    ]
    for c in cases:
        print(f"\n  {c.name} {c.args} -> {run_with_hook(c, fake_exec)}")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
