"""
02_custom_tool_pydantic.py - 自定义只读 Tool + Pydantic schema

学习要点:
1. Tool 输入用 Pydantic 校验
2. 失败返回 ERROR: 引导模型纠错
"""

from pydantic import BaseModel, Field  # BaseModel=数据模型基类；Field=字段约束与元数据


class SearchDocsInput(BaseModel):
    """
    Tool 入参模型：继承 BaseModel 后自动获得校验、序列化能力。
    字段注解 + Field(...) 在实例化时触发校验。
    """

    # str 类型；Field 约束 min_length/max_length 与 description（供 schema 生成）
    query: str = Field(min_length=1, max_length=200, description="搜索关键词")
    # default=5 表示可选参数；ge/le 限制数值范围 [1, 20]
    limit: int = Field(default=5, ge=1, le=20)


# 列表字面量；元素为 dict，键值对用 "key": value 表示
MOCK_DOCS = [
    {"title": "发布流程", "snippet": "staging -> prod"},
    {"title": "故障手册", "snippet": "P0 先 rollback"},
    {"title": "Onboarding", "snippet": "申请 VPN 与账号"},
]


def search_internal_docs(params: SearchDocsInput) -> str:
    """
    模拟内部文档搜索 Tool。
    params 已是校验通过的 SearchDocsInput 实例。
    """
    # 列表推导：[表达式 for 变量 in 可迭代 if 条件]
    hits = [d for d in MOCK_DOCS if params.query.lower() in d["title"].lower()]
    # 切片 [:n] 取前 n 个元素，等价于 hits = hits[0:params.limit]
    hits = hits[: params.limit]
    if not hits:
        # !r 调用 repr()，输出带引号的字符串字面量形式，便于调试
        return f"ERROR: 未找到与 {params.query!r} 相关的文档"
    # 推导式生成格式化字符串列表
    lines = [f"- {h['title']}: {h['snippet']}" for h in hits]
    # "\n".join 用换行符连接列表，得到多行文本
    return "\n".join(lines)


def main():
    """演示合法/非法 Pydantic 输入与 Tool 返回。"""
    print("=" * 50)
    print("02 - Custom Tool (Pydantic)")
    print("=" * 50)

    # 关键字参数构造模型；校验通过则正常实例化
    ok = SearchDocsInput(query="发布")
    print(f"\n  合法输入: {search_internal_docs(ok)}")

    # try/except 捕获校验异常（如 min_length 不满足）
    try:
        bad = SearchDocsInput(query="")  # 空字符串违反 min_length=1
    except Exception as e:
        print(f"\n  校验失败: {e}")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
