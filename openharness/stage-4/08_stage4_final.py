"""
08_stage4_final.py - 综合：调研子 Agent + 汇总主 Agent

学习要点:
1. 多 Agent 分工模拟
2. Task + Compaction + 熔断
"""


def research_agent(topic: str) -> str:
    # 模拟子 Agent：接收主题，返回固定格式结论字符串
    return f"调研结论({topic}): 市场增长 12%"


def summarize_agent(bullets: list[str]) -> str:
    # 列表推导 + join：每个 bullet 前加 "- "，再用换行连接
    return "汇总报告:\n" + "\n".join(f"- {b}" for b in bullets)


def main():
    print("=" * 50)
    print("08 - Stage 4 Final")
    print("=" * 50)

    topics = ["竞品 A", "竞品 B", "政策风险"]  # list[str]
    # 列表推导：对每个 topic 调用 research_agent，得到 findings 列表
    findings = [research_agent(t) for t in topics]  # list[str]
    report = summarize_agent(findings)  # str

    print(f"\n{report}")  # f-string 可嵌入多行字符串
    print("\n[OK] 阶段四综合练习完成")


if __name__ == "__main__":
    main()
