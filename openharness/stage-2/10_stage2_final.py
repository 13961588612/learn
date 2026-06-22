"""
10_stage2_final.py - 综合：Tool + Hook + Skill 发现

学习要点:
1. 注册自定义 Tool
2. Pre/Post Hook + 审计
3. 列出可用 Skills
"""

import json
from dataclasses import dataclass, field
from pathlib import Path

from pydantic import BaseModel, Field


class LookupInput(BaseModel):
    employee_id: str = Field(min_length=3, max_length=10)


MOCK_DIR = {"E001": "Alice / Eng", "E002": "Bob / SRE"}


@dataclass
class ToolRegistry:
    audit: list[dict] = field(default_factory=list)

    def lookup_employee(self, params: LookupInput) -> str:
        self.audit.append({"tool": "lookup_employee", "id": params.employee_id})
        info = MOCK_DIR.get(params.employee_id)
        if not info:
            return f"ERROR: 未找到 {params.employee_id}"
        return info


def list_skills() -> list[str]:
    root = Path(__file__).resolve().parents[1] / "showcase" / "02_company_skills" / "skills"
    if not root.exists():
        return []
    return [p.name for p in root.iterdir() if (p / "SKILL.md").exists()]


def main():
    print("=" * 50)
    print("10 - Stage 2 Final")
    print("=" * 50)

    reg = ToolRegistry()
    print(f"\n  lookup: {reg.lookup_employee(LookupInput(employee_id='E001'))}")
    print(f"  audit: {json.dumps(reg.audit, ensure_ascii=False)}")

    skills = list_skills()
    print(f"\n  skills: {skills or '(完成 showcase/02 后可见)'}")

    print("\n[OK] 阶段二综合练习完成")


if __name__ == "__main__":
    main()
