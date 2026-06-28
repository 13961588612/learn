"""尝试列出 skills 相关 CLI（版本差异时仅作探测）"""

import sys  # 修改 sys.path 以 import 仓库根模块
from pathlib import Path  # 定位 lab 与仓库根目录

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

# noqa: E402 告诉 linter「import 不在文件顶部」是故意的（需先改 path）
from _shared.cli import print_result_summary, require_cli_or_guide, run_cli, save_experiment  # noqa: E402

LAB_DIR = Path(__file__).resolve().parents[1]


def main():
    """探测 openh CLI --help 并保存实验结果。"""
    print("=" * 50)
    print("Lab - Verify Skills CLI")
    print("=" * 50)

    # require_cli_or_guide 检查 CLI 是否可用，不可用则打印指引并返回 False
    if not require_cli_or_guide("skills 探测"):
        return

    # 单元素元组 (["--help"],) 末尾逗号不可省略，否则会被当作 list
    for args in (["--help"],):
        r = run_cli(args, timeout=30)  # 子进程运行 CLI，30 秒超时
        print_result_summary(r, max_lines=15)  # 打印 stdout/stderr 摘要
        save_experiment(LAB_DIR, "skills_help", r)  # 结果写入 lab/experiments/

    print("\n  请在 TUI 中执行 /skills 并记录到 experiments/")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
