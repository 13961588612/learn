"""探测 gateway / ohmo 相关 CLI（版本差异友好）"""

import sys                    # path 操作、sys.path 动态导入
from pathlib import Path      # 面向对象的路径 API

# __file__ 当前脚本路径；resolve() 绝对化；parents[3] 向上 4 级到 openharness 根
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))  # 把根目录插入模块搜索路径最前，以便 import _shared

from _shared.cli import print_result_summary, require_cli_or_guide, run_cli, save_experiment  # noqa: E402

# parents[1] 向上 2 级到 lab/ 目录，用于保存实验结果
LAB_DIR = Path(__file__).resolve().parents[1]


def main():
    print("=" * 50)   # 字符串 * 整数：重复 50 次
    print("Lab - gateway help probe")
    print("=" * 50)
    # 若 CLI 不可用则打印指引并 return 提前退出
    if not require_cli_or_guide("help"):
        return
    r = run_cli(["--help"], timeout=30)  # 探测 --help 输出
    print_result_summary(r, max_lines=40)  # max_lines 限制打印行数
    save_experiment(LAB_DIR, "gateway_help", r)
    print("\n  在 help 中搜索 gateway / ohmo / channel 子命令")
    print("\n[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
