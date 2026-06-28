"""
05_comprehensions.py - 列表/字典推导、生成器表达式、yield 入门

学习要点:
1. 推导式简洁创建 list/dict/set
2. 生成器表达式惰性求值，节省内存
3. yield 把函数变为生成器，逐步产出值
"""


def demo_list_comprehension():
    print("\n=== 列表推导 ===")
    # [表达式 for 变量 in 可迭代对象]
    squares = [x * x for x in range(1, 6)]
    # 带条件过滤：[表达式 for ... if 条件]
    evens = [x for x in range(10) if x % 2 == 0]
    print(f"squares: {squares}")
    print(f"evens: {evens}")


def demo_dict_set_comprehension():
    print("\n=== 字典 / 集合推导 ===")
    word = "hello"
    # {键: 值 for ...} 字典推导；set(word) 去重得到唯一字符
    freq = {ch: word.count(ch) for ch in set(word)}
    # {表达式 for ...} 集合推导
    unique_lengths = {len(w) for w in ["ai", "ml", "llm"]}
    print(f"freq: {freq}")
    print(f"unique_lengths: {unique_lengths}")


def demo_generator_expression():
    print("\n=== 生成器表达式 ===")
    # (表达式 for ...) 圆括号 → 生成器表达式，惰性求值不立即算完
    gen = (x * x for x in range(1, 6))
    print(f"type: {type(gen).__name__}")
    # next(gen) 逐个取值；列表推导包一层可一次取多个
    print(f"first three: {[next(gen) for _ in range(3)]}")


def count_up_to(n: int):
    """含 yield 的函数是生成器函数，调用返回生成器对象而非直接返回值"""
    current = 1
    while current <= n:
        yield current  # 产出值并暂停，下次 next() 从这里继续
        current += 1


def demo_yield():
    print("\n=== yield 生成器 ===")
    # for 循环自动调用 next()，StopIteration 时结束
    for value in count_up_to(5):
        print(f"  got {value}")


def main():
    print("=" * 50)
    print("05 - Comprehensions & Generators")
    print("=" * 50)
    demo_list_comprehension()
    demo_dict_set_comprehension()
    demo_generator_expression()
    demo_yield()
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
