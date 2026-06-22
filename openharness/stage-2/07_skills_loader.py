"""
07_skills_loader.py - 扫描 .openharness/skills/ 目录

学习要点:
1. 每个 skill 一个子目录 + SKILL.md
2. 项目级 vs 用户级 skills 路径
"""

from pathlib import Path


def discover_skills(root: Path) -> list[dict]:
    if not root.exists():
        return []
    skills = []
    for child in sorted(root.iterdir()):
        if not child.is_dir():
            continue
        skill_md = child / "SKILL.md"
        if skill_md.exists():
            skills.append({
                "name": child.name,
                "path": str(skill_md),
                "size": skill_md.stat().st_size,
            })
    return skills


def main():
    print("=" * 50)
    print("07 - Skills Loader")
    print("=" * 50)

    showcase_skills = Path(__file__).resolve().parents[1] / "showcase" / "02_company_skills" / "skills"
    found = discover_skills(showcase_skills)

    print(f"\n  扫描: {showcase_skills}")
    for s in found:
        print(f"  - {s['name']} ({s['size']} bytes)")

    if not found:
        print("  (暂无 skill，完成 showcase/02 后可见)")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
