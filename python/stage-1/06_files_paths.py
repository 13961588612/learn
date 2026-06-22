"""
06_files_paths.py - open、pathlib 读写、编码 UTF-8

学习要点:
1. pathlib.Path 是现代路径 API（优于 os.path 拼接）
2. 读写文本时显式指定 encoding='utf-8'
3. with 语句自动关闭文件句柄
"""

from pathlib import Path


def demo_pathlib():
    print("\n=== pathlib ===")
    here = Path(__file__).resolve()
    data_dir = here.parent / "data"
    data_dir.mkdir(exist_ok=True)
    print(f"当前脚本: {here.name}")
    print(f"data 目录: {data_dir}")


def demo_write_read():
    print("\n=== 读写文本 ===")
    path = Path(__file__).parent / "data" / "sample.txt"
    lines = ["第一行\n", "第二行 Hello\n", "第三行 中文\n"]
    path.write_text("".join(lines), encoding="utf-8")

    content = path.read_text(encoding="utf-8")
    print(f"读取 {path.name}:\n{content}")


def demo_read_lines():
    print("\n=== 逐行读取 ===")
    path = Path(__file__).parent / "data" / "sample.txt"
    with path.open(encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            print(f"  L{i}: {line.rstrip()}")


def main():
    print("=" * 50)
    print("06 - Files & Paths")
    print("=" * 50)
    demo_pathlib()
    demo_write_read()
    demo_read_lines()
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
