"""Webhook Gateway 教学版 - 模拟 IM 通道"""

import uuid                              # uuid4() 生成随机 session_id
from datetime import datetime, timezone  # timezone.utc 表示 UTC 时区

from fastapi import FastAPI, HTTPException  # FastAPI 应用；HTTPException 返回 HTTP 错误
from pydantic import BaseModel, Field      # 请求/响应体校验

# 创建 FastAPI 实例；title/version 出现在 OpenAPI 文档
app = FastAPI(title="OpenHarness Gateway Demo", version="0.1.0")

# 模块级 dict：session_id -> stream 事件列表；dict[str, list[dict]] 类型注解
SESSIONS: dict[str, list[dict]] = {}


# 继承 BaseModel：POST body 自动解析并校验
class WebhookMessage(BaseModel):
    user_id: str = Field(min_length=1)
    text: str = Field(min_length=1)
    channel: str = Field(default="internal-im")  # 可选字段默认值


class WebhookResponse(BaseModel):
    session_id: str
    reply_preview: str


def simulate_harness_stream(user_text: str) -> list[dict]:
    """模拟 stream-json 事件序列"""
    return [
        {"type": "message_start", "ts": datetime.now(timezone.utc).isoformat()},
        {"type": "content_block_delta", "delta": {"text": "收到: "}},
        {"type": "content_block_delta", "delta": {"text": user_text[:50]}},  # [:50] 截断
        {"type": "message_stop"},
    ]


# @app.get 注册 GET 路由；函数名 health 即 operation_id
@app.get("/health")
def health():
    return {"status": "ok", "sessions": len(SESSIONS)}  # len(dict) 为键数量


# response_model 指定响应体 schema；msg 由 FastAPI 从 JSON body 注入
@app.post("/webhook/im", response_model=WebhookResponse)
def webhook_im(msg: WebhookMessage):
    sid = str(uuid.uuid4())  # UUID 转字符串作为 session_id
    events = simulate_harness_stream(msg.text)
    SESSIONS[sid] = events  # 存入内存会话表
    # 生成器表达式：从 delta 事件拼接 text 字段
    preview = "".join(e.get("delta", {}).get("text", "") for e in events if e.get("type") == "content_block_delta")
    # preview or "(empty)"：空字符串时用占位符
    return WebhookResponse(session_id=sid, reply_preview=preview or "(empty)")


# {session_id} 路径参数注入同名函数参数
@app.get("/sessions/{session_id}/events")
def get_events(session_id: str):
    if session_id not in SESSIONS:
        raise HTTPException(404, "session not found")  # 404 状态码
    return {"session_id": session_id, "events": SESSIONS[session_id]}
