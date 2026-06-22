"""
08_imports_modules.py - import 规则、__name__、模块执行

学习要点:
1. import / from ... import 的区别
2. __name__ == "__main__" 表示脚本直接运行
3. 模块搜索路径与包的概念（同目录模块）
"""

import demo_module
from demo_module import add, VERSION


def demo_import_styles():
    print("\n=== import 方式 ===")
    print(f"demo_module.VERSION = {demo_module.VERSION}")
    print(f"add(2, 3) = {add(2, 3)}")


def demo_name_main():
    print("\n=== __name__ ===")
    print(f"本文件 __name__ = {__name__!r}")
    print("直接运行脚本时为 '__main__'，被 import 时为模块名")


def demo_dir_builtin():
    print("\n=== 内置与模块属性 ===")
    print(f"demo_module 公开名: {[n for n in dir(demo_module) if not n.startswith('_')]}")


def main():
    print("=" * 50)
    print("08 - Imports & Modules")
    print("=" * 50)
    demo_import_styles()
    demo_name_main()
    demo_dir_builtin()
    print("\n提示: 也可运行  python demo_module.py  观察 __main__ 行为")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
