"""Stage 7 final - capstone checklist"""

CHECKLIST = [
    "showcase/04 启动 Bridge",
    "curl POST /v1/sessions/s1/messages",
    "IntentGate AgentScopeBackend 指向 base_url",
    "端到端 card action（可选）",
]


def main():
    print("=" * 50)
    print("Stage 7 Final")
    print("=" * 50)
    for i, item in enumerate(CHECKLIST, 1):
        print(f"  [ ] {i}. {item}")
    print("\n[OK] stage-7 final")
if __name__ == "__main__":
    main()
