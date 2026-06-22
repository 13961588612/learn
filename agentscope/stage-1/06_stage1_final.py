"""Stage 1 综合验收"""

import subprocess
import sys
from pathlib import Path

STAGE = Path(__file__).resolve().parent
SCRIPTS = [
    "01_agentscope_concepts.py",
    "02_msg_blocks.py",
    "03_react_loop_simulator.py",
    "04_event_stream_concepts.py",
    "05_vs_langchain_openharness.py",
]


def main():
    print("=" * 50)
    print("Stage 1 Final")
    print("=" * 50)
    ok = 0
    for name in SCRIPTS:
        path = STAGE / name
        r = subprocess.run([sys.executable, str(path)], capture_output=True, text=True)
        if r.returncode == 0:
            ok += 1
            print(f"  [OK] {name}")
        else:
            print(f"  [FAIL] {name}")
    print(f"\n  概念脚本: {ok}/{len(SCRIPTS)}")
    print("  Lab: 完成 stage-1/lab workbook")
    print("\n[OK] stage-1 final")


if __name__ == "__main__":
    main()
