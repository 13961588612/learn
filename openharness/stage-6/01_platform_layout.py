"""
01_platform_layout.py - 公司统一后端目录规范
"""

# 三引号多行字符串：保留换行与缩进，用于展示目录树
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
    print("=" * 50)   # 字符串 * 整数：重复 50 次
    print("01 - Platform Layout")
    print("=" * 50)
    print(LAYOUT)     # 直接打印多行字符串
    print("[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
