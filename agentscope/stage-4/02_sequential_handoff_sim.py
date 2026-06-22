"""02_sequential_handoff_sim.py - 顺序 handoff 模拟"""


def pipeline(agents: list[str], task: str) -> list[str]:
    trace = []
    msg = task
    for name in agents:
        out = f"[{name}] processed: {msg[:30]}"
        trace.append(out)
        msg = out
    return trace


def main():
    print("=" * 50)
    print("02 - Sequential Handoff Sim")
    print("=" * 50)
    for line in pipeline(["researcher", "writer"], "调研 AgentScope 并摘要"):
        print(f"  {line}")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
