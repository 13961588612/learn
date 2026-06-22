"""
08_stdlib_os_subprocess.py - os、pathlib 进阶、subprocess 安全调用

学习要点:
1. os.environ 读取环境变量
2. subprocess.run 替代 shell=True（更安全）
3. pathlib 遍历目录
"""

import os
import subprocess
import sys
from pathlib import Path


def demo_environ():
    print("\n=== os.environ ===")
    path_preview = os.environ.get("PATH", "")[:80]
    print(f"PATH 前缀: {path_preview}...")


def demo_subprocess():
    print("\n=== subprocess.run ===")
    result = subprocess.run(
        [sys.executable, "-c", "print('hello from subprocess')"],
        capture_output=True,
        text=True,
        check=True,
    )
    print(f"stdout: {result.stdout.strip()}")


def demo_pathlib_walk():
    print("\n=== pathlib 列举 ===")
    here = Path(__file__).parent
    py_files = sorted(p.name for p in here.glob("*.py"))
    print(f"stage-2 脚本: {py_files[:4]} ... 共 {len(py_files)} 个")


def main():
    print("=" * 50)
    print("08 - os & subprocess")
    print("=" * 50)
    demo_environ()
    demo_subprocess()
    demo_pathlib_walk()
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
