"""
10_stage1_final.py - 综合：迷你 Harness 模拟器

学习要点:
1. 串联 Loop + Permission + Hook + Tool Registry
2. P0 验收：理解 Query → Engine → Tool → Permission → Hook → Loop
"""

from dataclasses import dataclass, field  # @dataclass + field 处理可变默认值
from typing import Any, Callable           # Callable 标注工具函数签名


@dataclass
class AuditEvent:
    """单次工具调用的审计记录。"""
    tool: str
    allowed: bool
    detail: str


@dataclass
class MiniHarness:
    """
    迷你 Harness：工具注册表 + 权限 pre_hook + 审计日志。
    模拟 Query → Permission → Tool → Audit 链路。
    """
    tools: dict[str, Callable[[dict], str]]  # 工具名 -> 可调用对象
    # field(default_factory=...) 为 set/list 等可变类型提供独立默认实例
    denied_tools: set[str] = field(default_factory=lambda: {"Bash"})
    audit_log: list[AuditEvent] = field(default_factory=list)

    def pre_hook(self, name: str, args: dict) -> bool:
        """
        执行前钩子：denied_tools 中的工具直接拒绝。
        -> bool：True 允许继续，False 拦截。
        """
        if name in self.denied_tools:
            self.audit_log.append(AuditEvent(name, False, "denied by policy"))
            return False
        self.audit_log.append(AuditEvent(name, True, "pre_ok"))
        return True

    def execute(self, name: str, args: dict) -> str:
        """经 pre_hook 校验后调用 tools 注册表中的工具。"""
        if not self.pre_hook(name, args):
            return "ERROR: permission denied"
        if name not in self.tools:
            return f"ERROR: unknown tool {name}"
        result = self.tools[name](args)  # 调用注册的工具函数
        self.audit_log.append(AuditEvent(name, True, f"result_len={len(result)}"))
        return result

    def run_turn(self, tool_name: str, tool_args: dict) -> str:
        """单轮工具调用入口，委托给 execute。"""
        return self.execute(tool_name, tool_args)


def main():
    print("=" * 50)
    print("10 - Stage 1 Final")
    print("=" * 50)

    # 实例化 MiniHarness，tools 字典内嵌 lambda 匿名函数
    harness = MiniHarness(tools={
        "Read": lambda a: f"content of {a.get('path')}",   # a.get 安全取键
        "Grep": lambda a: f"matches in {a.get('pattern')}",
    })

    cases = [
        ("Read", {"path": "README.md"}),
        ("Bash", {"command": "ls"}),
        ("Unknown", {}),
    ]

    for name, args in cases:
        out = harness.run_turn(name, args)
        print(f"\n  {name} -> {out}")

    print("\n=== 审计日志 ===")
    for e in harness.audit_log:
        print(f"  {e.tool}: allowed={e.allowed} {e.detail}")

    print("\n[OK] 阶段一综合练习完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
