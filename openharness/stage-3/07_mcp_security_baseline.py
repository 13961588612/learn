"""
07_mcp_security_baseline.py - MCP 只读 / 超时 / 白名单

学习要点:
1. 默认只读 Tool
2. 超时与 API Key 走环境变量
3. Tool 白名单
"""

from dataclasses import dataclass  # @dataclass 自动生成 __init__ 等样板代码


@dataclass
class McpSecurityPolicy:
    # 类属性带默认值；无类型注解的字段也可由 dataclass 推断
    read_only: bool = True
    timeout_sec: int = 30
    # frozenset 不可变集合，适合作为白名单（不可被意外修改）
    allowed_tools: frozenset[str] = frozenset({"search_tickets", "get_ticket"})


def authorize_tool(name: str, policy: McpSecurityPolicy) -> tuple[bool, str]:
    # tuple[bool, str] 返回 (是否允许, 原因说明) 二元组
    if name not in policy.allowed_tools:  # not in 检查成员不在集合中
        # {name!r} 等价于 repr(name)，带引号便于调试
        return False, f"tool {name!r} not in whitelist"
    # str.startswith 前缀匹配；read_only 时禁止 delete_ 开头 Tool
    if policy.read_only and name.startswith("delete_"):
        return False, "read-only policy"
    return True, "ok"


def main():
    print("=" * 50)
    print("07 - MCP Security Baseline")
    print("=" * 50)

    policy = McpSecurityPolicy()  # 使用 dataclass 默认值实例化
    # 元组 (a, b, c) 可迭代；for tool in ... 逐个检查
    for tool in ("search_tickets", "delete_ticket", "run_shell"):
        ok, msg = authorize_tool(tool, policy)  # 元组解包为 ok 与 msg
        # 三元表达式：ok 为 True 显示 ALLOW，否则 DENY
        print(f"  {tool}: {'ALLOW' if ok else 'DENY'} ({msg})")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
