"""Webhook Gateway 教学版 - 模拟 IM 通道"""

import uuid
from datetime import datetime, timezone

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="OpenHarness Gateway Demo", version="0.1.0")

SESSIONS: dict[str, list[dict]] = {}


class WebhookMessage(BaseModel):
    user_id: str = Field(min_length=1)
    text: str = Field(min_length=1)
    channel: str = Field(default="internal-im")


class WebhookResponse(BaseModel):
    session_id: str
    reply_preview: str


def simulate_harness_stream(user_text: str) -> list[dict]:
    """模拟 stream-json 事件序列"""
    return [
        {"type": "message_start", "ts": datetime.now(timezone.utc).isoformat()},
        {"type": "content_block_delta", "delta": {"text": "收到: "}},
        {"type": "content_block_delta", "delta": {"text": user_text[:50]}},
        {"type": "message_stop"},
    ]


@app.get("/health")
def health():
    return {"status": "ok", "sessions": len(SESSIONS)}


@app.post("/webhook/im", response_model=WebhookResponse)
def webhook_im(msg: WebhookMessage):
    sid = str(uuid.uuid4())
    events = simulate_harness_stream(msg.text)
    SESSIONS[sid] = events
    preview = "".join(e.get("delta", {}).get("text", "") for e in events if e.get("type") == "content_block_delta")
    return WebhookResponse(session_id=sid, reply_preview=preview or "(empty)")


@app.get("/sessions/{session_id}/events")
def get_events(session_id: str):
    if session_id not in SESSIONS:
        raise HTTPException(404, "session not found")
    return {"session_id": session_id, "events": SESSIONS[session_id]}
