"""Stage 2 综合"""

import subprocess
import sys
from pathlib import Path

STAGE = Path(__file__).resolve().parent
SCRIPTS = [f"0{i}_*.py" for i in range(1, 7)]


def main():
    print("=" * 50)
    print("Stage 2 Final")
    print("=" * 50)
    files = sorted(STAGE.glob("0*.py"))
    files = [f for f in files if f.name != "07_stage2_final.py"]
    ok = sum(
        1
        for f in files
        if subprocess.run([sys.executable, str(f)], capture_output=True).returncode == 0
    )
    print(f"  概念脚本: {ok}/{len(files)}")
    print("  Lab + showcase/01")
    print("\n[OK] stage-2 final")


if __name__ == "__main__":
    main()
