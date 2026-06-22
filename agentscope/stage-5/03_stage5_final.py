"""Stage 5 final"""
import subprocess, sys
from pathlib import Path
def main():
    stage = Path(__file__).parent
    files = [f for f in sorted(stage.glob("0*.py")) if "final" not in f.name]
    ok = sum(1 for f in files if subprocess.run([sys.executable, str(f)]).returncode == 0)
    print(f"Stage 5: {ok}/{len(files)}\n[OK]")
if __name__ == "__main__":
    main()
