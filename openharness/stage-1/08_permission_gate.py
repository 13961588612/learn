"""
08_permission_gate.py - 工具调用前权限门禁

学习要点:
1. permissions 在 execute 之前拦截
2. path_rules、denied_commands 基线
"""

from dataclasses import dataclass       # @dataclass 自动生成 __init__
from pathlib import PurePosixPath       # 纯 POSIX 路径，不访问文件系统，适合跨平台规则匹配


# @dataclass 装饰器：为字段生成 __init__；默认值在类体中直接赋值
@dataclass
class PermissionConfig:
    """权限策略配置：模式、禁止命令、允许读取的路径前缀。"""
    mode: str = "default"  # default | auto | plan
    # tuple[str, ...]：固定长度可变元组类型；(...) 为元组字面量
    denied_commands: tuple[str, ...] = ("rm", "curl", "wget")
    allowed_read_paths: tuple[str, ...] = ("/project", "/tmp")


def check_bash(command: str, cfg: PermissionConfig) -> tuple[bool, str]:
    """
    检查 bash 命令首词是否在 denied_commands 中。
    -> tuple[bool, str]： (是否允许, 说明信息)。
    """
    # 三元表达式：条件为真取 split()[0]，否则空串
    first = command.strip().split()[0] if command.strip() else ""
    if first in cfg.denied_commands:  # in 成员检测
        return False, f"denied_commands 禁止: {first}"
    return True, "allowed"


def check_read_path(path: str, cfg: PermissionConfig) -> tuple[bool, str]:
    """检查读取路径是否以 allowed_read_paths 中某前缀开头。"""
    p = PurePosixPath(path)  # 构造纯路径对象，统一斜杠语义
    for prefix in cfg.allowed_read_paths:
        if str(p).startswith(prefix):  # startswith 前缀匹配
            return True, "allowed"
    return False, f"path_rules 拒绝: {path}"


def main():
    print("=" * 50)
    print("08 - Permission Gate")
    print("=" * 50)
    cfg = PermissionConfig()  # 使用 dataclass 默认值实例化

    # (kind, arg) 元组列表：kind 区分 bash / read 检查
    tests = [
        ("bash", "ls -la"),
        ("bash", "rm -rf /"),
        ("read", "/project/README.md"),
        ("read", "/etc/passwd"),
    ]

    for kind, arg in tests:
        if kind == "bash":
            ok, msg = check_bash(arg, cfg)  # 元组解包
        else:
            ok, msg = check_read_path(arg, cfg)
        status = "ALLOW" if ok else "DENY"  # 三元表达式选字符串
        print(f"  [{status}] {kind} {arg!r} -> {msg}")  # !r 用 repr 显示引号

    print("\n[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
