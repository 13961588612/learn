"""
07_httpx_async.py - httpx 异步客户端、重试、超时

学习要点:
1. httpx.AsyncClient 管理连接池，应用 async with 确保关闭
2. timeout 参数限制连接/读/写各阶段耗时
3. MockTransport 可在无网络时模拟 HTTP 响应（测试常用）
4. 简单重试：捕获异常后 sleep 再请求
"""

import asyncio
import json

import httpx


def build_mock_transport() -> httpx.MockTransport:
    """MockTransport：按 URL 返回预设响应，无需真实网络"""

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == "/users/1":
            body = {"id": 1, "name": "Alice", "email": "alice@example.com"}
            return httpx.Response(200, json=body)
        if request.url.path == "/health":
            return httpx.Response(200, json={"status": "ok"})
        return httpx.Response(404, json={"error": "not found"})

    return httpx.MockTransport(handler)


async def fetch_json(client: httpx.AsyncClient, path: str) -> dict:
    response = await client.get(path)
    response.raise_for_status()  # 4xx/5xx 抛 httpx.HTTPStatusError
    return response.json()


async def fetch_with_retry(
    client: httpx.AsyncClient,
    path: str,
    *,
    max_attempts: int = 3,
    backoff: float = 0.1,
) -> dict:
    last_error: Exception | None = None
    for attempt in range(1, max_attempts + 1):
        try:
            return await fetch_json(client, path)
        except httpx.HTTPError as e:
            last_error = e
            print(f"  第 {attempt} 次失败: {e}")
            if attempt < max_attempts:
                await asyncio.sleep(backoff * attempt)
    raise RuntimeError(f"重试耗尽: {last_error}")


async def main_async():
    print("=" * 50)
    print("07 - httpx Async")
    print("=" * 50)

    transport = build_mock_transport()
    # timeout=httpx.Timeout(5.0) 限制总超时；MockTransport 演示中可选
    async with httpx.AsyncClient(
        base_url="https://api.example.com",
        transport=transport,
        timeout=5.0,
    ) as client:
        print("\n=== GET /users/1 ===")
        user = await fetch_json(client, "/users/1")
        print(f"  user = {json.dumps(user, ensure_ascii=False)}")

        print("\n=== GET /health ===")
        health = await fetch_json(client, "/health")
        print(f"  health = {health}")

        print("\n=== 404 重试演示 ===")
        try:
            await fetch_with_retry(client, "/missing")
        except RuntimeError as e:
            print(f"  预期失败: {e}")

    print("\n提示: 生产环境可将 base_url 换为真实 API，去掉 MockTransport")
    print("\n[OK] 完成")


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
