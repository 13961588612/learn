"""
01_state_graph_basics.py - StateGraph 基础

学习要点:
1. StateGraph / Node / Edge / START / END
2. TypedDict 作为 State Schema
3. compile() 与 invoke() — 图即 Runnable
4. 节点单一职责：每个节点只改 state 的一部分

前置: stage-1/04_chains_lcel.py
"""
from typing_extensions import TypedDict

from langgraph.graph import END, START, StateGraph


# ========== State Schema ==========


class CounterState(TypedDict):
    """简单计数器状态"""

    count: int
    log: list[str]


# ========== Nodes ==========


def init_node(state: CounterState) -> dict:
    return {"count": 0, "log": ["初始化"]}


def increment_node(state: CounterState) -> dict:
    new_count = state["count"] + 1
    return {
        "count": new_count,
        "log": state["log"] + [f"increment → {new_count}"],
    }


def double_node(state: CounterState) -> dict:
    new_count = state["count"] * 2
    return {
        "count": new_count,
        "log": state["log"] + [f"double → {new_count}"],
    }


def build_counter_graph():
    """线性图: init → increment → double → END"""
    graph = StateGraph(CounterState)
    graph.add_node("init", init_node)
    graph.add_node("increment", increment_node)
    graph.add_node("double", double_node)

    graph.add_edge(START, "init")
    graph.add_edge("init", "increment")
    graph.add_edge("increment", "double")
    graph.add_edge("double", END)

    return graph.compile()


def demo_linear_graph():
    print("\n=== 线性 StateGraph ===")
    app = build_counter_graph()
    result = app.invoke({"count": 0, "log": []})
    print(f"最终 count: {result['count']}")
    print("执行日志:")
    for line in result["log"]:
        print(f"  {line}")


def demo_partial_state():
    """节点只需返回要更新的字段，LangGraph 自动 merge"""
    print("\n=== 部分状态更新 ===")

    class MiniState(TypedDict):
        a: int
        b: int

    def add_a(state: MiniState) -> dict:
        return {"a": state["a"] + 10}

    def add_b(state: MiniState) -> dict:
        return {"b": state["b"] + 100}

    g = StateGraph(MiniState)
    g.add_node("step_a", add_a)
    g.add_node("step_b", add_b)
    g.add_edge(START, "step_a")
    g.add_edge("step_a", "step_b")
    g.add_edge("step_b", END)

    out = g.compile().invoke({"a": 1, "b": 2})
    print(f"a={out['a']}, b={out['b']}  (期望 a=11, b=102)")


if __name__ == "__main__":
    print("=" * 60)
    print("01 - StateGraph 基础")
    print("=" * 60)

    demo_linear_graph()
    demo_partial_state()

    print("\n核心要点:")
    print("1. StateGraph(StateSchema) 定义图，节点签名 (state) -> partial_state")
    print("2. add_edge / add_conditional_edges 连接节点")
    print("3. compile() 得到可 invoke/stream 的 Runnable")
