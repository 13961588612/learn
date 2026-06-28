"""
04_memory_md.py - MEMORY.md 读写策略

学习要点:
1. 跨会话持久化用户/团队偏好
2. 与 LangGraph Store 对比
"""

from pathlib import Path


# 模块级默认 MEMORY 模板；三引号保留 Markdown 换行
DEFAULT_MEMORY = """# MEMORY

## User preferences
- 回复使用简体中文
- 代码示例 prefer Python 3.11+

## Team facts
- 发布窗口: 周二/周四 20:00-22:00
"""


def load_memory(path: Path) -> str:
    if path.exists():  # 文件已存在则直接读取
        return path.read_text(encoding="utf-8")
    # 不存在则创建目录并写入默认内容（懒初始化）
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(DEFAULT_MEMORY, encoding="utf-8")
    return DEFAULT_MEMORY


def main():
    print("=" * 50)
    print("04 - MEMORY.md")
    print("=" * 50)

    mem_path = Path(__file__).parent / "data" / "MEMORY.md"
    content = load_memory(mem_path)
    print(f"  路径: {mem_path}")
    # splitlines() 按行拆分；len 统计行数
    print(f"  行数: {len(content.splitlines())}")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
