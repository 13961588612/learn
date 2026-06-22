"""
08_permission_gate.py - 工具调用前权限门禁

学习要点:
1. permissions 在 execute 之前拦截
2. path_rules、denied_commands 基线
"""

from dataclasses import dataclass
from pathlib import PurePosixPath


@dataclass
class PermissionConfig:
    mode: str = "default"  # default | auto | plan
    denied_commands: tuple[str, ...] = ("rm", "curl", "wget")
    allowed_read_paths: tuple[str, ...] = ("/project", "/tmp")


def check_bash(command: str, cfg: PermissionConfig) -> tuple[bool, str]:
    first = command.strip().split()[0] if command.strip() else ""
    if first in cfg.denied_commands:
        return False, f"denied_commands 禁止: {first}"
    return True, "allowed"


def check_read_path(path: str, cfg: PermissionConfig) -> tuple[bool, str]:
    p = PurePosixPath(path)
    for prefix in cfg.allowed_read_paths:
        if str(p).startswith(prefix):
            return True, "allowed"
    return False, f"path_rules 拒绝: {path}"


def main():
    print("=" * 50)
    print("08 - Permission Gate")
    print("=" * 50)
    cfg = PermissionConfig()

    tests = [
        ("bash", "ls -la"),
        ("bash", "rm -rf /"),
        ("read", "/project/README.md"),
        ("read", "/etc/passwd"),
    ]

    for kind, arg in tests:
        if kind == "bash":
            ok, msg = check_bash(arg, cfg)
        else:
            ok, msg = check_read_path(arg, cfg)
        status = "ALLOW" if ok else "DENY"
        print(f"  [{status}] {kind} {arg!r} -> {msg}")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
