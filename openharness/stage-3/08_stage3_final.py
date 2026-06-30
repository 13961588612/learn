"""
08_stage3_final.py - 综合：MCP 配置 + 模拟调用 + 安全策略
"""

import json  # 标准库 JSON 解析/序列化（综合练习可扩展配置读写）


def validate_mcp_config(data: dict) -> list[str]:
    errors: list[str] = []
    # data.get("mcpServers", {}) 缺省空 dict；.items() 遍历各 server 配置
    for name, cfg in data.get("mcpServers", {}).items():  # name: str；cfg: dict
        if "command" not in cfg:
            errors.append(f"{name}: 缺少 command")
    return errors


def mock_tools_call(ticket_id: str) -> str:
    # 模拟 MCP tools/call 返回的文本内容
    return f"Ticket {ticket_id}: open"


# 模块级常量：frozenset 不可变，O(1) 成员检测
ALLOWED = frozenset({"get_ticket", "search_tickets"})


def main():
    print("=" * 50)
    print("08 - Stage 3 Final")
    print("=" * 50)

    # 单行 dict 字面量构造最小合法 MCP 配置
    cfg = {"mcpServers": {"tickets": {"command": "python", "args": ["-m", "ticket_mcp"]}}}  # dict
    # validate 返回空列表时 or 'OK' 显示 OK
    print(f"\n  config: {validate_mcp_config(cfg) or 'OK'}")
    print(f"  call: {mock_tools_call('T-1')}")
    # in 运算符检查成员是否在 frozenset 中
    print(f"  whitelist get_ticket: {'ALLOW' if 'get_ticket' in ALLOWED else 'DENY'}")

    print("\n[OK] 阶段三综合练习完成")


if __name__ == "__main__":
    main()
