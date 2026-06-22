"""OpenHarness CLI 工具 — 各 stage lab 脚本共用"""

from __future__ import annotations

import json
import shutil
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

# learn/openharness/ — lab 脚本 sys.path 应指向此目录
OH_ROOT = Path(__file__).resolve().parent.parent


@dataclass
class CliResult:
    command: list[str]
    returncode: int
    stdout: str
    stderr: str
    ok: bool


def find_cli() -> list[str] | None:
    for cmd in ("openh", "oh"):
        if shutil.which(cmd):
            return [cmd]
    return None


def run_cli(args: list[str], timeout: int = 120) -> CliResult:
    cli = find_cli()
    if not cli:
        return CliResult(args, 127, "", "CLI not found: install openharness-ai", False)
    cmd = cli + args
    try:
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return CliResult(cmd, proc.returncode, proc.stdout or "", proc.stderr or "", proc.returncode == 0)
    except subprocess.TimeoutExpired:
        return CliResult(cmd, -1, "", "timeout", False)
    except FileNotFoundError:
        return CliResult(cmd, 127, "", "command not found", False)


def save_experiment(lab_dir: Path, name: str, result: CliResult, notes: str = "") -> Path:
    out_dir = lab_dir / "experiments"
    out_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    path = out_dir / f"{name}_{ts}.json"
    payload = {
        "timestamp": ts,
        "command": result.command,
        "returncode": result.returncode,
        "stdout": result.stdout[:8000],
        "stderr": result.stderr[:4000],
        "notes": notes,
    }
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def require_cli_or_guide(step: str) -> bool:
    if find_cli():
        return True
    print(f"  [跳过] {step}")
    print("  安装: uv sync --group openharness-cli")
    print("  或:   pip install openharness-ai")
    print("  Windows 使用 openh，Unix 可用 oh")
    return False


def print_result_summary(result: CliResult, max_lines: int = 25) -> None:
    print(f"  命令: {' '.join(result.command)}")
    print(f"  exit: {result.returncode}")
    combined = (result.stdout + result.stderr).strip()
    if not combined:
        print("  (无输出)")
        return
    lines = combined.splitlines()
    for line in lines[:max_lines]:
        print(f"  | {line}")
    if len(lines) > max_lines:
        print(f"  | ... ({len(lines) - max_lines} more lines)")
