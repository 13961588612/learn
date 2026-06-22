"""demo_module.py - 供 08_imports_modules.py 演示的示例模块"""

VERSION = "1.0.0"


def add(a: int, b: int) -> int:
    return a + b


def _private_helper() -> str:
    return "不应被外部直接依赖"


if __name__ == "__main__":
    print("demo_module 被直接运行（通常作为脚本入口）")
