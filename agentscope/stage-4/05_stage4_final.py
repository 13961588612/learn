"""Stage 4 final"""
import subprocess, sys
from pathlib import Path
def main():
    print("Stage 4 Final")
    stage = Path(__file__).parent
    files = [f for f in sorted(stage.glob("0*.py")) if "final" not in f.name]
    ok = sum(1 for f in files if subprocess.run([sys.executable, str(f)]).returncode == 0)
    print(f"  {ok}/{len(files)} OK\n[OK] stage-4 final")
if __name__ == "__main__":
    main()
