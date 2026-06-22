"""
07_mcp_security_baseline.py - MCP 只读 / 超时 / 白名单

学习要点:
1. 默认只读 Tool
2. 超时与 API Key 走环境变量
3. Tool 白名单
"""

from dataclasses import dataclass


@dataclass
class McpSecurityPolicy:
    read_only: bool = True
    timeout_sec: int = 30
    allowed_tools: frozenset[str] = frozenset({"search_tickets", "get_ticket"})


def authorize_tool(name: str, policy: McpSecurityPolicy) -> tuple[bool, str]:
    if name not in policy.allowed_tools:
        return False, f"tool {name!r} not in whitelist"
    if policy.read_only and name.startswith("delete_"):
        return False, "read-only policy"
    return True, "ok"


def main():
    print("=" * 50)
    print("07 - MCP Security Baseline")
    print("=" * 50)

    policy = McpSecurityPolicy()
    for tool in ("search_tickets", "delete_ticket", "run_shell"):
        ok, msg = authorize_tool(tool, policy)
        print(f"  {tool}: {'ALLOW' if ok else 'DENY'} ({msg})")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
