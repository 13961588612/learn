"""
04_mcp_config_validate.py - servers.json 校验

学习要点:
1. mcpServers 配置结构
2. dry-run 应能发现 command/args 错误
"""

import json
from pathlib import Path  # Path 面向对象的路径操作，跨平台


def validate_mcp_config(data: dict) -> list[str]:
    # -> list[str] 返回值注解：错误信息字符串列表
    errors: list[str] = []  # 空列表，后续 append 追加错误
    # .get("mcpServers", {}) 缺省返回空 dict，避免 KeyError
    servers = data.get("mcpServers", {})  # dict
    if not servers:  # 空 dict 在布尔上下文中为 False
        errors.append("mcpServers 为空")
    # .items() 遍历 dict 的 (键, 值) 对
    for name, cfg in servers.items():  # name: str；cfg: dict
        # in 检查键是否存在；not in cfg 等价于 "command" not in cfg.keys()
        if "command" not in cfg:
            errors.append(f"{name}: 缺少 command")  # f-string 嵌入变量
        # .get("args") 为空列表/None/缺失时均为 falsy
        if not cfg.get("args"):
            errors.append(f"{name}: args 为空")
    return errors


def main():
    print("=" * 50)
    print("04 - MCP Config Validate")
    print("=" * 50)

    # 嵌套 dict + list 模拟合法 MCP 配置
    good = {  # dict
        "mcpServers": {
            "company-tickets": {
                "command": "uv",                              # 启动命令
                "args": ["run", "python", "-m", "ticket_mcp"],  # 命令行参数列表
            },
        },
    }
    bad = {"mcpServers": {"broken": {}}}  # dict：缺少 command/args 的无效配置

    # [(label, cfg), ...] 列表包元组，for 解包为 label 与 cfg
    for label, cfg in [("valid", good), ("invalid", bad)]:  # label: str；cfg: dict
        errs = validate_mcp_config(cfg)  # list[str]
        # errs or 'OK'：空列表为 falsy，显示 'OK'；否则显示错误列表
        print(f"\n  {label}: {errs or 'OK'}")

    # Path(__file__) 当前脚本路径；.parent 上一级；/ 运算符拼接子路径
    example = Path(__file__).parent.parent / "showcase" / "03_mcp_readonly_server" / "config" / "servers.json.example"  # Path
    if example.exists():  # 文件存在才读取，避免 FileNotFoundError
        # read_text(encoding="utf-8") 读全文；json.loads 解析为 dict
        loaded = json.loads(example.read_text(encoding="utf-8"))  # dict
        print(f"\n  showcase 配置校验: {validate_mcp_config(loaded) or 'OK'}")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
