"""
08_supervisor_pattern.py - 监督者智能体模式

学习要点:
1. Supervisor 节点: 决定派给哪个 worker
2. Worker 节点: 各自处理专项任务
3. 循环: worker → supervisor 直到任务完成

前置: 02_conditional_edges.py, stage-1/03_tools.py
"""
import os

from dotenv import load_dotenv
from typing_extensions import TypedDict

load_dotenv()

from langchain.messages import HumanMessage, SystemMessage
from langgraph.graph import END, START, StateGraph

from model import getModel


class SupervisorState(TypedDict):
    task: str
    next_worker: str
    results: dict[str, str]
    final_answer: str
    iterations: int


WORKERS = ["researcher", "writer", "reviewer"]


def supervisor_node(state: SupervisorState) -> dict:
    """Supervisor 决定下一步派给谁"""
    model = getModel(temperature=0)

    completed = list(state.get("results", {}).keys())
    remaining = [w for w in WORKERS if w not in completed]

    if not remaining:
        return {"next_worker": "FINISH", "iterations": state["iterations"] + 1}

    prompt = f"""你是任务调度 supervisor。
任务: {state['task']}
已完成: {completed or '无'}
可选 worker: {remaining}

只回复一个 worker 名称 ({', '.join(remaining)}) 或 FINISH。"""

    response = model.invoke([SystemMessage(content=prompt)])
    choice = response.content.strip().lower()

    for w in WORKERS:
        if w in choice:
            return {"next_worker": w, "iterations": state["iterations"] + 1}

    return {"next_worker": remaining[0], "iterations": state["iterations"] + 1}


def make_worker(name: str, role: str):
    def worker(state: SupervisorState) -> dict:
        model = getModel(temperature=0.3)
        prompt = f"你是 {role}。任务: {state['task']}\n已有结果: {state.get('results', {})}\n请完成你的部分，简洁输出。"
        response = model.invoke([HumanMessage(content=prompt)])
        results = dict(state.get("results", {}))
        results[name] = response.content[:200]
        return {"results": results}

    return worker


def route_supervisor(state: SupervisorState) -> str:
    if state["next_worker"] == "FINISH" or state["iterations"] > 6:
        return "finalize"
    return state["next_worker"]


def finalize_node(state: SupervisorState) -> dict:
    parts = "\n".join(f"[{k}] {v}" for k, v in state.get("results", {}).items())
    return {"final_answer": f"Supervisor 汇总:\n{parts}"}


def build_supervisor_graph():
    g = StateGraph(SupervisorState)
    g.add_node("supervisor", supervisor_node)
    g.add_node("researcher", make_worker("researcher", "研究员，负责收集信息"))
    g.add_node("writer", make_worker("writer", "写作者，负责撰写内容"))
    g.add_node("reviewer", make_worker("reviewer", "审核员，负责质量检查"))
    g.add_node("finalize", finalize_node)

    g.add_edge(START, "supervisor")
    g.add_conditional_edges(
        "supervisor",
        route_supervisor,
        ["researcher", "writer", "reviewer", "finalize"],
    )
    for w in WORKERS:
        g.add_edge(w, "supervisor")
    g.add_edge("finalize", END)
    return g.compile()


def demo_supervisor():
    if not os.getenv("DEEPSEEK_API_KEY") and not os.getenv("OPENAI_API_KEY"):
        print("\n=== Supervisor Pattern (跳过: 未配置 API Key) ===")
        return

    print("\n=== Supervisor Agent Pattern ===")
    app = build_supervisor_graph()
    result = app.invoke({
        "task": "写一段 100 字左右的 LangGraph 入门介绍",
        "next_worker": "",
        "results": {},
        "final_answer": "",
        "iterations": 0,
    })
    print(result["final_answer"][:500])


if __name__ == "__main__":
    print("=" * 60)
    print("08 - Supervisor Pattern")
    print("=" * 60)

    demo_supervisor()

    print("\n核心要点:")
    print("1. Supervisor 循环调度多个 specialist worker")
    print("2. worker 完成后回到 supervisor 重新决策")
    print("3. 适合多角色协作: 研究→写作→审核")
