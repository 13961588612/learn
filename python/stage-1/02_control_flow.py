"""
02_control_flow.py - if/for/while、match、布尔与真值

学习要点:
1. 缩进即代码块（无大括号）
2. for 遍历可迭代对象，while 条件循环
3. match/case 结构模式匹配（3.10+，类似 switch 增强版）
4. 三元表达式与短路逻辑
"""


def demo_if_elif():
    print("\n=== if / elif / else ===")
    score = 85
    # 缩进（通常 4 空格）定义代码块，无需 {}
    if score >= 90:
        grade = "A"
    elif score >= 80:  # else if 的 Python 写法
        grade = "B"
    else:
        grade = "C"
    print(f"score={score} -> grade={grade}")


def demo_for_while():
    print("\n=== for / while ===")
    total = 0
    # range(1, 6) 生成 1,2,3,4,5（左闭右开）
    for n in range(1, 6):
        total += n
    print(f"1..5 sum = {total}")

    count = 3
    while count > 0:  # 条件为真时反复执行
        print(f"countdown: {count}")
        count -= 1    # 等价于 count = count - 1


def demo_match():
    print("\n=== match / case ===")
    commands = ["start", "stop", "pause", "unknown"]

    for cmd in commands:
        # match/case：结构模式匹配（Python 3.10+）
        match cmd:
            case "start":
                action = "启动服务"
            case "stop" | "pause":  # | 表示多个模式或匹配
                action = "变更状态"
            case str(s) if s.startswith("debug"):  # 守卫条件 if
                action = f"调试模式: {s}"
            case _:  # _ 为通配符，匹配其余所有情况
                action = "未知命令"
        print(f"{cmd!r} -> {action}")


def demo_boolean_short_circuit():
    print("\n=== 布尔短路 ===")

    def expensive() -> bool:
        print("  (expensive 被调用)")
        return True

    # and：左侧为 False 时不求值右侧（短路）
    print("False and expensive:", False and expensive())
    # or：左侧为 True 时不求值右侧（短路）
    print("True or expensive:", True or expensive())


def main():
    print("=" * 50)
    print("02 - Control Flow")
    print("=" * 50)
    demo_if_elif()
    demo_for_while()
    demo_match()
    demo_boolean_short_circuit()
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
