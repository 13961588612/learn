"""
10_agent_final.py - 阶段二综合验收

学习要点:
1. 3+ 节点工作流: 分析 → 生成 → 审核 → (人工) → 发布
2. Checkpointing: SqliteSaver 持久化
3. Human-in-the-Loop: 审核节点 interrupt 等待确认
4. Streaming: stream_mode='updates' 观察进度

验收标准:
- 包含 3+ 节点的多步工作流
- 支持人机协同 (interrupt)
- 支持断点恢复 (checkpointer)

前置: stage-2 全部脚本
"""
import os
import tempfile

from dotenv import load_dotenv
from typing_extensions import TypedDict

load_dotenv()

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph
from langgraph.types import Command, interrupt

from model import getModel


class ContentPipelineState(TypedDict):
    topic: str
    outline: str
    draft: str
    review_notes: str
    approved: bool | None
    published: str
    status: str


def analyze_topic(state: ContentPipelineState) -> dict:
    if os.getenv("DEEPSEEK_API_KEY") or os.getenv("OPENAI_API_KEY"):
        model = getModel(temperature=0)
        resp = model.invoke(f"为「{state['topic']}」生成 3 点内容大纲，每点一行。")
        outline = resp.content
    else:
        outline = f"1. {state['topic']} 概述\n2. 核心概念\n3. 实践建议"
    return {"outline": outline, "status": "analyzed"}


def write_draft(state: ContentPipelineState) -> dict:
    if os.getenv("DEEPSEEK_API_KEY") or os.getenv("OPENAI_API_KEY"):
        model = getModel(temperature=0.5)
        resp = model.invoke(
            f"根据大纲写一段 150 字以内的短文:\n大纲:\n{state['outline']}"
        )
        draft = resp.content
    else:
        draft = f"关于 {state['topic']} 的示例文章（模拟草稿）。"
    return {"draft": draft, "status": "drafted"}


def auto_review(state: ContentPipelineState) -> dict:
    notes = []
    if len(state["draft"]) < 50:
        notes.append("内容过短")
    if len(state["draft"]) > 500:
        notes.append("内容过长")
    if not notes:
        notes.append("自动审核通过，等待人工确认")
    return {"review_notes": "; ".join(notes), "status": "reviewed"}


def human_approval(state: ContentPipelineState) -> dict:
    decision = interrupt({
        "action": "publish_review",
        "topic": state["topic"],
        "draft_preview": state["draft"][:200],
        "review_notes": state["review_notes"],
        "prompt": "确认发布? (true/false)",
    })
    approved = decision if isinstance(decision, bool) else str(decision).lower() in ("true", "yes", "1")
    return {"approved": approved, "status": "approved" if approved else "rejected"}


def publish_or_reject(state: ContentPipelineState) -> dict:
    if state.get("approved"):
        return {
            "published": f"✅ 已发布: {state['topic']}\n---\n{state['draft']}",
            "status": "published",
        }
    return {
        "published": f"❌ 未发布: {state['topic']} (人工拒绝)",
        "status": "rejected",
    }


def build_content_pipeline():
    g = StateGraph(ContentPipelineState)
    g.add_node("analyze", analyze_topic)
    g.add_node("write", write_draft)
    g.add_node("review", auto_review)
    g.add_node("approve", human_approval)
    g.add_node("publish", publish_or_reject)

    g.add_edge(START, "analyze")
    g.add_edge("analyze", "write")
    g.add_edge("write", "review")
    g.add_edge("review", "approve")
    g.add_edge("approve", "publish")
    g.add_edge("publish", END)
    return g


def demo_full_pipeline():
    print("\n=== 综合验收: 内容生产流水线 ===")
    checkpointer = MemorySaver()
    app = build_content_pipeline().compile(checkpointer=checkpointer)
    config = {"configurable": {"thread_id": "final-demo-1"}}

    initial = {
        "topic": "LangGraph 入门",
        "outline": "",
        "draft": "",
        "review_notes": "",
        "approved": None,
        "published": "",
        "status": "init",
    }

    print("  [streaming updates]")
    for chunk in app.stream(initial, config=config, stream_mode="updates"):
        node = list(chunk.keys())[0]
        update = chunk[node]
        print(f"    → {node}: status={update.get('status', '...')}")

    state = app.get_state(config)
    result = state.values
    if state.next:
        print("\n  流水线暂停，等待人工审批...")
        result = app.invoke(Command(resume=True), config=config)

    print(f"\n  最终状态: {result.get('status')}")
    print(f"  发布结果:\n{result.get('published', '')[:300]}")


def demo_checkpoint_recovery():
    print("\n=== 断点恢复演示 ===")
    db_path = os.path.join(tempfile.gettempdir(), "langgraph_stage2_final.db")

    from langgraph.checkpoint.sqlite import SqliteSaver

    with SqliteSaver.from_conn_string(db_path) as cp:
        app = build_content_pipeline().compile(checkpointer=cp)
        config = {"configurable": {"thread_id": "recovery-demo"}}

        app.invoke({
            "topic": "Checkpoint 机制",
            "outline": "", "draft": "", "review_notes": "",
            "approved": None, "published": "", "status": "init",
        }, config=config)

        saved = app.get_state(config)
        print(f"  中断点 next={saved.next}, status={saved.values.get('status')}")
        print(f"  draft 已生成: {bool(saved.values.get('draft'))}")


if __name__ == "__main__":
    print("=" * 60)
    print("10 - 阶段二综合验收")
    print("=" * 60)

    demo_full_pipeline()
    demo_checkpoint_recovery()

    print("\n验收清单:")
    print("✓ 5 节点工作流: analyze → write → review → approve → publish")
    print("✓ Human-in-the-Loop: approve 节点 interrupt + Command(resume)")
    print("✓ Checkpointing: MemorySaver / SqliteSaver")
    print("✓ Streaming: stream_mode='updates'")
