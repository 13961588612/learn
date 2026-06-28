"""
08_stdlib_os_subprocess.py - os、pathlib 进阶、subprocess 安全调用

学习要点:
1. os.environ 读取环境变量
2. subprocess.run 替代 shell=True（更安全）
3. pathlib 遍历目录
"""

import os
import subprocess
import sys       # sys.executable 为当前 Python 解释器路径
from pathlib import Path


def demo_environ():
    print("\n=== os.environ ===")
    # os.environ 类似 dict；.get(key, default) 安全读取
    path_preview = os.environ.get("PATH", "")[:80]  # 切片取前 80 字符
    print(f"PATH 前缀: {path_preview}...")


def demo_subprocess():
    print("\n=== subprocess.run ===")
    result = subprocess.run(
        [sys.executable, "-c", "print('hello from subprocess')"],  # 列表形式，无 shell 注入风险
        capture_output=True,  # 捕获 stdout/stderr
        text=True,            # 输出解码为 str 而非 bytes
        check=True,           # 非零退出码时抛 CalledProcessError
    )
    print(f"stdout: {result.stdout.strip()}")


def demo_pathlib_walk():
    print("\n=== pathlib 列举 ===")
    here = Path(__file__).parent
    # glob("*.py") 匹配当前目录下所有 .py 文件
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
