"""max-turns 非交互实验（需 API）"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]  # 仓库根 learn/
sys.path.insert(0, str(ROOT))  # 使 _shared 等包可 import

from _shared.cli import print_result_summary, require_cli_or_guide, run_cli, save_experiment  # noqa: E402

LAB_DIR = Path(__file__).resolve().parents[1]


def main():
    print("=" * 50)
    print("Lab - max-turns")
    print("=" * 50)
    if not require_cli_or_guide("max-turns"):
        return

    # 部分版本支持 --max-turns；不支持则 CLI 会报错，仍记录
    args = [
        "-p",                                    # 非交互 prompt 模式
        "List files, then read README, repeat until done",
        "--max-turns",
        "3",                                     # 最多 3 轮 Agent Loop
        "--output-format",
        "json",                                  # 结构化输出便于 save_experiment
    ]
    r = run_cli(args, timeout=180)  # 180 秒超时，防止死循环挂起
    print_result_summary(r, max_lines=30)  # 最多显示 30 行摘要
    save_experiment(LAB_DIR, "max_turns", r)
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
