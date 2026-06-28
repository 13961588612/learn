"""
08_permissions_rules.py - settings.json permission 基线

学习要点:
1. permission mode: default / auto / plan
2. path_rules、denied_commands
"""

import json  # 将 dict 序列化为 JSON 写入 settings 文件
from pathlib import Path  # 定位输出路径


# 嵌套 dict：模拟 OpenHarness settings.json 的权限基线结构
DEFAULT_SETTINGS = {
    "permissionMode": "default",  # 默认模式：写操作需逐项确认
    "pathRules": {
        "allowRead": ["/project", "/tmp"],
        "denyWrite": ["/etc", "/prod", "**/.env"],  # glob 风格路径模式
    },
    "deniedCommands": ["rm", "curl", "wget", "sudo"],  # Shell 命令黑名单
}


def main():
    """将 DEFAULT_SETTINGS 写入 stage-2/data/settings.json。"""
    print("=" * 50)
    print("08 - Permissions Rules")
    print("=" * 50)

    out = Path(__file__).parent / "data" / "settings.json"
    out.parent.mkdir(parents=True, exist_ok=True)  # 确保 data/ 目录存在
    # indent=2 格式化 JSON；encoding 指定 UTF-8
    out.write_text(json.dumps(DEFAULT_SETTINGS, indent=2), encoding="utf-8")

    print(f"  写入: {out}")
    # dict['key'] 按键访问嵌套值
    print(f"  mode: {DEFAULT_SETTINGS['permissionMode']}")
    print(f"  denied: {DEFAULT_SETTINGS['deniedCommands']}")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
