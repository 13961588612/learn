"""将 showcase Skills 复制到项目级 .openharness/skills/"""

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

LAB_DIR = Path(__file__).resolve().parents[1]
SRC = ROOT / "showcase" / "02_company_skills" / "skills"
DST = LAB_DIR / ".openharness" / "skills"


def main():
    print("=" * 50)
    print("Lab - Install Skills")
    print("=" * 50)

    if not SRC.exists():
        print(f"  源目录不存在: {SRC}")
        return

    if DST.exists():
        shutil.rmtree(DST)
    shutil.copytree(SRC, DST)

    names = [p.name for p in DST.iterdir() if p.is_dir()]
    print(f"  已安装到: {DST}")
    print(f"  skills: {names}")
    print("\n  在项目目录启动 openh，运行 /skills 验证")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
