"""
最小 MCP 风格只读工单 Server（教学用 stdio JSON-RPC 模拟）

生产环境建议使用官方 MCP SDK；此处保持零额外依赖、可读性优先。
"""

import json
import sys
from typing import Any

TICKETS = {
    "T-100": {"title": "登录超时", "status": "open"},
    "T-101": {"title": "支付回调延迟", "status": "closed"},
    "T-102": {"title": "报表导出失败", "status": "open"},
}


def tools_list() -> dict:
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
        kw = arguments.get("keyword", "").lower()
        hits = [f"{tid}: {t['title']} ({t['status']})" for tid, t in TICKETS.items() if kw in t["title"].lower()]
        text = "\n".join(hits) if hits else "no matches"
    elif name == "get_ticket":
        tid = arguments.get("id", "")
        t = TICKETS.get(tid)
        text = json.dumps(t, ensure_ascii=False) if t else f"ERROR: unknown {tid}"
    else:
        text = f"ERROR: unknown tool {name}"
    return {"content": [{"type": "text", "text": text}]}


def handle(line: str) -> dict:
    req = json.loads(line)
    method = req.get("method")
    rid = req.get("id")
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": rid, "result": tools_list()}
    if method == "tools/call":
        params = req.get("params", {})
        result = tools_call(params.get("name", ""), params.get("arguments", {}))
        return {"jsonrpc": "2.0", "id": rid, "result": result}
    return {"jsonrpc": "2.0", "id": rid, "error": {"code": -32601, "message": "not found"}}


def demo_stdio():
    """演示一次 list + call（非长期 stdio 服务）"""
    for raw in (
        {"jsonrpc": "2.0", "id": 1, "method": "tools/list"},
        {"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "get_ticket", "arguments": {"id": "T-100"}}},
    ):
        resp = handle(json.dumps(raw))
        print(json.dumps(resp, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--stdio":
        for line in sys.stdin:
            line = line.strip()
            if line:
                sys.stdout.write(json.dumps(handle(line)) + "\n")
                sys.stdout.flush()
    else:
        demo_stdio()
