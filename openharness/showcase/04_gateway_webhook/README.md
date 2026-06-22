# 04_gateway_webhook · Webhook 通道 + stream 模拟

对应 **P4–P5** · [`../../base/openharness/p4-gateway-backend`](../../base/openharness/p4-gateway-backend)

## 运行

```bash
cd openharness/showcase/04_gateway_webhook
uv run uvicorn app.main:app --reload
```

## 接口

- `POST /webhook/im` - 模拟 IM 消息入站
- `GET /health` - 健康检查
- `GET /sessions/{id}/events` - 查看模拟 stream 事件

## 说明

此为 **Gateway 契约教学版**：不连接真实 OpenHarness，用 FastAPI 模拟 channel → harness → stream 回传。
