"""OpenHarness CLI 工具 — 各 stage lab 脚本共用"""

from __future__ import annotations  # 推迟注解求值，允许前向引用与 PEP 604 写法

import json              # dumps 序列化实验记录为 JSON
import shutil            # which() 在 PATH 中查找 openh/oh 可执行文件
import subprocess        # run() 同步执行 CLI 子进程
from dataclasses import dataclass  # @dataclass 定义 CLI 执行结果数据结构
from datetime import datetime, timezone  # 生成 UTC 时间戳文件名
from pathlib import Path  # 跨平台路径操作

# learn/openharness/ — lab 脚本 sys.path 应指向此目录
# Path(__file__).resolve().parent.parent：_shared/cli.py -> _shared -> openharness
OH_ROOT = Path(__file__).resolve().parent.parent


# @dataclass 装饰器：自动生成 __init__、__repr__ 等
@dataclass
class CliResult:
    """一次 CLI 调用的完整结果。"""
    command: list[str]   # 实际执行的命令 argv 列表
    returncode: int        # 进程退出码，0 通常表示成功
    stdout: str
    stderr: str
    ok: bool               # 是否成功（returncode == 0）


def find_cli() -> list[str] | None:
    """
    在 PATH 中查找 openh（Windows）或 oh（Unix）命令。
    -> list[str] | None：找到返回 [cmd]，否则 None。
    """
    for cmd in ("openh", "oh"):
        if shutil.which(cmd):
            return [cmd]
    return None


def run_cli(args: list[str], timeout: int = 120) -> CliResult:
    """
    执行 openh/oh + args，捕获输出并封装为 CliResult。
    timeout: int = 120 默认超时秒数。
    """
    cli = find_cli()
    if not cli:
        return CliResult(args, 127, "", "CLI not found: install openharness-ai", False)
    cmd = cli + args  # 列表拼接：["openh"] + ["--dry-run"]
    try:
        # capture_output=True 捕获 stdout/stderr；text=True 返回 str
        proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return CliResult(
            cmd,
            proc.returncode,
            proc.stdout or "",   # or "" 防止 None
            proc.stderr or "",
            proc.returncode == 0,
        )
    except subprocess.TimeoutExpired:
        return CliResult(cmd, -1, "", "timeout", False)
    except FileNotFoundError:
        return CliResult(cmd, 127, "", "command not found", False)


def save_experiment(lab_dir: Path, name: str, result: CliResult, notes: str = "") -> Path:
    """
    将 CLI 结果写入 lab/experiments/{name}_{timestamp}.json。
    -> Path 返回写入文件的完整路径。
    """
    out_dir = lab_dir / "experiments"
    out_dir.mkdir(parents=True, exist_ok=True)  # 递归创建，已存在不报错
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")  # UTC ISO 风格时间戳
    path = out_dir / f"{name}_{ts}.json"
    payload = {
        "timestamp": ts,
        "command": result.command,
        "returncode": result.returncode,
        "stdout": result.stdout[:8000],   # 切片限制体积，避免 JSON 过大
        "stderr": result.stderr[:4000],
        "notes": notes,
    }
    # ensure_ascii=False 保留中文；indent=2 美化；encoding 指定 UTF-8
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    return path


def require_cli_or_guide(step: str) -> bool:
    """
    若 CLI 未安装则打印跳过提示与安装指引。
    -> bool：True 表示可继续，False 表示应跳过 lab 步骤。
    """
    if find_cli():
        return True
    print(f"  [跳过] {step}")
    print("  安装: uv sync --group openharness-cli")
    print("  或:   pip install openharness-ai")
    print("  Windows 使用 openh，Unix 可用 oh")
    return False


def print_result_summary(result: CliResult, max_lines: int = 25) -> None:
    """
    打印命令、退出码与输出摘要（最多 max_lines 行）。
    max_lines: int = 25 为默认参数。
    """
    print(f"  命令: {' '.join(result.command)}")
    print(f"  exit: {result.returncode}")
    combined = (result.stdout + result.stderr).strip()
    if not combined:
        print("  (无输出)")
        return
    lines = combined.splitlines()  # 按行拆分，不含换行符
    for line in lines[:max_lines]:
        print(f"  | {line}")
    if len(lines) > max_lines:
        print(f"  | ... ({len(lines) - max_lines} more lines)")
