"""
04_checkpointing.py - 断点持久化

学习要点:
1. MemorySaver: 内存 checkpoint（开发调试）
2. SqliteSaver: 文件持久化，进程重启可恢复
3. thread_id: 会话隔离键
4. get_state / update_state: 读取与手动修正状态

前置: stage-1/10_check_pointer.py
"""
import os
import tempfile

from dotenv import load_dotenv
from typing_extensions import TypedDict

load_dotenv()

from langgraph.checkpoint.memory import MemorySaver
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import END, START, StateGraph


class WorkflowState(TypedDict):
    step: int
    history: list[str]


def step_one(state: WorkflowState) -> dict:
    return {"step": 1, "history": state["history"] + ["完成步骤 1"]}


def step_two(state: WorkflowState) -> dict:
    return {"step": 2, "history": state["history"] + ["完成步骤 2"]}


def step_three(state: WorkflowState) -> dict:
    return {"step": 3, "history": state["history"] + ["完成步骤 3"]}


def build_workflow():
    g = StateGraph(WorkflowState)
    g.add_node("step1", step_one)
    g.add_node("step2", step_two)
    g.add_node("step3", step_three)
    g.add_edge(START, "step1")
    g.add_edge("step1", "step2")
    g.add_edge("step2", "step3")
    g.add_edge("step3", END)
    return g


def demo_memory_saver():
    print("\n=== MemorySaver 内存 checkpoint ===")
    checkpointer = MemorySaver()
    app = build_workflow().compile(checkpointer=checkpointer)
    config = {"configurable": {"thread_id": "demo-thread-1"}}

    result = app.invoke({"step": 0, "history": []}, config=config)
    print(f"  执行结果: step={result['step']}, history={result['history']}")

    saved = app.get_state(config)
    print(f"  get_state: next={saved.next}, values.step={saved.values.get('step')}")


def demo_sqlite_saver():
    print("\n=== SqliteSaver 文件持久化 ===")
    db_path = os.path.join(tempfile.gettempdir(), "langgraph_learn_stage2.db")
    print(f"  数据库: {db_path}")

    with SqliteSaver.from_conn_string(db_path) as checkpointer:
        app = build_workflow().compile(checkpointer=checkpointer)
        config = {"configurable": {"thread_id": "sqlite-thread-1"}}

        result = app.invoke({"step": 0, "history": []}, config=config)
        print(f"  首次运行: {result['history']}")

    with SqliteSaver.from_conn_string(db_path) as checkpointer:
        app = build_workflow().compile(checkpointer=checkpointer)
        saved = app.get_state(config)
        print(f"  重启后恢复: step={saved.values.get('step')}, history={saved.values.get('history')}")


def demo_update_state():
    print("\n=== update_state 手动修正 ===")
    checkpointer = MemorySaver()
    app = build_workflow().compile(checkpointer=checkpointer)
    config = {"configurable": {"thread_id": "update-demo"}}

    app.invoke({"step": 0, "history": ["用户输入"]}, config=config)

    app.update_state(
        config,
        {"history": ["用户输入", "人工修正: 跳过步骤1"]},
        as_node="step1",
    )

    result = app.invoke(None, config=config)
    print(f"  从 step1 继续: {result['history']}")


if __name__ == "__main__":
    print("=" * 60)
    print("04 - Checkpointing 断点持久化")
    print("=" * 60)

    demo_memory_saver()
    demo_sqlite_saver()
    demo_update_state()

    print("\n核心要点:")
    print("1. compile(checkpointer=...) 启用状态快照")
    print("2. config={'configurable': {'thread_id': '...'}} 隔离会话")
    print("3. MemorySaver 调试用，SqliteSaver/PostgresSaver 生产用")
    print("4. get_state / update_state 支持人工干预与恢复")
