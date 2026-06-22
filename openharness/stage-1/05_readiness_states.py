"""
05_readiness_states.py - ready / warning / blocked 判定模拟

学习要点:
1. dry-run 输出三类 readiness
2. blocked 时列出 next actions 逐项修复
"""

from dataclasses import dataclass


@dataclass
class Readiness:
    status: str  # ready | warning | blocked
    messages: list[str]
    next_actions: list[str]


def check_mock_env(api_key: bool, mcp_ok: bool, profile: bool) -> Readiness:
    warnings: list[str] = []
    actions: list[str] = []

    if not api_key:
        actions.append("设置 ANTHROPIC_API_KEY 或运行 openh setup")
    if not profile:
        actions.append("配置至少一个 provider profile")
    if not mcp_ok:
        warnings.append("MCP server company-tickets 未连接（可选）")

    if actions:
        return Readiness("blocked", warnings, actions)
    if warnings:
        return Readiness("warning", warnings, [])
    return Readiness("ready", [], [])


def main():
    print("=" * 50)
    print("05 - Readiness States")
    print("=" * 50)

    scenarios = [
        ("全就绪", True, True, True),
        ("缺 API Key", False, True, True),
        ("MCP 告警", True, False, True),
    ]

    for name, key, mcp, prof in scenarios:
        r = check_mock_env(key, mcp, prof)
        print(f"\n--- {name} -> {r.status} ---")
        for w in r.messages:
            print(f"  warning: {w}")
        for a in r.next_actions:
            print(f"  next_action: {a}")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
