"""
03_mcp_mock_server.py - 模拟 MCP JSON-RPC 请求/响应

学习要点:
1. tools/list 与 tools/call 消息形状
2. 不依赖真实 MCP 进程即可理解协议
"""

import json                          # dumps() 将 dict 序列化为 JSON 字符串
from typing import Any               # Any=任意类型，用于 JSON 动态结构


def handle_request(req: dict[str, Any]) -> dict[str, Any]:
    # dict[str, Any] 表示键为 str、值为任意类型的字典
    # .get("method") 安全取值，键不存在时返回 None
    method = req.get("method")  # str | None
    req_id = req.get("id")  # str | int | None：JSON-RPC 请求 id，响应需原样回传

    if method == "tools/list":
        # return 字典字面量即 JSON-RPC 2.0 成功响应
        return {
            "jsonrpc": "2.0",       # 协议版本固定为 2.0
            "id": req_id,           # 与请求 id 对应
            "result": {             # 成功时放 result，失败时放 error
                "tools": [{         # 列表 [] 包一层，内含单个 tool 描述
                    "name": "get_ticket",
                    "description": "Get ticket by id",
                    # 内嵌 JSON Schema：object 类型 + properties 定义字段
                    "inputSchema": {"type": "object", "properties": {"id": {"type": "string"}}},
                }],
            },
        }

    if method == "tools/call":
        # 链式 .get() 逐层安全访问嵌套 dict，任一层缺失返回 None
        ticket_id = req.get("params", {}).get("arguments", {}).get("id")  # str | None
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            # content 为 MCP 标准内容块列表；type=text 表示纯文本
            "result": {"content": [{"type": "text", "text": f"Ticket {ticket_id}: open"}]},
        }

    # JSON-RPC 标准错误码 -32601 = Method not found
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}


def main():
    print("=" * 50)
    print("03 - MCP Mock Server")
    print("=" * 50)

    # 字典字面量模拟 JSON-RPC 请求；id 用于关联响应
    list_req = {"jsonrpc": "2.0", "id": 1, "method": "tools/list"}  # dict[str, Any]
    call_req = {"jsonrpc": "2.0", "id": 2, "method": "tools/call", "params": {"name": "get_ticket", "arguments": {"id": "T-100"}}}  # dict[str, Any]

    # (list_req, call_req) 元组可迭代；for req in ... 依次处理两个请求
    for req in (list_req, call_req):  # dict[str, Any]
        resp = handle_request(req)  # dict[str, Any]
        # json.dumps 序列化；ensure_ascii=False 保留中文；[:120] 切片截断显示
        print(f"\n  {req['method']} -> {json.dumps(resp, ensure_ascii=False)[:120]}...")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
