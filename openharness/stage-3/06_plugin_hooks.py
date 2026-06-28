"""
06_plugin_hooks.py - Plugin Hook 注册

学习要点:
1. hooks.json 声明 PreToolUse / PostToolUse
2. 与 stage-2 Hook 概念一致，Plugin 打包分发
"""

import json
from pathlib import Path


# 嵌套 dict 模拟 hooks.json 结构；列表 [] 可含多个 hook 规则
HOOKS_EXAMPLE = {
    "hooks": {
        "PreToolUse": [{  # Tool 调用前触发
            "matcher": "Write|Edit",  # 正则匹配 Tool 名
            "hooks": [{"type": "command", "command": "python -m hooks.block_prod_writes"}],
        }],
        "PostToolUse": [{  # Tool 调用后触发
            "matcher": "*",  # * 匹配所有 Tool
            "hooks": [{"type": "command", "command": "python -m hooks.audit"}],
        }],
    },
}


def main():
    print("=" * 50)
    print("06 - Plugin Hooks")
    print("=" * 50)

    # Path(__file__).parent 当前脚本所在目录 stage-3/
    out = Path(__file__).parent / "data" / "hooks.example.json"
    # mkdir(parents=True) 递归创建中间目录；exist_ok=True 已存在不报错
    out.parent.mkdir(parents=True, exist_ok=True)
    # json.dumps(indent=2) 格式化 JSON；write_text 写入 UTF-8 文本
    out.write_text(json.dumps(HOOKS_EXAMPLE, indent=2), encoding="utf-8")
    print(f"  示例写入: {out}")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
