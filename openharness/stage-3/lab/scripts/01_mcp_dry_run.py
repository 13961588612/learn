"""MCP dry-run 探测"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from _shared.cli import print_result_summary, require_cli_or_guide, run_cli, save_experiment  # noqa: E402

LAB_DIR = Path(__file__).resolve().parents[1]


def main():
    print("=" * 50)
    print("Lab - MCP dry-run")
    print("=" * 50)
    if not require_cli_or_guide("MCP dry-run"):
        return
    r = run_cli(["--dry-run"], timeout=60)
    print_result_summary(r)
    save_experiment(LAB_DIR, "mcp_dry_run", r)
    print("\n  配置 MCP 后重复本脚本，对比 readiness 变化")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
