"""
05_readiness_states.py - ready / warning / blocked 判定模拟

学习要点:
1. dry-run 输出三类 readiness
2. blocked 时列出 next actions 逐项修复
"""

from dataclasses import dataclass  # @dataclass 自动生成 __init__ 等


# @dataclass 装饰器：为下面字段自动生成 __init__、__repr__
@dataclass
class Readiness:
    """readiness 检查结果：状态、告警消息、待办修复项。"""
    status: str  # ready | warning | blocked
    messages: list[str]       # 类型注解：字符串列表
    next_actions: list[str]


def check_mock_env(api_key: bool, mcp_ok: bool, profile: bool) -> Readiness:
    """
    根据模拟环境标志判定 readiness。
    参数均为 bool；-> Readiness 返回数据类实例。
    """
    warnings: list[str] = []  # 显式类型注解的空列表
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

    # 列表内嵌元组：(场景名, api_key, mcp_ok, profile)
    scenarios = [
        ("全就绪", True, True, True),
        ("缺 API Key", False, True, True),
        ("MCP 告警", True, False, True),
    ]

    # 元组解包：name, key, mcp, prof 分别接收四个元素
    for name, key, mcp, prof in scenarios:
        r = check_mock_env(key, mcp, prof)
        print(f"\n--- {name} -> {r.status} ---")
        for w in r.messages:
            print(f"  warning: {w}")
        for a in r.next_actions:
            print(f"  next_action: {a}")

    print("\n[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
