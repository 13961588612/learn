"""Lab 03: 非交互 stream-json（需已 setup 且 API 可用）"""

import sys              # 修改 import 路径
from pathlib import Path  # 读取 prompt 文件、定位 lab 目录

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from _shared.cli import print_result_summary, require_cli_or_guide, run_cli, save_experiment  # noqa: E402

LAB_DIR = Path(__file__).resolve().parents[1]
# 拼接 lab/prompts/smoke-test.txt 作为非交互 prompt 来源
PROMPT = Path(__file__).resolve().parents[1] / "prompts" / "smoke-test.txt"


def main():
    """用 smoke-test.txt 内容发起 stream-json 请求并保存输出。"""
    print("=" * 50)
    print("Lab 03 - stream-json")
    print("=" * 50)

    if not require_cli_or_guide("stream-json"):
        return

    text = PROMPT.read_text(encoding="utf-8").strip()  # 读文件并去首尾空白
    result = run_cli(
        ["-p", text, "--output-format", "stream-json"],
        timeout=180,  # 流式输出可能较慢，超时设 180 秒
    )
    print_result_summary(result, max_lines=40)  # 关键字参数 max_lines
    path = save_experiment(LAB_DIR, "stream_json", result, notes="smoke-test.txt")
    print(f"\n  已保存: {path}")

    if result.returncode != 0:
        print("  提示: 若失败，先完成 openh setup 并配置 API Key")

    print("\n  填写 workbook/04-stream-json.md")
    print("\n[OK] lab 03 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
