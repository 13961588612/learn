"""创建示例 MEMORY.md 供 Harness 读取"""

from pathlib import Path

MEMORY = """# MEMORY

## Team preferences
- 回复使用简体中文
- 发布窗口: 周二/周四 20:00-22:00

## User facts
- 学习轨道: openharness stage-4
"""

LAB_DIR = Path(__file__).resolve().parents[1]
TARGET = LAB_DIR / ".openharness" / "MEMORY.md"


def main():
    print("=" * 50)
    print("Lab - Seed MEMORY.md")
    print("=" * 50)
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(MEMORY, encoding="utf-8")
    print(f"  已写入: {TARGET}")
    print("\n  在 lab 目录启动 openh，询问「我们的发布窗口是什么时候」")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
