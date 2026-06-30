"""打印 MCP 配置示例路径与内容"""

import json
from pathlib import Path

# parents[3] 从 lab/scripts/ 向上到仓库根 learn/
ROOT = Path(__file__).resolve().parents[3]  # Path
# / 运算符拼接路径段，指向 showcase 示例配置
EXAMPLE = ROOT / "showcase" / "03_mcp_readonly_server" / "config" / "servers.json.example"  # Path


def main():
    print("=" * 50)
    print("MCP Config Example")
    print("=" * 50)
    if not EXAMPLE.exists():  # 文件不存在则提前 return
        print("  示例文件不存在")
        return
    # read_text 读 UTF-8 文本；json.loads 解析为 Python dict
    data = json.loads(EXAMPLE.read_text(encoding="utf-8"))  # dict
    # indent=2 美化输出；ensure_ascii=False 保留中文
    print(json.dumps(data, indent=2, ensure_ascii=False))
    print(f"\n  路径: {EXAMPLE}")
    print("\n  将内容合并到 ~/.openharness/ 下 MCP 配置（见官方文档）")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
