"""
03_task_lifecycle.py - Task Create → Output → Stop

学习要点:
1. 后台 Task 异步执行
2. 主会话通过 Output 取结果
"""

from dataclasses import dataclass, field
from enum import Enum


class TaskStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    DONE = "done"
    STOPPED = "stopped"


@dataclass
class Task:
    id: str
    prompt: str
    status: TaskStatus = TaskStatus.PENDING
    output: str = ""


@dataclass
class TaskManager:
    tasks: dict[str, Task] = field(default_factory=dict)
    _counter: int = 0

    def create(self, prompt: str) -> Task:
        self._counter += 1
        tid = f"task-{self._counter}"
        t = Task(id=tid, prompt=prompt, status=TaskStatus.RUNNING)
        self.tasks[tid] = t
        return t

    def complete(self, tid: str, output: str) -> None:
        t = self.tasks[tid]
        t.output = output
        t.status = TaskStatus.DONE

    def stop(self, tid: str) -> None:
        self.tasks[tid].status = TaskStatus.STOPPED


def main():
    print("=" * 50)
    print("03 - Task Lifecycle")
    print("=" * 50)

    mgr = TaskManager()
    t = mgr.create("汇总上周工单统计")
    mgr.complete(t.id, "共 42 单，P0: 2")
    print(f"  {t.id} status={t.status.value} output={t.output}")

    t2 = mgr.create("长时间扫描")
    mgr.stop(t2.id)
    print(f"  {t2.id} status={t2.status.value}")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
