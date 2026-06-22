"""
01_health_probe.py - 健康检查项
"""

CHECKS = [
    "GET /health",
    "openh --dry-run readiness=ready",
    "MCP server ping",
    "profile default model reachable",
]


def main():
    print("=" * 50)
    print("01 - Health Probe")
    print("=" * 50)
    for c in CHECKS:
        print(f"  - {c}")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
