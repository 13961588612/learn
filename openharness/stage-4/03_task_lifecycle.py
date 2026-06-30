"""
03_task_lifecycle.py - Task Create → Output → Stop

学习要点:
1. 后台 Task 异步执行
2. 主会话通过 Output 取结果
"""

from dataclasses import dataclass, field
from enum import Enum  # Enum 定义有限常量集合，成员可比较、可 .value 取字符串


class TaskStatus(str, Enum):
    # (str, Enum) 多重继承：成员值同时是 str，可直接与字符串比较
    PENDING = "pending"
    RUNNING = "running"
    DONE = "done"
    STOPPED = "stopped"


@dataclass
class Task:
    id: str
    prompt: str
    status: TaskStatus = TaskStatus.PENDING  # 枚举成员作为默认值
    output: str = ""  # 空字符串默认


@dataclass
class TaskManager:
    # dict[str, Task] 键为 task id，值为 Task 实例
    tasks: dict[str, Task] = field(default_factory=dict)
    _counter: int = 0  # 下划线前缀表示「内部用」计数器

    def create(self, prompt: str) -> Task:
        self._counter += 1  # 自增生成唯一 id
        tid = f"task-{self._counter}"  # str
        # 创建时直接设为 RUNNING，模拟后台立即启动
        t = Task(id=tid, prompt=prompt, status=TaskStatus.RUNNING)  # Task
        self.tasks[tid] = t  # dict 赋值注册 Task
        return t

    def complete(self, tid: str, output: str) -> None:
        # -> None 表示无返回值；通过修改 t 的属性更新状态
        t = self.tasks[tid]  # Task
        t.output = output
        t.status = TaskStatus.DONE

    def stop(self, tid: str) -> None:
        # 链式访问：先取 Task 再改 status
        self.tasks[tid].status = TaskStatus.STOPPED


def main():
    print("=" * 50)
    print("03 - Task Lifecycle")
    print("=" * 50)

    mgr = TaskManager()  # TaskManager
    t = mgr.create("汇总上周工单统计")  # Task
    mgr.complete(t.id, "共 42 单，P0: 2")
    # .status.value 取 Enum 底层字符串值
    print(f"  {t.id} status={t.status.value} output={t.output}")

    t2 = mgr.create("长时间扫描")  # Task
    mgr.stop(t2.id)  # 模拟用户或系统中止
    print(f"  {t2.id} status={t2.status.value}")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
