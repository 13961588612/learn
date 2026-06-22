"""Stage 3 final"""

import subprocess, sys
from pathlib import Path

def main():
    print("=" * 50)
    print("Stage 3 Final")
    print("=" * 50)
    stage = Path(__file__).parent
    files = [f for f in sorted(stage.glob("0*.py")) if "final" not in f.name]
    ok = sum(1 for f in files if subprocess.run([sys.executable, str(f)]).returncode == 0)
    print(f"  {ok}/{len(files)} scripts OK")
    print("\n[OK] stage-3 final")

if __name__ == "__main__":
    main()
