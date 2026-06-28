"""
05_plugin_structure.py - Plugin 目录约定

学习要点:
1. plugin: commands/ + hooks/ + .claude-plugin/plugin.json
2. oh plugin enable / disable
"""

from pathlib import Path


# 模块级字符串常量；三引号保留目录树换行格式
PLUGIN_LAYOUT = """
my-plugin/
├── .claude-plugin/
│   └── plugin.json
├── commands/
│   └── deploy-check.md
└── hooks/
    └── hooks.json
"""


def main():
    print("=" * 50)
    print("05 - Plugin Structure")
    print("=" * 50)
    print(PLUGIN_LAYOUT)  # 直接打印多行字符串

    # .resolve() 解析为绝对路径；.parents[1] 向上两级目录（stage-3 的上级 openharness）
    showcase = Path(__file__).resolve().parents[1] / "showcase" / "01_custom_tool_audit"
    # .name 只取路径最后一段（目录/文件名）
    print(f"  参考示范: {showcase.name}/ (Tool+Hook，Plugin 见 base/openharness)")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
