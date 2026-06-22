"""IntentGate 兼容 Bridge — SSE /v1/sessions/{id}/messages"""

from __future__ import annotations

import asyncio
import json
import sys
import uuid
from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from agentscope.message import UserMsg  # noqa: E402
from _shared.env import has_any_llm  # noqa: E402
from _shared.runtime import build_agent  # noqa: E402

app = FastAPI(title="AgentScope IntentGate Bridge")
_sessions: dict[str, list] = {}


class StandardMessage(BaseModel):
    session_id: str
    text: str = Field(default="")
    user_id: str = Field(default="demo")


class AgentReply(BaseModel):
    type: str = "text"
    content: str = ""


@app.get("/health")
def health():
    return {"status": "ok", "llm": has_any_llm()}


@app.post("/v1/sessions/{session_id}/messages")
async def post_message(session_id: str, body: StandardMessage):
    async def stream():
        if not has_any_llm():
            payload = AgentReply(content="[mock] 请配置 OPENAI_API_KEY").model_dump()
            yield f"data: {json.dumps(payload, ensure_ascii=False)}\n\n"
            return
        agent = build_agent(name="bridge", system_prompt="简短中文回答。")
        reply = await agent.reply(UserMsg("user", body.text or "hello"))
        text = reply.get_text_content() or ""
        payload = AgentReply(content=text).model_dump()
        yield f"data: {json.dumps(payload, ensure_ascii=False)}\n\n"

    return StreamingResponse(stream(), media_type="text/event-stream")


@app.post("/v1/sessions/{session_id}/actions")
async def post_action(session_id: str, body: dict):
    async def stream():
        payload = AgentReply(content=f"action ack: {body.get('action_id', 'n/a')}").model_dump()
        yield f"data: {json.dumps(payload, ensure_ascii=False)}\n\n"

    return StreamingResponse(stream(), media_type="text/event-stream")


def main():
    import uvicorn

    host = "127.0.0.1"
    port = 8090
    print(f"Bridge http://{host}:{port}/health")
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    main()
