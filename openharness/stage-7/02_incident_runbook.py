"""
02_incident_runbook.py - 故障树速查
"""

RUNBOOK = {
    "MCP 挂": "检查 server 进程、servers.json、dry-run",
    "profile 失效": "rotate API key、openh setup",
    "compaction 异常": "检查 MEMORY.md 大小、max context",
    "Gateway 内存涨": "会话 TTL、限制附件",
}


def main():
    print("=" * 50)
    print("02 - Incident Runbook")
    print("=" * 50)
    for k, v in RUNBOOK.items():
        print(f"  {k}: {v}")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
