"""
03_parallel_send.py - 并行节点 (Send API)

学习要点:
1. Send: 动态 fan-out，为每个 item 派生子任务
2. 聚合节点: 收集并行结果
3. 适用 Map-Reduce 中的 Map 阶段

前置: 01_state_graph_basics.py
"""
import operator
from typing import Annotated

from typing_extensions import TypedDict

from langgraph.graph import END, START, StateGraph
from langgraph.types import Send


class MapReduceState(TypedDict):
    topics: list[str]
    drafts: Annotated[list[str], operator.add]
    summary: str


def fan_out(state: MapReduceState) -> list[Send]:
    """为每个 topic 发送一个 worker 任务"""
    return [Send("worker", {"topic": topic}) for topic in state["topics"]]


class WorkerState(TypedDict):
    topic: str


def worker_node(state: WorkerState) -> dict:
    topic = state["topic"]
    draft = f"[{topic}] 要点: 这是关于 {topic} 的简要分析。"
    return {"drafts": [draft]}


def summarize_node(state: MapReduceState) -> dict:
    combined = "\n".join(f"- {d}" for d in state["drafts"])
    return {"summary": f"共 {len(state['drafts'])} 份报告:\n{combined}"}


def build_map_graph():
    g = StateGraph(MapReduceState)
    g.add_node("worker", worker_node)
    g.add_node("summarize", summarize_node)

    g.add_conditional_edges(START, fan_out, ["worker"])
    g.add_edge("worker", "summarize")
    g.add_edge("summarize", END)
    return g.compile()


def demo_parallel_send():
    print("\n=== Send API 并行 fan-out ===")
    app = build_map_graph()
    result = app.invoke({
        "topics": ["AI", "区块链", "量子计算"],
        "drafts": [],
        "summary": "",
    })
    print(result["summary"])


if __name__ == "__main__":
    print("=" * 60)
    print("03 - 并行节点 (Send API)")
    print("=" * 60)

    demo_parallel_send()

    print("\n核心要点:")
    print("1. Send(node_name, partial_state) 动态创建并行分支")
    print("2. Annotated[list, operator.add] 用于聚合多分支返回值")
    print("3. Map-Reduce 模式: fan_out → workers → summarize")
