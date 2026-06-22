"""
09_map_reduce_pattern.py - 分治智能体模式

学习要点:
1. Map: Send API 并行处理多个子任务
2. Reduce: 聚合节点合并结果
3. 典型场景: 长文档分块分析、批量数据处理

前置: 03_parallel_send.py, stage-1/06_rag.py
"""
import operator
import os
from typing import Annotated

from dotenv import load_dotenv
from typing_extensions import TypedDict

load_dotenv()

from langchain.messages import HumanMessage
from langgraph.graph import END, START, StateGraph
from langgraph.types import Send

from model import getModel


class DocState(TypedDict):
    document: str
    chunks: list[str]
    analyses: Annotated[list[str], operator.add]
    final_summary: str


def split_document(state: DocState) -> dict:
    text = state["document"]
    chunk_size = 80
    chunks = [text[i:i + chunk_size] for i in range(0, len(text), chunk_size)]
    return {"chunks": chunks}


def fan_out_chunks(state: DocState) -> list[Send]:
    return [Send("analyze_chunk", {"chunk": c, "index": i}) for i, c in enumerate(state["chunks"])]


class ChunkState(TypedDict):
    chunk: str
    index: int


def analyze_chunk(state: ChunkState) -> dict:
    if not os.getenv("DEEPSEEK_API_KEY") and not os.getenv("OPENAI_API_KEY"):
        summary = f"[块{state['index']}] {state['chunk'][:40]}..."
    else:
        model = getModel(temperature=0)
        response = model.invoke([
            HumanMessage(content=f"用一句话概括以下文本要点:\n{state['chunk']}"),
        ])
        summary = f"[块{state['index']}] {response.content.strip()}"
    return {"analyses": [summary]}


def reduce_summaries(state: DocState) -> dict:
    if not os.getenv("DEEPSEEK_API_KEY") and not os.getenv("OPENAI_API_KEY"):
        combined = "\n".join(state["analyses"])
        return {"final_summary": f"Reduce 汇总 ({len(state['analyses'])} 块):\n{combined}"}

    model = getModel(temperature=0)
    bullet_points = "\n".join(state["analyses"])
    response = model.invoke([
        HumanMessage(content=f"将以下分块摘要合并为一段连贯总结:\n{bullet_points}"),
    ])
    return {"final_summary": response.content}


def build_map_reduce_graph():
    g = StateGraph(DocState)
    g.add_node("split", split_document)
    g.add_node("analyze_chunk", analyze_chunk)
    g.add_node("reduce", reduce_summaries)

    g.add_edge(START, "split")
    g.add_conditional_edges("split", fan_out_chunks, ["analyze_chunk"])
    g.add_edge("analyze_chunk", "reduce")
    g.add_edge("reduce", END)
    return g.compile()


def demo_map_reduce():
    print("\n=== Map-Reduce Agent Pattern ===")
    doc = (
        "LangGraph 是 LangChain 团队开发的状态图编排框架。"
        "它基于 StateGraph 构建有状态的多步骤 Agent 工作流。"
        "核心能力包括条件路由、断点恢复、人机协同和子图嵌套。"
        "通过 checkpoint 机制，工作流可以在任意节点暂停和恢复。"
        "Send API 支持动态并行，适合 Map-Reduce 等分治模式。"
    )

    app = build_map_reduce_graph()
    result = app.invoke({
        "document": doc,
        "chunks": [],
        "analyses": [],
        "final_summary": "",
    })

    print(f"  分块数: {len(result.get('chunks', []))}")
    print(f"  各块分析:")
    for a in result["analyses"]:
        print(f"    {a}")
    print(f"\n  最终汇总:\n{result['final_summary']}")


if __name__ == "__main__":
    print("=" * 60)
    print("09 - Map-Reduce Pattern")
    print("=" * 60)

    demo_map_reduce()

    print("\n核心要点:")
    print("1. split → fan_out(Send) → parallel workers → reduce")
    print("2. Annotated[list, operator.add] 自动合并并行分支输出")
    print("3. 长文档 RAG、批量分析、多源汇总的经典模式")
