"""
03_mcp_mock_server.py - 模拟 MCP JSON-RPC 请求/响应

学习要点:
1. tools/list 与 tools/call 消息形状
2. 不依赖真实 MCP 进程即可理解协议
"""

import json
from typing import Any


def handle_request(req: dict[str, Any]) -> dict[str, Any]:
    method = req.get("method")
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [{
                    "name": "get_ticket",
                    "description": "Get ticket by id",
                    "inputSchema": {"type": "object", "properties": {"id": {"type": "string"}}},
                }],
            },
        }

    if method == "tools/call":
        ticket_id = req.get("params", {}).get("arguments", {}).get("id")
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {"content": [{"type": "text", "text": f"Ticket {ticket_id}: open"}]},
        }

    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}


def main():
    print("=" * 50)
    print("03 - MCP Mock Server")
    print("=" * 50)

    list_req = {"jsonrpc": "2.0", "id": 1, "method": "tools/list"}
    call_req = {"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "get_ticket", "arguments": {"id": "T-100"}}}

    for req in (list_req, call_req):
        resp = handle_request(req)
        print(f"\n  {req['method']} -> {json.dumps(resp, ensure_ascii=False)[:120]}...")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
