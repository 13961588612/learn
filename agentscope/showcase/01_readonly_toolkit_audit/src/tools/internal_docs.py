"""search_internal_docs - 公司内部文档只读 Tool"""

DOCS = [
    {"id": "D1", "title": "发布流程", "body": "staging -> prod，需 CR 审批"},
    {"id": "D2", "title": "故障手册", "body": "P0 先 rollback，再根因"},
    {"id": "D3", "title": "安全基线", "body": "禁止明文密钥入库"},
]


def search_internal_docs(query: str) -> str:
    """
    搜索公司内部文档索引（只读）。

    Args:
        query: 搜索关键词

    When to use:
    - 用户询问发布、故障、规范等内部流程

    Do NOT use:
    - 修改文档或查询私人信息
    """
    q = query.lower()
    hits = [d for d in DOCS if q in d["title"].lower() or q in d["body"].lower()]
    if not hits:
        return f"ERROR: 无匹配 {query!r}"
    return "\n".join(f"[{h['id']}] {h['title']}: {h['body']}" for h in hits)
