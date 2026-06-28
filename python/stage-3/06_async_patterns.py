"""
06_async_patterns.py - 超时、取消、TaskGroup、与线程对比

学习要点:
1. asyncio.wait_for / asyncio.timeout 限制协程执行时间
2. Task.cancel() 取消任务，需处理 CancelledError
3. TaskGroup（3.11+）结构化并发，子任务异常时自动取消兄弟任务
4. asyncio.to_thread 把阻塞函数放到线程池，避免卡住事件循环
"""

import asyncio
import time


async def slow_job(name: str, seconds: float) -> str:
    await asyncio.sleep(seconds)
    return f"{name} done"


async def demo_timeout():
    print("\n=== 超时 ===")
    try:
        # Python 3.11+ 推荐 async with asyncio.timeout
        async with asyncio.timeout(0.1):
            await slow_job("slow", 1.0)
    except TimeoutError:
        print("  捕获 TimeoutError：任务超过 0.1s")


async def demo_cancel():
    print("\n=== 取消任务 ===")
    task = asyncio.create_task(slow_job("cancel-me", 2.0))
    await asyncio.sleep(0.05)
    task.cancel()
    try:
        await task
    except asyncio.CancelledError:
        print("  任务已取消（CancelledError）")


async def demo_task_group():
    print("\n=== TaskGroup ===")
    start = time.perf_counter()
    async with asyncio.TaskGroup() as tg:
        # tg.create_task 创建子任务；退出 with 块时等待全部完成
        tg.create_task(slow_job("job-1", 0.15))
        tg.create_task(slow_job("job-2", 0.15))
    elapsed = time.perf_counter() - start
    print(f"  TaskGroup 全部完成，耗时 {elapsed:.2f}s")


def blocking_io() -> str:
    """模拟阻塞式 I/O（如老式 requests 同步调用）"""
    time.sleep(0.2)
    return "blocking result"


async def demo_to_thread():
    print("\n=== asyncio.to_thread vs 直接调用 ===")
    start = time.perf_counter()
    # to_thread 在线程池运行阻塞函数，不阻塞事件循环
    result = await asyncio.to_thread(blocking_io)
    elapsed = time.perf_counter() - start
    print(f"  to_thread 结果: {result!r}, 耗时 {elapsed:.2f}s")


async def main_async():
    print("=" * 50)
    print("06 - Async Patterns")
    print("=" * 50)
    await demo_timeout()
    await demo_cancel()
    await demo_task_group()
    await demo_to_thread()
    print("\n[OK] 完成")


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
