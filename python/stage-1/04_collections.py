"""
04_collections.py - list/dict/set/tuple、常用方法、浅拷贝

学习要点:
1. list 可变有序，tuple 不可变有序
2. dict 键值映射，set 无序唯一元素
3. 切片与常用方法
4. 浅拷贝 vs 深拷贝
"""

import copy  # deepcopy 递归复制嵌套对象


def demo_list_tuple():
    print("\n=== list / tuple ===")
    nums = [10, 20, 30]   # list：可变、有序
    nums.append(40)       # 原地追加元素
    print(f"list: {nums}, slice[1:]: {nums[1:]}")  # [1:] 切片：从索引 1 到末尾

    point = (1, 2)  # tuple：不可变、有序
    print(f"tuple: {point}, 不可变 -> 解包 x,y = point => {point[0]}, {point[1]}")


def demo_dict_set():
    print("\n=== dict / set ===")
    user = {"name": "Dave", "role": "admin"}  # dict：键值映射
    user["city"] = "Beijing"  # 新增或覆盖键
    print(f"dict keys: {list(user.keys())}")  # keys() 返回视图，转 list 便于打印

    # set：无序、元素唯一，重复值自动去重
    tags = {"python", "java", "python", "go"}
    print(f"set 去重: {tags}")


def demo_copy():
    print("\n=== 浅拷贝 vs 深拷贝 ===")
    original = {"items": [1, 2, 3]}
    shallow = original.copy()       # 浅拷贝：顶层新 dict，嵌套 list 仍共享引用
    deep = copy.deepcopy(original)  # 深拷贝：递归复制所有嵌套对象

    shallow["items"].append(99)  # 修改嵌套 list 会影响 original
    print(f"original after shallow mutate: {original}")
    print(f"deep still: {deep}")


def demo_useful_methods():
    print("\n=== 常用方法 ===")
    words = ["banana", "apple", "cherry"]
    words.sort(key=len)  # 原地排序，key=len 按字符串长度
    print(f"sorted by len: {words}")

    text = "  hello world  "
    print(f"strip: {text.strip()!r}")  # strip() 去除首尾空白


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
