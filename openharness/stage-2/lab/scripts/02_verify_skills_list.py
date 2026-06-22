"""尝试列出 skills 相关 CLI（版本差异时仅作探测）"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from _shared.cli import print_result_summary, require_cli_or_guide, run_cli, save_experiment  # noqa: E402

LAB_DIR = Path(__file__).resolve().parents[1]


def main():
    print("=" * 50)
    print("Lab - Verify Skills CLI")
    print("=" * 50)

    if not require_cli_or_guide("skills 探测"):
        return

    for args in (["--help"],):
        r = run_cli(args, timeout=30)
        print_result_summary(r, max_lines=15)
        save_experiment(LAB_DIR, "skills_help", r)

    print("\n  请在 TUI 中执行 /skills 并记录到 experiments/")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
