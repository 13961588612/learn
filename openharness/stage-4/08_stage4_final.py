"""
08_stage4_final.py - 综合：调研子 Agent + 汇总主 Agent

学习要点:
1. 多 Agent 分工模拟
2. Task + Compaction + 熔断
"""


def research_agent(topic: str) -> str:
    return f"调研结论({topic}): 市场增长 12%"


def summarize_agent(bullets: list[str]) -> str:
    return "汇总报告:\n" + "\n".join(f"- {b}" for b in bullets)


def main():
    print("=" * 50)
    print("08 - Stage 4 Final")
    print("=" * 50)

    topics = ["竞品 A", "竞品 B", "政策风险"]
    findings = [research_agent(t) for t in topics]
    report = summarize_agent(findings)

    print(f"\n{report}")
    print("\n[OK] 阶段四综合练习完成")


if __name__ == "__main__":
    main()
