"""
05_plugin_structure.py - Plugin 目录约定

学习要点:
1. plugin: commands/ + hooks/ + .claude-plugin/plugin.json
2. oh plugin enable / disable
"""

from pathlib import Path


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
    print(PLUGIN_LAYOUT)

    showcase = Path(__file__).resolve().parents[1] / "showcase" / "01_custom_tool_audit"
    print(f"  参考示范: {showcase.name}/ (Tool+Hook，Plugin 见 base/openharness)")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
