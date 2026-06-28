"""
最小 MCP 风格只读工单 Server（教学用 stdio JSON-RPC 模拟）

生产环境建议使用官方 MCP SDK；此处保持零额外依赖、可读性优先。
"""

import json       # loads/dumps JSON-RPC 消息
import sys        # stdin/stdout 与 argv
from typing import Any  # Any 表示任意类型（本文件 dict 值未细粒度标注）

# dict：工单 ID -> {title, status}
TICKETS = {
    "T-100": {"title": "登录超时", "status": "open"},
    "T-101": {"title": "支付回调延迟", "status": "closed"},
    "T-102": {"title": "报表导出失败", "status": "open"},
}


def tools_list() -> dict:
    # 返回 MCP tools/list 风格的工具描述（JSON Schema inputSchema）
    return {
        "tools": [
            {
                "name": "search_tickets",
                "description": "Search tickets by keyword (read-only)",
                "inputSchema": {
                    "type": "object",
                    "properties": {"keyword": {"type": "string"}},
                    "required": ["keyword"],
                },
            },
            {
                "name": "get_ticket",
                "description": "Get ticket by id (read-only)",
                "inputSchema": {
                    "type": "object",
                    "properties": {"id": {"type": "string"}},
                    "required": ["id"],
                },
            },
        ],
    }


def tools_call(name: str, arguments: dict) -> dict:
    if name == "search_tickets":
        kw = arguments.get("keyword", "").lower()  # get 带默认值，避免 KeyError
        # 列表推导：标题含 kw 的工单格式化为字符串
        hits = [f"{tid}: {t['title']} ({t['status']})" for tid, t in TICKETS.items() if kw in t["title"].lower()]
        text = "\n".join(hits) if hits else "no matches"  # 三元表达式
    elif name == "get_ticket":
        tid = arguments.get("id", "")
        t = TICKETS.get(tid)  # 不存在则 t 为 None
        text = json.dumps(t, ensure_ascii=False) if t else f"ERROR: unknown {tid}"
    else:
        text = f"ERROR: unknown tool {name}"
    # MCP 工具结果：content 数组，每项 type=text
    return {"content": [{"type": "text", "text": text}]}


def handle(line: str) -> dict:
    req = json.loads(line)  # 解析单行 JSON-RPC 请求
    method = req.get("method")
    rid = req.get("id")  # 请求 id，响应需原样回传
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": rid, "result": tools_list()}
    if method == "tools/call":
        params = req.get("params", {})  # 缺省 params 时用空 dict
        result = tools_call(params.get("name", ""), params.get("arguments", {}))
        return {"jsonrpc": "2.0", "id": rid, "result": result}
    # JSON-RPC 标准错误码 -32601 Method not found
    return {"jsonrpc": "2.0", "id": rid, "error": {"code": -32601, "message": "not found"}}


def demo_stdio():
    """演示一次 list + call（非长期 stdio 服务）"""
    # for raw in (...): 遍历固定演示请求（元组内为 dict）
    for raw in (
        {"jsonrpc": "2.0", "id": 1, "method": "tools/list"},
        {"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "get_ticket", "arguments": {"id": "T-100"}}},
    ):
        resp = handle(json.dumps(raw))  # 先 dumps 成字符串再 handle（模拟 stdin 一行）
        print(json.dumps(resp, ensure_ascii=False, indent=2))  # indent=2 美化输出


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    # len(sys.argv) > 1 且 argv[1]=="--stdio" 时进入长期 stdio 服务模式
    if len(sys.argv) > 1 and sys.argv[1] == "--stdio":
        for line in sys.stdin:  # 阻塞读 stdin 每一行
            line = line.strip()
            if line:
                sys.stdout.write(json.dumps(handle(line)) + "\n")  # 写一行响应
                sys.stdout.flush()  # 立即刷新，便于对端读取
    else:
        demo_stdio()  # 无 --stdio 则跑本地演示
