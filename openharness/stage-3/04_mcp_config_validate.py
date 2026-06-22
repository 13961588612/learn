"""
04_mcp_config_validate.py - servers.json 校验

学习要点:
1. mcpServers 配置结构
2. dry-run 应能发现 command/args 错误
"""

import json
from pathlib import Path


def validate_mcp_config(data: dict) -> list[str]:
    errors: list[str] = []
    servers = data.get("mcpServers", {})
    if not servers:
        errors.append("mcpServers 为空")
    for name, cfg in servers.items():
        if "command" not in cfg:
            errors.append(f"{name}: 缺少 command")
        if not cfg.get("args"):
            errors.append(f"{name}: args 为空")
    return errors


def main():
    print("=" * 50)
    print("04 - MCP Config Validate")
    print("=" * 50)

    good = {
        "mcpServers": {
            "company-tickets": {
                "command": "uv",
                "args": ["run", "python", "-m", "ticket_mcp"],
            },
        },
    }
    bad = {"mcpServers": {"broken": {}}}

    for label, cfg in [("valid", good), ("invalid", bad)]:
        errs = validate_mcp_config(cfg)
        print(f"\n  {label}: {errs or 'OK'}")

    example = Path(__file__).parent.parent / "showcase" / "03_mcp_readonly_server" / "config" / "servers.json.example"
    if example.exists():
        loaded = json.loads(example.read_text(encoding="utf-8"))
        print(f"\n  showcase 配置校验: {validate_mcp_config(loaded) or 'OK'}")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
