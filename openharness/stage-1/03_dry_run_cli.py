"""
03_dry_run_cli.py - 调用 openh --dry-run（可选）

学习要点:
1. --dry-run 不调用模型、不执行 Tool，只检查 readiness
2. Windows 使用 openh，Unix 优先 oh
3. 未安装 CLI 时跳过并提示安装
"""

import shutil       # which() 在 PATH 中查找可执行文件
import subprocess   # run() 启动子进程执行外部命令
import sys          # 本模块未直接使用，保留供扩展（如 sys.exit）


def find_cli() -> list[str] | None:
    """
    在 PATH 中查找 openh 或 oh 命令。
    -> list[str] | None：找到返回单元素命令列表，否则 None（PEP 604 联合类型写法）。
    """
    for cmd in ("openh", "oh"):  # 元组字面量，遍历候选命令名
        if shutil.which(cmd):    # which 返回完整路径或 None
            return [cmd]         # 返回列表，便于后续 cli + args 拼接
    return None


def run_dry_run() -> None:
    """尝试执行 openh/oh --dry-run 并打印结果；未安装 CLI 时跳过。"""
    cli = find_cli()
    if not cli:
        print("  跳过: 未找到 openh/oh CLI")
        print("  安装: pip install openharness-ai  或  uv sync --group openharness-cli")
        print("  然后: uv run python openharness/stage-1/03_dry_run_cli.py  （uv run 会把 .venv/Scripts 加入 PATH）")
        return  # 提前返回，不继续执行

    cmd = cli + ["--dry-run"]  # 列表 + 列表：拼接命令与参数
    print(f"  执行: {' '.join(cmd)}")  # join 将命令列表转为可读字符串
    try:
        # subprocess.run：同步执行子进程
        # capture_output=True 捕获 stdout/stderr；text=True 以 str 而非 bytes 返回
        # timeout=30 超时秒数，超时抛 subprocess.TimeoutExpired
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        print(f"  exit_code: {result.returncode}")
        # or 链：优先 stdout，空则 stderr，再 strip 去首尾空白
        out = (result.stdout or result.stderr or "").strip()
        if out:
            print(f"  输出预览:\n{out[:800]}")  # 字符串切片 [:800] 取前 800 字符
    except subprocess.TimeoutExpired:
        print("  超时")
    except FileNotFoundError:
        print("  CLI 不可用")


def main():
    print("=" * 50)
    print("03 - dry-run CLI")
    print("=" * 50)
    print("\n=== readiness 含义 ===")
    print("  ready   - 可运行")
    print("  warning - 可运行但有配置告警")
    print("  blocked - 需修复 next actions 后再运行")
    print("\n=== 尝试 dry-run ===")
    run_dry_run()
    print("\n[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
