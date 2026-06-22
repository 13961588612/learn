"""
06_streaming.py - LangGraph 流式输出

学习要点:
1. stream_mode='values': 每步完整 state
2. stream_mode='updates': 每步节点增量更新（推荐）
3. stream_mode='debug': 节点输入输出详情
4. 与 stage-1/08_streaming.py Agent 流式的区别

前置: stage-1/08_streaming.py, 01_state_graph_basics.py
"""
from typing_extensions import TypedDict

from langgraph.graph import END, START, StateGraph


class StreamState(TypedDict):
    items: list[str]
    processed: list[str]
    status: str


def load_items(state: StreamState) -> dict:
    return {"items": ["apple", "banana", "cherry"], "status": "loaded"}


def process_items(state: StreamState) -> dict:
    processed = [f"[OK] {item.upper()}" for item in state["items"]]
    return {"processed": processed, "status": "processed"}


def finalize(state: StreamState) -> dict:
    return {"status": f"done ({len(state['processed'])} items)"}


def build_graph():
    g = StateGraph(StreamState)
    g.add_node("load", load_items)
    g.add_node("process", process_items)
    g.add_node("finalize", finalize)
    g.add_edge(START, "load")
    g.add_edge("load", "process")
    g.add_edge("process", "finalize")
    g.add_edge("finalize", END)
    return g.compile()


def demo_stream_updates():
    print("\n=== stream_mode='updates' ===")
    app = build_graph()
    for i, chunk in enumerate(app.stream(
        {"items": [], "processed": [], "status": "init"},
        stream_mode="updates",
    )):
        node_name = list(chunk.keys())[0]
        update = chunk[node_name]
        print(f"  [{i + 1}] {node_name}: {update}")


def demo_stream_values():
    print("\n=== stream_mode='values' ===")
    app = build_graph()
    for i, state in enumerate(app.stream(
        {"items": [], "processed": [], "status": "init"},
        stream_mode="values",
    )):
        print(f"  [{i + 1}] status={state.get('status')}, processed={state.get('processed', [])}")


def demo_stream_debug():
    print("\n=== stream_mode='debug' (摘要) ===")
    app = build_graph()
    count = 0
    for event in app.stream(
        {"items": [], "processed": [], "status": "init"},
        stream_mode="debug",
    ):
        count += 1
        if count <= 3:
            print(f"  debug event keys: {list(event.keys()) if isinstance(event, dict) else type(event)}")
    print(f"  共 {count} 个 debug 事件")


if __name__ == "__main__":
    print("=" * 60)
    print("06 - LangGraph Streaming")
    print("=" * 60)

    demo_stream_updates()
    demo_stream_values()
    demo_stream_debug()

    print("\n核心要点:")
    print("1. graph.stream(..., stream_mode=...) 逐步输出")
    print("2. updates 只看增量，values 看完整 state，debug 看执行细节")
    print("3. Agent 场景 additionally 支持 stream_mode='messages' 逐 token")
