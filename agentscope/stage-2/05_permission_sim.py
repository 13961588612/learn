"""05_permission_sim.py - Permission 决策模拟"""

from dataclasses import dataclass


@dataclass
class PermissionDecision:
    allowed: bool
    reason: str


SENSITIVE = (".env", "/etc", ".ssh")


def check_write_path(path: str) -> PermissionDecision:
    for s in SENSITIVE:
        if s in path:
            return PermissionDecision(False, f"blocked path {path}")
    return PermissionDecision(True, "ok")


def main():
    print("=" * 50)
    print("05 - Permission Sim")
    print("=" * 50)
    for p in ("README.md", ".env", "/etc/hosts"):
        d = check_write_path(p)
        print(f"  {p}: allowed={d.allowed} ({d.reason})")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
