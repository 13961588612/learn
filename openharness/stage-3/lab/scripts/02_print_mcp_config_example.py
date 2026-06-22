"""打印 MCP 配置示例路径与内容"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
EXAMPLE = ROOT / "showcase" / "03_mcp_readonly_server" / "config" / "servers.json.example"


def main():
    print("=" * 50)
    print("MCP Config Example")
    print("=" * 50)
    if not EXAMPLE.exists():
        print("  示例文件不存在")
        return
    data = json.loads(EXAMPLE.read_text(encoding="utf-8"))
    print(json.dumps(data, indent=2, ensure_ascii=False))
    print(f"\n  路径: {EXAMPLE}")
    print("\n  将内容合并到 ~/.openharness/ 下 MCP 配置（见官方文档）")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
