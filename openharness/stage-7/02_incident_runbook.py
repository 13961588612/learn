"""
02_incident_runbook.py - 故障树速查
"""

# dict：键为故障现象，值为处理步骤简述
RUNBOOK = {
    "MCP 挂": "检查 server 进程、servers.json、dry-run",
    "profile 失效": "rotate API key、openh setup",
    "compaction 异常": "检查 MEMORY.md 大小、max context",
    "Gateway 内存涨": "会话 TTL、限制附件",
}


def main():
    print("=" * 50)   # 字符串 * 整数：重复 50 次
    print("02 - Incident Runbook")
    print("=" * 50)
    # dict.items() 返回 (键, 值) 元组，for 循环解包
    for k, v in RUNBOOK.items():
        print(f"  {k}: {v}")
    print("\n[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
