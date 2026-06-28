"""
06_skill_md_format.py - SKILL.md frontmatter 解析

学习要点:
1. YAML frontmatter: name, description
2. 正文：When to use / Steps / Do NOT
"""

import re  # 正则表达式模块，用于匹配 frontmatter 分隔块
from pathlib import Path  # 路径读写


def parse_skill_md(text: str) -> dict:
    """
    解析 SKILL.md：提取 --- 包裹的 YAML frontmatter 与正文。
    返回 {"meta": dict, "body": str}。
    """
    # re.match 从字符串开头匹配；(.*?) 非贪婪捕获；re.DOTALL 让 . 匹配换行
    match = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not match:
        # 无 frontmatter 时返回空 meta 与去空白后的全文
        return {"meta": {}, "body": text.strip()}

    # group(1) 第一个捕获组（frontmatter）；strip() 去首尾空白
    meta_lines = match.group(1).strip().splitlines()  # splitlines 按行分割
    meta = {}
    for line in meta_lines:
        if ":" in line:
            # split(":", 1) 只分割第一个冒号，避免值中含冒号被误切
            k, v = line.split(":", 1)
            # 链式 strip：去空白并去掉值两侧引号
            meta[k.strip()] = v.strip().strip('"')
    return {"meta": meta, "body": match.group(2).strip()}


def main():
    """从 showcase 或内联字符串演示 frontmatter 解析。"""
    print("=" * 50)
    print("06 - SKILL.md Format")
    print("=" * 50)

    # parents[1] 上两级目录，定位 showcase 下的示例 SKILL.md
    sample = Path(__file__).parent.parent / "showcase" / "02_company_skills" / "skills" / "incident-response" / "SKILL.md"
    if sample.exists():
        # read_text(encoding="utf-8") 读取文件为 str
        parsed = parse_skill_md(sample.read_text(encoding="utf-8"))
        # dict.get(key) 安全取值，缺失返回 None
        print(f"  name: {parsed['meta'].get('name')}")
        # 切片 [:60] 只显示 description 前 60 字符
        print(f"  description: {parsed['meta'].get('description', '')[:60]}...")
    else:
        print("  (showcase skill 尚未创建，跳过文件读取)")

    # 三引号多行字符串，模拟完整 SKILL.md 内容
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
