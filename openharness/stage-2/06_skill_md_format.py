"""
06_skill_md_format.py - SKILL.md frontmatter 解析

学习要点:
1. YAML frontmatter: name, description
2. 正文：When to use / Steps / Do NOT
"""

import re
from pathlib import Path


def parse_skill_md(text: str) -> dict:
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not match:
        return {"meta": {}, "body": text.strip()}

    meta_lines = match.group(1).strip().splitlines()
    meta = {}
    for line in meta_lines:
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"')
    return {"meta": meta, "body": match.group(2).strip()}


def main():
    print("=" * 50)
    print("06 - SKILL.md Format")
    print("=" * 50)

    sample = Path(__file__).parent.parent / "showcase" / "02_company_skills" / "skills" / "incident-response" / "SKILL.md"
    if sample.exists():
        parsed = parse_skill_md(sample.read_text(encoding="utf-8"))
        print(f"  name: {parsed['meta'].get('name')}")
        print(f"  description: {parsed['meta'].get('description', '')[:60]}...")
    else:
        print("  (showcase skill 尚未创建，跳过文件读取)")

    inline = """---
name: demo-skill
description: Demo skill for learning
---

# Demo

## When to use
- Learning only
"""
    parsed = parse_skill_md(inline)
    print(f"\n  内联示例 meta: {parsed['meta']}")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
