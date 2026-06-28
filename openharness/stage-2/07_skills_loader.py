"""
07_skills_loader.py - 扫描 .openharness/skills/ 目录

学习要点:
1. 每个 skill 一个子目录 + SKILL.md
2. 项目级 vs 用户级 skills 路径
"""

from pathlib import Path  # Path 对象表示文件系统路径


def discover_skills(root: Path) -> list[dict]:
    """
    扫描 root 下每个子目录，若存在 SKILL.md 则收录。
    返回 list[dict]，每项含 name、path、size。
    """
    if not root.exists():
        return []  # 路径不存在时返回空列表
    skills = []
    # sorted(iterdir()) 按名称排序遍历直接子项
    for child in sorted(root.iterdir()):
        if not child.is_dir():
            continue  # 跳过非目录项
        # Path / str 拼接子路径
        skill_md = child / "SKILL.md"
        if skill_md.exists():
            skills.append({
                "name": child.name,           # 目录名即 skill 名
                "path": str(skill_md),        # Path -> str 便于序列化
                "size": skill_md.stat().st_size,  # stat().st_size 文件字节数
            })
    return skills


def main():
    """扫描 showcase 下的 skills 目录并打印摘要。"""
    print("=" * 50)
    print("07 - Skills Loader")
    print("=" * 50)

    # resolve() 解析为绝对路径；parents[1] 上溯两级到 openharness 根
    showcase_skills = Path(__file__).resolve().parents[1] / "showcase" / "02_company_skills" / "skills"
    found = discover_skills(showcase_skills)

    print(f"\n  扫描: {showcase_skills}")
    for s in found:
        # s 为 dict，['name'] / ['size'] 按键访问
        print(f"  - {s['name']} ({s['size']} bytes)")

    if not found:
        print("  (暂无 skill，完成 showcase/02 后可见)")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
