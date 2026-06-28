"""
01_typing_basics.py - Optional、Union、类型别名、mypy 概念

学习要点:
1. 类型注解帮助 IDE 与静态检查器（mypy）发现错误
2. Python 3.10+ 用 X | Y 代替 Union[X, Y]
3. Optional[X] 等价于 X | None
4. 类型别名用 TypeAlias 或简单赋值（3.12+ 推荐 TypeAliasType）
"""

from typing import Optional, TypeAlias, Union

# 类型别名：给复杂类型起短名，便于复用
UserId: TypeAlias = int
JsonDict: TypeAlias = dict[str, object]


def find_user(user_id: UserId) -> Optional[str]:
    # Optional[str] 等价于 str | None：可能返回值，也可能没有
    db = {1: "Alice", 2: "Bob"}
    return db.get(user_id)


def parse_score(raw: Union[int, str]) -> float:
    # Union[int, str]：参数可以是 int 或 str（3.10+ 可写 int | str）
    if isinstance(raw, int):
        return float(raw)
    return float(raw.strip())


def build_greeting(name: str, title: str | None = None) -> str:
    # str | None 是 Optional[str] 的现代写法
    if title:
        return f"{title} {name}"
    return f"Hello, {name}"


def demo_mypy_concept() -> None:
    """
    mypy 是静态类型检查器，运行: uv run mypy python/stage-3/01_typing_basics.py
    本脚本故意展示「合法注解」；错误示例见注释：
      # reveal_type(find_user(1))  # mypy 插件可推断 Optional[str]
      # x: int = "wrong"           # mypy 会报错：类型不兼容
    """
    user = find_user(1)
    if user is not None:  # 缩窄（narrowing）：None 检查后可当 str 用
        print(f"  找到用户: {user}")


def main():
    print("=" * 50)
    print("01 - Typing Basics")
    print("=" * 50)

    print(f"\nfind_user(1) = {find_user(1)!r}")
    print(f"find_user(99) = {find_user(99)!r}")
    print(f"parse_score('87.5') = {parse_score('87.5')}")
    print(f"build_greeting('Carol', 'Dr.') = {build_greeting('Carol', 'Dr.')}")

    print("\n=== mypy 概念 ===")
    demo_mypy_concept()
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
