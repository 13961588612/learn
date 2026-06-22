"""
03_dry_run_cli.py - 调用 openh --dry-run（可选）

学习要点:
1. --dry-run 不调用模型、不执行 Tool，只检查 readiness
2. Windows 使用 openh，Unix 优先 oh
3. 未安装 CLI 时跳过并提示安装
"""

import shutil
import subprocess
import sys


def find_cli() -> list[str] | None:
    for cmd in ("openh", "oh"):
        if shutil.which(cmd):
            return [cmd]
    return None


def run_dry_run() -> None:
    cli = find_cli()
    if not cli:
        print("  跳过: 未找到 openh/oh CLI")
        print("  安装: pip install openharness-ai  或  uv sync --group openharness-stage-1")
        return

    cmd = cli + ["--dry-run"]
    print(f"  执行: {' '.join(cmd)}")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        print(f"  exit_code: {result.returncode}")
        out = (result.stdout or result.stderr or "").strip()
        if out:
            print(f"  输出预览:\n{out[:800]}")
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


if __name__ == "__main__":
    main()
