"""
04_collections.py - list/dict/set/tuple、常用方法、浅拷贝

学习要点:
1. list 可变有序，tuple 不可变有序
2. dict 键值映射，set 无序唯一元素
3. 切片与常用方法
4. 浅拷贝 vs 深拷贝
"""

import copy


def demo_list_tuple():
    print("\n=== list / tuple ===")
    nums = [10, 20, 30]
    nums.append(40)
    print(f"list: {nums}, slice[1:]: {nums[1:]}")

    point = (1, 2)
    print(f"tuple: {point}, 不可变 -> 解包 x,y = point => {point[0]}, {point[1]}")


def demo_dict_set():
    print("\n=== dict / set ===")
    user = {"name": "Dave", "role": "admin"}
    user["city"] = "Beijing"
    print(f"dict keys: {list(user.keys())}")

    tags = {"python", "java", "python", "go"}
    print(f"set 去重: {tags}")


def demo_copy():
    print("\n=== 浅拷贝 vs 深拷贝 ===")
    original = {"items": [1, 2, 3]}
    shallow = original.copy()
    deep = copy.deepcopy(original)

    shallow["items"].append(99)
    print(f"original after shallow mutate: {original}")
    print(f"deep still: {deep}")


def demo_useful_methods():
    print("\n=== 常用方法 ===")
    words = ["banana", "apple", "cherry"]
    words.sort(key=len)
    print(f"sorted by len: {words}")

    text = "  hello world  "
    print(f"strip: {text.strip()!r}")


def main():
    print("=" * 50)
    print("04 - Collections")
    print("=" * 50)
    demo_list_tuple()
    demo_dict_set()
    demo_copy()
    demo_useful_methods()
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
