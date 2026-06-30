"""
01_health_probe.py - 健康检查项
"""

# 字符串列表：每项是一条健康检查描述
CHECKS = [
    "GET /health",
    "openh --dry-run readiness=ready",
    "MCP server ping",
    "profile default model reachable",
]


def main():
    print("=" * 50)   # 字符串 * 整数：重复 50 次
    print("01 - Health Probe")
    print("=" * 50)
    for c in CHECKS:  # str
        print(f"  - {c}")  # f-string 嵌入变量
    print("\n[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
