"""06_readonly_tool_pattern.py - 公司只读 Tool 模式"""

DOCS = [
    {"id": "D1", "title": "发布流程", "body": "需 CR"},
    {"id": "D2", "title": "故障手册", "body": "先 rollback"},
]


def search_internal_docs(query: str) -> str:
    """只读搜索内部文档索引。勿用于写操作。"""
    hits = [d for d in DOCS if query.lower() in d["title"].lower()]
    if not hits:
        return f"ERROR: 无匹配 {query!r}"
    return "\n".join(f"[{h['id']}] {h['title']}: {h['body']}" for h in hits)


def main():
    print("=" * 50)
    print("06 - Readonly Tool Pattern")
    print("=" * 50)
    print(search_internal_docs("发布"))
    print("\n  完整版: showcase/01_readonly_toolkit_audit/")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
