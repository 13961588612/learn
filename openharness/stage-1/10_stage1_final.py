"""
10_stage1_final.py - 综合：迷你 Harness 模拟器

学习要点:
1. 串联 Loop + Permission + Hook + Tool Registry
2. P0 验收：理解 Query → Engine → Tool → Permission → Hook → Loop
"""

from dataclasses import dataclass, field
from typing import Any, Callable


@dataclass
class AuditEvent:
    tool: str
    allowed: bool
    detail: str


@dataclass
class MiniHarness:
    tools: dict[str, Callable[[dict], str]]
    denied_tools: set[str] = field(default_factory=lambda: {"Bash"})
    audit_log: list[AuditEvent] = field(default_factory=list)

    def pre_hook(self, name: str, args: dict) -> bool:
        if name in self.denied_tools:
            self.audit_log.append(AuditEvent(name, False, "denied by policy"))
            return False
        self.audit_log.append(AuditEvent(name, True, "pre_ok"))
        return True

    def execute(self, name: str, args: dict) -> str:
        if not self.pre_hook(name, args):
            return "ERROR: permission denied"
        if name not in self.tools:
            return f"ERROR: unknown tool {name}"
        result = self.tools[name](args)
        self.audit_log.append(AuditEvent(name, True, f"result_len={len(result)}"))
        return result

    def run_turn(self, tool_name: str, tool_args: dict) -> str:
        return self.execute(tool_name, tool_args)


def main():
    print("=" * 50)
    print("10 - Stage 1 Final")
    print("=" * 50)

    harness = MiniHarness(tools={
        "Read": lambda a: f"content of {a.get('path')}",
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


if __name__ == "__main__":
    main()
