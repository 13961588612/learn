"""04_middleware_audit_sim.py - Middleware 审计概念"""

from dataclasses import dataclass, field


@dataclass
class AuditLog:
    entries: list[str] = field(default_factory=list)

    def record(self, agent: str, tool: str) -> None:
        self.entries.append(f"{agent}:{tool}")


def simulate_on_acting(audit: AuditLog, agent: str, tool: str, execute) -> str:
    result = execute()
    audit.record(agent, tool)
    return result


def main():
    print("=" * 50)
    print("04 - Middleware Audit Sim")
    print("=" * 50)
    log = AuditLog()
    out = simulate_on_acting(log, "ops", "search_docs", lambda: "ok")
    print(f"  result={out} audit={log.entries}")
    print("\n  实现见 _shared/audit_middleware.py 与 showcase/01")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
