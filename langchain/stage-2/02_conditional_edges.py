"""
02_conditional_edges.py - 条件路由

学习要点:
1. add_conditional_edges: 根据 state 动态选择下一节点
2. 路由函数返回节点名或 END
3. 结合 LLM 做意图分类路由

前置: 01_state_graph_basics.py
"""
import os
from typing import Literal

from dotenv import load_dotenv
from typing_extensions import TypedDict

load_dotenv()

from langgraph.graph import END, START, StateGraph


class RouterState(TypedDict):
    query: str
    intent: str
    response: str


# ========== 规则路由（无需 API） ==========


def classify_intent(state: RouterState) -> dict:
    q = state["query"].lower()
    if any(w in q for w in ("价格", "多少钱", "费用")):
        intent = "pricing"
    elif any(w in q for w in ("退货", "退款", "售后")):
        intent = "support"
    else:
        intent = "general"
    return {"intent": intent}


def route_by_intent(state: RouterState) -> str:
    mapping = {
        "pricing": "pricing_node",
        "support": "support_node",
        "general": "general_node",
    }
    return mapping.get(state["intent"], "general_node")


def pricing_node(state: RouterState) -> dict:
    return {"response": "标准版 99 元/月，企业版请联系销售。"}


def support_node(state: RouterState) -> dict:
    return {"response": "7 天无理由退货，请保留原包装并联系客服。"}


def general_node(state: RouterState) -> dict:
    return {"response": "您好，请问有什么可以帮您？"}


def build_rule_router():
    g = StateGraph(RouterState)
    g.add_node("classify", classify_intent)
    g.add_node("pricing_node", pricing_node)
    g.add_node("support_node", support_node)
    g.add_node("general_node", general_node)

    g.add_edge(START, "classify")
    g.add_conditional_edges(
        "classify",
        route_by_intent,
        ["pricing_node", "support_node", "general_node"],
    )
    g.add_edge("pricing_node", END)
    g.add_edge("support_node", END)
    g.add_edge("general_node", END)
    return g.compile()


def demo_rule_router():
    print("\n=== 规则条件路由 ===")
    app = build_rule_router()
    queries = [
        "你们产品多少钱？",
        "我想申请退货",
        "LangGraph 是什么？",
    ]
    for q in queries:
        result = app.invoke({"query": q, "intent": "", "response": ""})
        print(f"  Q: {q}")
        print(f"  intent={result['intent']} → {result['response']}\n")


# ========== LLM 路由（需 API） ==========


class LLMRouterState(TypedDict):
    query: str
    category: Literal["tech", "biz", ""]
    answer: str


def demo_llm_router():
    """用 LLM structured output 做路由决策"""
    if not os.getenv("OPENAI_API_KEY") and not os.getenv("DEEPSEEK_API_KEY"):
        print("\n=== LLM 条件路由 (跳过: 未配置 API Key) ===")
        return

    print("\n=== LLM 条件路由 ===")

    try:
        from pydantic import BaseModel, Field
        from langchain.chat_models import init_chat_model
    except ImportError:
        print("  跳过: 请先在项目根目录运行 uv sync")
        return

    class RouteDecision(BaseModel):
        category: Literal["tech", "biz"] = Field(description="tech=技术问题, biz=商务问题")

    model = init_chat_model(
        "openai:gpt-4o-mini" if os.getenv("OPENAI_API_KEY") else "deepseek:deepseek-chat",
        temperature=0,
    )
    router = model.with_structured_output(RouteDecision)

    def llm_classify(state: LLMRouterState) -> dict:
        decision = router.invoke(f"分类用户问题:\n{state['query']}")
        return {"category": decision.category}

    def llm_route(state: LLMRouterState) -> str:
        return "tech_node" if state["category"] == "tech" else "biz_node"

    def tech_node(state: LLMRouterState) -> dict:
        return {"answer": "[技术] 建议使用 StateGraph 编排多步工作流。"}

    def biz_node(state: LLMRouterState) -> dict:
        return {"answer": "[商务] 请联系 sales@example.com 获取报价。"}

    g = StateGraph(LLMRouterState)
    g.add_node("classify", llm_classify)
    g.add_node("tech_node", tech_node)
    g.add_node("biz_node", biz_node)
    g.add_edge(START, "classify")
    g.add_conditional_edges("classify", llm_route, ["tech_node", "biz_node"])
    g.add_edge("tech_node", END)
    g.add_edge("biz_node", END)

    app = g.compile()
    result = app.invoke({
        "query": "LangGraph 的 checkpoint 怎么持久化？",
        "category": "",
        "answer": "",
    })
    print(f"  category={result['category']}")
    print(f"  answer={result['answer']}")


if __name__ == "__main__":
    print("=" * 60)
    print("02 - 条件路由 (Conditional Edges)")
    print("=" * 60)

    demo_rule_router()
    demo_llm_router()

    print("\n核心要点:")
    print("1. add_conditional_edges(source, router_fn, targets)")
    print("2. router_fn 返回下一节点名，必须在 targets 列表中")
    print("3. 简单场景用规则，复杂意图用 LLM + structured output")
