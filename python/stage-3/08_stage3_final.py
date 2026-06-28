"""
08_stage3_final.py - 综合：并发拉取多个 API → Pydantic 校验 → 汇总报告

学习要点:
1. 组合 asyncio.gather + httpx.AsyncClient 并发请求
2. MockTransport 读取本地 JSON 模拟多 API（离线可运行）
3. Pydantic 模型统一校验各 API 响应
4. 汇总结果写入 data/report.json
"""

import asyncio
import json
from pathlib import Path

import httpx
from pydantic import BaseModel, Field


class ScoreRecord(BaseModel):
    user_id: int
    name: str
    score: float = Field(ge=0, le=100)


class ActivityRecord(BaseModel):
    user_id: int
    post_count: int = Field(ge=0)
    last_active: str


class UserSummary(BaseModel):
    user_id: int
    name: str
    score: float
    post_count: int
    last_active: str


class Stage3Report(BaseModel):
    users: list[UserSummary]
    average_score: float
    total_posts: int


def build_mock_transport(data_dir: Path) -> httpx.MockTransport:
    """按路径返回 data/ 下对应 JSON 文件内容"""

    def handler(request: httpx.Request) -> httpx.Response:
        mapping = {
            "/api/scores": data_dir / "api_scores.json",
            "/api/activity": data_dir / "api_activity.json",
        }
        file_path = mapping.get(request.url.path)
        if file_path is None or not file_path.exists():
            return httpx.Response(404, json={"error": "not found"})
        payload = json.loads(file_path.read_text(encoding="utf-8"))
        return httpx.Response(200, json=payload)

    return httpx.MockTransport(handler)


async def fetch_scores(client: httpx.AsyncClient) -> list[ScoreRecord]:
    response = await client.get("/api/scores")
    response.raise_for_status()
    return [ScoreRecord.model_validate(item) for item in response.json()]


async def fetch_activity(client: httpx.AsyncClient) -> list[ActivityRecord]:
    response = await client.get("/api/activity")
    response.raise_for_status()
    return [ActivityRecord.model_validate(item) for item in response.json()]


def merge_records(
    scores: list[ScoreRecord],
    activities: list[ActivityRecord],
) -> Stage3Report:
    activity_map = {a.user_id: a for a in activities}
    summaries: list[UserSummary] = []

    for s in scores:
        act = activity_map.get(s.user_id)
        if act is None:
            continue
        summaries.append(
            UserSummary(
                user_id=s.user_id,
                name=s.name,
                score=s.score,
                post_count=act.post_count,
                last_active=act.last_active,
            )
        )

    avg = sum(u.score for u in summaries) / len(summaries) if summaries else 0.0
    total_posts = sum(u.post_count for u in summaries)

    return Stage3Report(
        users=summaries,
        average_score=round(avg, 2),
        total_posts=total_posts,
    )


async def build_report(data_dir: Path) -> Stage3Report:
    transport = build_mock_transport(data_dir)
    async with httpx.AsyncClient(
        base_url="https://mock.local",
        transport=transport,
        timeout=10.0,
    ) as client:
        # gather 并发拉取两个「API」
        scores, activities = await asyncio.gather(
            fetch_scores(client),
            fetch_activity(client),
        )
    return merge_records(scores, activities)


async def main_async():
    print("=" * 50)
    print("08 - Stage 3 Final")
    print("=" * 50)

    base = Path(__file__).parent
    data_dir = base / "data"
    report_path = data_dir / "report.json"

    report = await build_report(data_dir)

    report_path.write_text(
        report.model_dump_json(indent=2),
        encoding="utf-8",
    )

    print("\n用户汇总:")
    for u in report.users:
        print(f"  [{u.user_id}] {u.name}: score={u.score}, posts={u.post_count}")

    print(f"\n平均分: {report.average_score}")
    print(f"总发帖: {report.total_posts}")
    print(f"\n报告已写入: {report_path}")
    print("\n[OK] 阶段三综合练习完成")


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
