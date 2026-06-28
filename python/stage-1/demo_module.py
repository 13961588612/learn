"""demo_module.py - 供 08_imports_modules.py 演示的示例模块"""

# 模块级变量：import demo_module 后可通过 demo_module.VERSION 访问
VERSION = "1.0.0"


def add(a: int, b: int) -> int:
    return a + b


def _private_helper() -> str:
    # 单下划线前缀：约定为内部实现，不应被外部直接依赖（非语法强制）
    return "不应被外部直接依赖"


if __name__ == "__main__":
    # 直接运行 demo_module.py 时进入此分支；被 import 时不执行
    print("demo_module 被直接运行（通常作为脚本入口）")
