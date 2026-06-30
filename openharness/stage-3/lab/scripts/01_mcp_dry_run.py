"""MCP dry-run 探测"""

import sys
from pathlib import Path

# __file__ 当前脚本路径；parents[3] 向上四级到仓库根目录 learn/
ROOT = Path(__file__).resolve().parents[3]  # Path
# insert(0, ...) 把 ROOT 插到 sys.path 最前，使后续可 import 仓库内模块
sys.path.insert(0, str(ROOT))

# noqa: E402 抑制「import 不在文件顶部」的 linter 告警（因上面修改了 sys.path）
from _shared.cli import print_result_summary, require_cli_or_guide, run_cli, save_experiment  # noqa: E402

# parents[1] 向上两级到 lab/ 目录，用于保存实验结果
LAB_DIR = Path(__file__).resolve().parents[1]  # Path


def main():
    print("=" * 50)
    print("Lab - MCP dry-run")
    print("=" * 50)
    # 若 CLI 不可用则打印指引并 return 提前退出
    if not require_cli_or_guide("MCP dry-run"):
        return
    # run_cli 执行 openh 命令；["--dry-run"] 为参数列表；timeout 秒数上限
    r = run_cli(["--dry-run"], timeout=60)  # CliResult
    print_result_summary(r)  # 打印 CLI 返回摘要
    save_experiment(LAB_DIR, "mcp_dry_run", r)  # 将结果持久化到 lab 目录
    print("\n  配置 MCP 后重复本脚本，对比 readiness 变化")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
