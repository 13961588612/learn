"""
05_async_basics.py - async def、await、asyncio.gather

学习要点:
1. async def 定义协程函数，调用后返回 coroutine 对象（不会立刻执行）
2. await 挂起当前协程，等待异步操作完成
3. asyncio.gather 并发运行多个协程，等待全部完成
4. asyncio.run() 是脚本入口启动事件循环的标准方式
"""

import asyncio
import time


async def fetch_label(name: str, delay: float) -> str:
    # await asyncio.sleep 模拟 I/O 等待（不阻塞线程）
    await asyncio.sleep(delay)
    return f"{name}({delay}s)"


async def demo_sequential():
    print("\n=== 顺序 await ===")
    start = time.perf_counter()
    a = await fetch_label("A", 0.2)
    b = await fetch_label("B", 0.2)
    elapsed = time.perf_counter() - start
    print(f"  结果: {a}, {b}  耗时: {elapsed:.2f}s")


async def demo_gather():
    print("\n=== asyncio.gather 并发 ===")
    start = time.perf_counter()
    # gather 同时启动多个协程，总耗时约等于最慢的那个
    results = await asyncio.gather(
        fetch_label("A", 0.2),
        fetch_label("B", 0.2),
        fetch_label("C", 0.2),
    )
    elapsed = time.perf_counter() - start
    print(f"  结果: {results}")
    print(f"  耗时: {elapsed:.2f}s（约 0.2s 而非 0.6s）")


async def main_async():
    print("=" * 50)
    print("05 - Async Basics")
    print("=" * 50)
    await demo_sequential()
    await demo_gather()
    print("\n[OK] 完成")


def main():
    asyncio.run(main_async())  # 创建事件循环并运行顶层协程


if __name__ == "__main__":
    main()
