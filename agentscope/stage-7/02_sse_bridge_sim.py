"""02_sse_bridge_sim.py - SSE 行格式模拟"""

def sse_lines(payload: str) -> list[str]:
    return [f"data: {payload}", ""]


def main():
    print("=" * 50)
    print("02 - SSE Bridge Sim")
    print("=" * 50)
    for line in sse_lines('{"type":"text","content":"hello"}'):
        print(f"  | {line!r}")
    print("\n[OK] 完成")
if __name__ == "__main__":
    main()
