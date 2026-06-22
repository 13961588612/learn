"""
06_plugin_hooks.py - Plugin Hook 注册

学习要点:
1. hooks.json 声明 PreToolUse / PostToolUse
2. 与 stage-2 Hook 概念一致，Plugin 打包分发
"""

import json
from pathlib import Path


HOOKS_EXAMPLE = {
    "hooks": {
        "PreToolUse": [{
            "matcher": "Write|Edit",
            "hooks": [{"type": "command", "command": "python -m hooks.block_prod_writes"}],
        }],
        "PostToolUse": [{
            "matcher": "*",
            "hooks": [{"type": "command", "command": "python -m hooks.audit"}],
        }],
    },
}


def main():
    print("=" * 50)
    print("06 - Plugin Hooks")
    print("=" * 50)

    out = Path(__file__).parent / "data" / "hooks.example.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(HOOKS_EXAMPLE, indent=2), encoding="utf-8")
    print(f"  示例写入: {out}")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
