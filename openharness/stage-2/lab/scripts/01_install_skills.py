"""将 showcase Skills 复制到项目级 .openharness/skills/"""

import shutil  # copytree / rmtree 目录级复制与删除
import sys     # sys.path 修改模块搜索路径
from pathlib import Path  # 解析脚本相对路径

# __file__ -> 本脚本；parents[3] 上溯到仓库根 learn/
ROOT = Path(__file__).resolve().parents[3]
# insert(0, ...) 将 ROOT 插入 sys.path 最前，便于 import 仓库内模块
sys.path.insert(0, str(ROOT))

# parents[1] 为 lab/ 目录
LAB_DIR = Path(__file__).resolve().parents[1]
SRC = ROOT / "showcase" / "02_company_skills" / "skills"  # 源 skills 目录
DST = LAB_DIR / ".openharness" / "skills"  # 目标：lab 项目级 skills


def main():
    """将 showcase skills 复制到 lab/.openharness/skills/。"""
    print("=" * 50)
    print("Lab - Install Skills")
    print("=" * 50)

    if not SRC.exists():
        print(f"  源目录不存在: {SRC}")
        return  # 提前退出，不抛异常

    if DST.exists():
        shutil.rmtree(DST)  # 删除已有目标目录（含内容）
    shutil.copytree(SRC, DST)  # 递归复制整个目录树

    # 列表推导：只保留 DST 下的子目录名
    names = [p.name for p in DST.iterdir() if p.is_dir()]
    print(f"  已安装到: {DST}")
    print(f"  skills: {names}")
    print("\n  在项目目录启动 openh，运行 /skills 验证")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
