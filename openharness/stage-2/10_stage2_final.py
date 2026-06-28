"""
10_stage2_final.py - 综合：Tool + Hook + Skill 发现

学习要点:
1. 注册自定义 Tool
2. Pre/Post Hook + 审计
3. 列出可用 Skills
"""

import json  # dumps 格式化 audit 列表输出
from dataclasses import dataclass, field  # dataclass 简化类定义；field 处理默认值
from pathlib import Path  # 扫描 skills 目录

from pydantic import BaseModel, Field  # Tool 入参校验


class LookupInput(BaseModel):
    """员工查询 Tool 的入参模型。"""

    employee_id: str = Field(min_length=3, max_length=10)


# 模拟员工 ID -> 部门信息映射
MOCK_DIR = {"E001": "Alice / Eng", "E002": "Bob / SRE"}


@dataclass
class ToolRegistry:
    """
    简易 Tool 注册表：封装 lookup_employee 并记录 audit 日志。
    """

    # default_factory=list 保证每个实例有独立 audit 列表
    audit: list[dict] = field(default_factory=list)

    def lookup_employee(self, params: LookupInput) -> str:
        """根据 employee_id 查询 mock 目录；未找到返回 ERROR 前缀。"""
        # append 追加审计条目，供 PostToolUse 类场景演示
        self.audit.append({"tool": "lookup_employee", "id": params.employee_id})
        info = MOCK_DIR.get(params.employee_id)  # .get 缺失时返回 None
        if not info:
            return f"ERROR: 未找到 {params.employee_id}"
        return info


def list_skills() -> list[str]:
    """
    扫描 showcase skills 目录，返回含 SKILL.md 的子目录名列表。
    """
    root = Path(__file__).resolve().parents[1] / "showcase" / "02_company_skills" / "skills"
    if not root.exists():
        return []
    # 列表推导 + 条件：(p / "SKILL.md").exists() 过滤有效 skill 目录
    return [p.name for p in root.iterdir() if (p / "SKILL.md").exists()]


def main():
    """综合演示 Tool 调用、audit 与 skills 列表。"""
    print("=" * 50)
    print("10 - Stage 2 Final")
    print("=" * 50)

    reg = ToolRegistry()
    print(f"\n  lookup: {reg.lookup_employee(LookupInput(employee_id='E001'))}")
    # ensure_ascii=False 保留中文；json.dumps 将 list[dict] 转为 JSON 字符串
    print(f"  audit: {json.dumps(reg.audit, ensure_ascii=False)}")

    skills = list_skills()
    # or 短路：skills 非空用 skills，否则用提示字符串
    print(f"\n  skills: {skills or '(完成 showcase/02 后可见)'}")

    print("\n[OK] 阶段二综合练习完成")


if __name__ == "__main__":
    main()
