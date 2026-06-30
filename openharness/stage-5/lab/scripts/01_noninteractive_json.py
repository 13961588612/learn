"""非交互 json 输出实验"""

import sys                    # path 操作、sys.path 动态导入
from pathlib import Path      # 面向对象的路径 API

# __file__ 当前脚本路径；resolve() 绝对化；parents[3] 向上 4 级到 openharness 根
ROOT = Path(__file__).resolve().parents[3]  # Path
sys.path.insert(0, str(ROOT))  # 把根目录插入模块搜索路径最前，以便 import _shared

from _shared.cli import print_result_summary, require_cli_or_guide, run_cli, save_experiment  # noqa: E402

# parents[1] 向上 2 级到 lab/ 目录，用于保存实验结果
LAB_DIR = Path(__file__).resolve().parents[1]  # Path


def main():
    print("=" * 50)   # 字符串 * 整数：重复 50 次
    print("Lab - noninteractive json")
    print("=" * 50)
    # 若 CLI 不可用则打印指引并 return 提前退出
    if not require_cli_or_guide("json prompt"):
        return
    # run_cli 接收 argv 列表；timeout 秒数限制子进程
    r = run_cli(["-p", "Reply with one word: pong", "--output-format", "json"], timeout=120)  # CliResult
    print_result_summary(r)
    save_experiment(LAB_DIR, "json_prompt", r)  # 把结果写入 lab 目录
    print("\n[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
