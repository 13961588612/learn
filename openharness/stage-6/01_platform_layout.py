"""
01_platform_layout.py - 公司统一后端目录规范
"""

LAYOUT = """
company-agent-backend/
├── config/
│   ├── profiles/
│   ├── settings.json
│   └── mcp/
├── skills/
├── plugins/
├── gateway/
├── audit/
└── deploy/
"""


def main():
    print("=" * 50)
    print("01 - Platform Layout")
    print("=" * 50)
    print(LAYOUT)
    print("[OK] 完成")


if __name__ == "__main__":
    main()
