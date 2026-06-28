"""Lab 01: 检查 OpenHarness CLI 安装"""

import sys              # path 操作后修改 sys.path，使 _shared 可 import
from pathlib import Path  # 解析脚本路径、拼接目录

# Path(__file__).resolve() 绝对路径；parents[3] 向上 4 级到 learn/openharness/
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))  # 将 openharness 根目录插入 import 搜索路径首位

# noqa: E402 告诉 linter「import 不在文件顶部」是故意的（需先改 sys.path）
from _shared.cli import print_result_summary, require_cli_or_guide, run_cli, save_experiment  # noqa: E402

# parents[1]：lab/scripts -> lab 目录，用于保存实验 JSON
LAB_DIR = Path(__file__).resolve().parents[1]


def main():
    """检查 CLI 是否安装，运行 --version / --help 并保存实验记录。"""
    print("=" * 50)
    print("Lab 01 - Check Install")
    print("=" * 50)

    if not require_cli_or_guide("检查安装"):
        return  # CLI 未安装时函数返回 False，提前退出

    # 元组 (["--version"], ["--help"])：遍历两组 CLI 参数
    for args in (["--version"], ["--help"]):
        result = run_cli(args, timeout=30)
        print_result_summary(result)
        save_experiment(LAB_DIR, "check_install", result)

    print("\n  下一步: openh setup（若尚未配置）")
    print("  填写 workbook/01-install-setup.md 观察题")
    print("\n[OK] lab 01 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
