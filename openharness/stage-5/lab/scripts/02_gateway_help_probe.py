"""探测 gateway / ohmo 相关 CLI（版本差异友好）"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from _shared.cli import print_result_summary, require_cli_or_guide, run_cli, save_experiment  # noqa: E402

LAB_DIR = Path(__file__).resolve().parents[1]


def main():
    print("=" * 50)
    print("Lab - gateway help probe")
    print("=" * 50)
    if not require_cli_or_guide("help"):
        return
    r = run_cli(["--help"], timeout=30)
    print_result_summary(r, max_lines=40)
    save_experiment(LAB_DIR, "gateway_help", r)
    print("\n  在 help 中搜索 gateway / ohmo / channel 子命令")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
