"""search_internal_docs - 公司内部文档只读搜索 Tool"""

from pydantic import BaseModel, Field  # BaseModel 数据校验；Field 约束字段

# 模块级常量：模拟内部文档索引（list of dict）
DOCS = [
    {"id": "D1", "title": "发布流程", "body": "staging -> prod，需 CR 审批"},
    {"id": "D2", "title": "故障手册", "body": "P0 先 rollback，再根因"},
    {"id": "D3", "title": "安全基线", "body": "禁止明文密钥入库"},
]


# 继承 BaseModel：构造时自动校验 query/limit 约束
class SearchDocsInput(BaseModel):
    query: str = Field(min_length=1, max_length=100, description="搜索关键词")
    limit: int = Field(default=5, ge=1, le=10)  # default=5；ge/le 上下界


def search_internal_docs(params: SearchDocsInput) -> str:
    """
    搜索公司内部文档索引（只读）。

    When to use:
    - 用户询问发布、故障、规范等内部流程

    Do NOT use:
    - 修改文档
    - 查询员工私人信息
    """
    q = params.query.lower()  # 转小写便于不区分大小写匹配
    # 列表推导：标题或正文包含 q 的文档
    hits = [d for d in DOCS if q in d["title"].lower() or q in d["body"].lower()]
    hits = hits[: params.limit]  # 切片取前 limit 条
    if not hits:
        return f"ERROR: 无匹配 {params.query!r}"  # !r 用 repr 显示引号
    # 生成器表达式 + join：每行 "[id] title: body"
    return "\n".join(f"[{h['id']}] {h['title']}: {h['body']}" for h in hits)


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    print(search_internal_docs(SearchDocsInput(query="发布")))
