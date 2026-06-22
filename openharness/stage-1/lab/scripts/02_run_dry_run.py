"""Lab 02: dry-run 实验"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from _shared.cli import print_result_summary, require_cli_or_guide, run_cli, save_experiment  # noqa: E402

LAB_DIR = Path(__file__).resolve().parents[1]


def main():
    print("=" * 50)
    print("Lab 02 - dry-run")
    print("=" * 50)

    if not require_cli_or_guide("dry-run"):
        return

    result = run_cli(["--dry-run"], timeout=60)
    print_result_summary(result)
    path = save_experiment(LAB_DIR, "dry_run", result)
    print(f"\n  已保存: {path}")

    result2 = run_cli(
        ["--dry-run", "-p", "Explain OpenHarness in one sentence", "--output-format", "json"],
        timeout=60,
    )
    print_result_summary(result2)
    save_experiment(LAB_DIR, "dry_run_json", result2)

    print("\n  请阅读 workbook/02-dry-run.md 并记录 readiness 含义")
    print("\n[OK] lab 02 完成")


if __name__ == "__main__":
    main()
