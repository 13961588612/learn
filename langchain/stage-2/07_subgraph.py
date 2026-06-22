"""
07_subgraph.py - 子图嵌套

学习要点:
1. 子图 compile 后作为节点 add_node
2. 共享 State Schema 或独立 Schema + 输入输出映射
3. 模块化: 复杂工作流拆分为可复用子图

前置: 01_state_graph_basics.py
"""
from typing_extensions import TypedDict

from langgraph.graph import END, START, StateGraph


# ========== 子图: 文本预处理 ==========


class PreprocessState(TypedDict):
    raw_text: str
    cleaned: str
    word_count: int


def strip_whitespace(state: PreprocessState) -> dict:
    cleaned = " ".join(state["raw_text"].split())
    return {"cleaned": cleaned}


def count_words(state: PreprocessState) -> dict:
    return {"word_count": len(state["cleaned"])}


def build_preprocess_subgraph():
    g = StateGraph(PreprocessState)
    g.add_node("strip", strip_whitespace)
    g.add_node("count", count_words)
    g.add_edge(START, "strip")
    g.add_edge("strip", "count")
    g.add_edge("count", END)
    return g.compile()


# ========== 主图: 文档处理流水线 ==========


class PipelineState(TypedDict):
    raw_text: str
    cleaned: str
    word_count: int
    report: str


def generate_report(state: PipelineState) -> dict:
    report = (
        f"文档统计\n"
        f"  原文长度: {len(state['raw_text'])} 字符\n"
        f"  清洗后: {len(state['cleaned'])} 字符\n"
        f"  词数: {state['word_count']}"
    )
    return {"report": report}


def build_pipeline():
    preprocess = build_preprocess_subgraph()

    g = StateGraph(PipelineState)
    g.add_node("preprocess", preprocess)
    g.add_node("report", generate_report)
    g.add_edge(START, "preprocess")
    g.add_edge("preprocess", "report")
    g.add_edge("report", END)
    return g.compile()


def demo_subgraph():
    print("\n=== 子图嵌套 ===")
    app = build_pipeline()
    text = "  LangGraph   支持   子图   嵌套。\n  便于模块化复用。  "
    result = app.invoke({
        "raw_text": text,
        "cleaned": "",
        "word_count": 0,
        "report": "",
    })
    print(result["report"])


def demo_reusable_subgraph():
    """同一子图被多个主图复用"""
    print("\n=== 子图复用 ===")
    preprocess = build_preprocess_subgraph()

    class ShortState(TypedDict):
        raw_text: str
        cleaned: str
        word_count: int
        label: str

    def label_node(state: ShortState) -> dict:
        label = "长文" if state["word_count"] > 5 else "短文"
        return {"label": label}

    g = StateGraph(ShortState)
    g.add_node("preprocess", preprocess)
    g.add_node("label", label_node)
    g.add_edge(START, "preprocess")
    g.add_edge("preprocess", "label")
    g.add_edge("label", END)

    for text in ["Hello world", "This is a longer sentence with many words"]:
        out = g.compile().invoke({
            "raw_text": text, "cleaned": "", "word_count": 0, "label": "",
        })
        print(f"  '{text[:30]}...' → {out['word_count']} 词, {out['label']}")


if __name__ == "__main__":
    print("=" * 60)
    print("07 - Subgraph 子图")
    print("=" * 60)

    demo_subgraph()
    demo_reusable_subgraph()

    print("\n核心要点:")
    print("1. subgraph = StateGraph(...).compile() 可作为节点嵌入主图")
    print("2. 子图与主图共享 State Schema 时无需额外映射")
    print("3. 复杂 Agent 工作流建议拆分为独立子图模块")
