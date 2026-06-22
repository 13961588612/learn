"""
08_permissions_rules.py - settings.json permission 基线

学习要点:
1. permission mode: default / auto / plan
2. path_rules、denied_commands
"""

import json
from pathlib import Path


DEFAULT_SETTINGS = {
    "permissionMode": "default",
    "pathRules": {
        "allowRead": ["/project", "/tmp"],
        "denyWrite": ["/etc", "/prod", "**/.env"],
    },
    "deniedCommands": ["rm", "curl", "wget", "sudo"],
}


def main():
    print("=" * 50)
    print("08 - Permissions Rules")
    print("=" * 50)

    out = Path(__file__).parent / "data" / "settings.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(DEFAULT_SETTINGS, indent=2), encoding="utf-8")

    print(f"  写入: {out}")
    print(f"  mode: {DEFAULT_SETTINGS['permissionMode']}")
    print(f"  denied: {DEFAULT_SETTINGS['deniedCommands']}")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
