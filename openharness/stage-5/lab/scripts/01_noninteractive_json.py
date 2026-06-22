"""非交互 json 输出实验"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from _shared.cli import print_result_summary, require_cli_or_guide, run_cli, save_experiment  # noqa: E402

LAB_DIR = Path(__file__).resolve().parents[1]


def main():
    print("=" * 50)
    print("Lab - noninteractive json")
    print("=" * 50)
    if not require_cli_or_guide("json prompt"):
        return
    r = run_cli(["-p", "Reply with one word: pong", "--output-format", "json"], timeout=120)
    print_result_summary(r)
    save_experiment(LAB_DIR, "json_prompt", r)
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
