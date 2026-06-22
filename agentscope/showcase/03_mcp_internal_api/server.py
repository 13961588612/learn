"""只读工单 MCP demo server（stdio）"""

TICKETS = {
    "TK-001": {"title": "登录慢", "status": "open"},
    "TK-002": {"title": "发布失败", "status": "closed"},
}


def search_tickets(status: str = "open") -> str:
    """按状态搜索工单（只读）"""
    hits = [f"{k}: {v['title']}" for k, v in TICKETS.items() if v["status"] == status]
    return "\n".join(hits) or "ERROR: 无工单"


def get_ticket(ticket_id: str) -> str:
    """获取单个工单"""
    t = TICKETS.get(ticket_id)
    if not t:
        return f"ERROR: 不存在 {ticket_id}"
    return f"{ticket_id} {t['title']} ({t['status']})"


def main():
    print("=" * 50)
    print("MCP Demo Tools (offline)")
    print("=" * 50)
    print(search_tickets("open"))
    print(get_ticket("TK-001"))
    print("\n  AgentScope MCP: Toolkit(mcps=[MCPClient(...)])")
    print("  见 stage-5 + 官方 MCP 文档")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
