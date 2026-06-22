"""
05_human_in_the_loop.py - 人机协同

学习要点:
1. interrupt(): 节点内暂停，等待人工输入
2. interrupt_before / interrupt_after: 编译时指定暂停点
3. Command(resume=...): 携带人工反馈恢复执行
4. 必须配合 checkpointer 使用

前置: 04_checkpointing.py
"""
from typing_extensions import TypedDict

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt


class ApprovalState(TypedDict):
    request: str
    approved: bool | None
    result: str


def submit_request(state: ApprovalState) -> dict:
    return {"request": state["request"], "result": "已提交审批"}


def human_review(state: ApprovalState) -> dict:
    """interrupt 暂停，等待人工 decision"""
    decision = interrupt({
        "action": "review",
        "request": state["request"],
        "prompt": "请审批此请求 (输入 true/false):",
    })
    approved = decision if isinstance(decision, bool) else str(decision).lower() in ("true", "yes", "1")
    status = "已批准" if approved else "已拒绝"
    return {"approved": approved, "result": f"{status}: {state['request']}"}


def execute_action(state: ApprovalState) -> dict:
    if state.get("approved"):
        return {"result": f"执行成功 → {state['request']}"}
    return {"result": "操作已取消"}


def build_approval_graph():
    g = StateGraph(ApprovalState)
    g.add_node("submit", submit_request)
    g.add_node("review", human_review)
    g.add_node("execute", execute_action)
    g.add_edge(START, "submit")
    g.add_edge("submit", "review")
    g.add_edge("review", "execute")
    g.add_edge("execute", END)
    return g


def demo_interrupt():
    print("\n=== interrupt() 人机协同 ===")
    checkpointer = MemorySaver()
    app = build_approval_graph().compile(checkpointer=checkpointer)
    config = {"configurable": {"thread_id": "hitl-1"}}

    result = app.invoke(
        {"request": "删除生产数据库备份", "approved": None, "result": ""},
        config=config,
    )

    state = app.get_state(config)
    if state.next:
        print("  图已暂停，等待人工审批...")
        if hasattr(result, "__interrupt__") or (isinstance(result, dict) and result.get("__interrupt__")):
            interrupts = getattr(result, "__interrupt__", result.get("__interrupt__"))
            print(f"  中断信息: {interrupts}")

        result = app.invoke(Command(resume=True), config=config)

    print(f"  最终结果: {result.get('result', result)}")


def demo_interrupt_before():
    print("\n=== interrupt_before 编译时暂停 ===")
    checkpointer = MemorySaver()

    class SimpleState(TypedDict):
        value: str

    def risky_op(state: SimpleState) -> dict:
        return {"value": state["value"] + " [已执行]"}

    g = StateGraph(SimpleState)
    g.add_node("risky", risky_op)
    g.add_edge(START, "risky")
    g.add_edge("risky", END)

    app = g.compile(
        checkpointer=checkpointer,
        interrupt_before=["risky"],
    )
    config = {"configurable": {"thread_id": "hitl-before-1"}}

    app.invoke({"value": "敏感操作"}, config=config)
    state = app.get_state(config)
    print(f"  暂停于 risky 之前, next={state.next}, value={state.values.get('value')}")

    result = app.invoke(None, config=config)
    print(f"  恢复后: {result['value']}")


if __name__ == "__main__":
    print("=" * 60)
    print("05 - Human-in-the-Loop 人机协同")
    print("=" * 60)

    demo_interrupt()
    demo_interrupt_before()

    print("\n核心要点:")
    print("1. interrupt(payload) 在节点内暂停，返回 __interrupt__")
    print("2. Command(resume=...) 携带人工反馈继续执行")
    print("3. interrupt_before/after 在 compile 时声明暂停点")
    print("4. 生产场景: 敏感操作审批、表单确认、人工纠错")
