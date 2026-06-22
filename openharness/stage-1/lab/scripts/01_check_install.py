"""Lab 01: 检查 OpenHarness CLI 安装"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from _shared.cli import print_result_summary, require_cli_or_guide, run_cli, save_experiment  # noqa: E402

LAB_DIR = Path(__file__).resolve().parents[1]


def main():
    print("=" * 50)
    print("Lab 01 - Check Install")
    print("=" * 50)

    if not require_cli_or_guide("检查安装"):
        return

    for args in (["--version"], ["--help"]):
        result = run_cli(args, timeout=30)
        print_result_summary(result)
        save_experiment(LAB_DIR, "check_install", result)

    print("\n  下一步: openh setup（若尚未配置）")
    print("  填写 workbook/01-install-setup.md 观察题")
    print("\n[OK] lab 01 完成")


if __name__ == "__main__":
    main()
