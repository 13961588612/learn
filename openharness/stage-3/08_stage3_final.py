"""
08_stage3_final.py - 综合：MCP 配置 + 模拟调用 + 安全策略
"""

import json


def validate_mcp_config(data: dict) -> list[str]:
    errors: list[str] = []
    for name, cfg in data.get("mcpServers", {}).items():
        if "command" not in cfg:
            errors.append(f"{name}: 缺少 command")
    return errors


def mock_tools_call(ticket_id: str) -> str:
    return f"Ticket {ticket_id}: open"


ALLOWED = frozenset({"get_ticket", "search_tickets"})


def main():
    print("=" * 50)
    print("08 - Stage 3 Final")
    print("=" * 50)

    cfg = {"mcpServers": {"tickets": {"command": "python", "args": ["-m", "ticket_mcp"]}}}
    print(f"\n  config: {validate_mcp_config(cfg) or 'OK'}")
    print(f"  call: {mock_tools_call('T-1')}")
    print(f"  whitelist get_ticket: {'ALLOW' if 'get_ticket' in ALLOWED else 'DENY'}")

    print("\n[OK] 阶段三综合练习完成")


if __name__ == "__main__":
    main()
