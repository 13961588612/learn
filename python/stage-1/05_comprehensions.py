"""
05_comprehensions.py - 列表/字典推导、生成器表达式、yield 入门

学习要点:
1. 推导式简洁创建 list/dict/set
2. 生成器表达式惰性求值，节省内存
3. yield 把函数变为生成器，逐步产出值
"""


def demo_list_comprehension():
    print("\n=== 列表推导 ===")
    squares = [x * x for x in range(1, 6)]
    evens = [x for x in range(10) if x % 2 == 0]
    print(f"squares: {squares}")
    print(f"evens: {evens}")


def demo_dict_set_comprehension():
    print("\n=== 字典 / 集合推导 ===")
    word = "hello"
    freq = {ch: word.count(ch) for ch in set(word)}
    unique_lengths = {len(w) for w in ["ai", "ml", "llm"]}
    print(f"freq: {freq}")
    print(f"unique_lengths: {unique_lengths}")


def demo_generator_expression():
    print("\n=== 生成器表达式 ===")
    gen = (x * x for x in range(1, 6))
    print(f"type: {type(gen).__name__}")
    print(f"first three: {[next(gen) for _ in range(3)]}")


def count_up_to(n: int):
    current = 1
    while current <= n:
        yield current
        current += 1


def demo_yield():
    print("\n=== yield 生成器 ===")
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
