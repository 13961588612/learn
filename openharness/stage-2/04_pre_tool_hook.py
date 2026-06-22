"""
04_pre_tool_hook.py - PreToolUse 拦截

学习要点:
1. Hook 在 execute 前运行
2. 敏感路径、写操作拦截
"""

from dataclasses import dataclass
from typing import Callable


@dataclass
class ToolCall:
    name: str
    args: dict


SENSITIVE_PATHS = ("/etc", "/prod", ".env")


def pre_tool_use(call: ToolCall) -> tuple[bool, str]:
    if call.name == "Write":
        path = call.args.get("path", "")
        for prefix in SENSITIVE_PATHS:
            if path.startswith(prefix):
                return False, f"blocked: 禁止写入 {path}"
    return True, "ok"


def run_with_hook(call: ToolCall, executor: Callable[[ToolCall], str]) -> str:
    allowed, reason = pre_tool_use(call)
    if not allowed:
        return f"ERROR: {reason}"
    return executor(call)


def main():
    print("=" * 50)
    print("04 - PreToolUse Hook")
    print("=" * 50)

    def fake_exec(c: ToolCall) -> str:
        return f"written {c.args.get('path')}"

    cases = [
        ToolCall("Write", {"path": "/tmp/log.txt"}),
        ToolCall("Write", {"path": "/prod/config.yaml"}),
    ]
    for c in cases:
        print(f"\n  {c.name} {c.args} -> {run_with_hook(c, fake_exec)}")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
