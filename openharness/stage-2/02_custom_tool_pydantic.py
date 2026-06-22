"""
02_custom_tool_pydantic.py - 自定义只读 Tool + Pydantic schema

学习要点:
1. Tool 输入用 Pydantic 校验
2. 失败返回 ERROR: 引导模型纠错
"""

from pydantic import BaseModel, Field


class SearchDocsInput(BaseModel):
    query: str = Field(min_length=1, max_length=200, description="搜索关键词")
    limit: int = Field(default=5, ge=1, le=20)


MOCK_DOCS = [
    {"title": "发布流程", "snippet": "staging -> prod"},
    {"title": "故障手册", "snippet": "P0 先 rollback"},
    {"title": "Onboarding", "snippet": "申请 VPN 与账号"},
]


def search_internal_docs(params: SearchDocsInput) -> str:
    hits = [d for d in MOCK_DOCS if params.query.lower() in d["title"].lower()]
    hits = hits[: params.limit]
    if not hits:
        return f"ERROR: 未找到与 {params.query!r} 相关的文档"
    lines = [f"- {h['title']}: {h['snippet']}" for h in hits]
    return "\n".join(lines)


def main():
    print("=" * 50)
    print("02 - Custom Tool (Pydantic)")
    print("=" * 50)

    ok = SearchDocsInput(query="发布")
    print(f"\n  合法输入: {search_internal_docs(ok)}")

    try:
        bad = SearchDocsInput(query="")
    except Exception as e:
        print(f"\n  校验失败: {e}")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
