"""
03_tool_docstring_routing.py - docstring 引导模型选 Tool

学习要点:
1. docstring 第一行是路由摘要
2. 明确 When to use / Do NOT use
"""

from pydantic import BaseModel, Field  # 定义 Tool 入参 schema


class GetServiceStatusInput(BaseModel):
    """查询服务状态 Tool 的入参。"""

    service_name: str = Field(description="服务名，如 order-api")


def get_service_status(params: GetServiceStatusInput) -> str:
    """
    查询内部服务健康状态（只读）。

    When to use:
    - 用户问某服务是否在线、健康检查失败原因

    Do NOT use:
    - 重启服务（无写权限）
    - 查询未注册的外部 URL
    """
    # 模拟服务名 -> 状态映射
    mock = {"order-api": "healthy", "payment-api": "degraded"}
    name = params.service_name  # 从 Pydantic 模型读取字段
    # in 运算符检查键是否存在于 dict
    if name not in mock:
        # list(mock.keys()) 取所有键的列表，嵌入错误提示
        return f"ERROR: 未知服务 {name!r}，可用: {list(mock.keys())}"
    return f"{name}: {mock[name]}"  # dict[key] 按键取值


def main():
    """打印 docstring 预览并演示 Tool 调用。"""
    print("=" * 50)
    print("03 - Tool Docstring Routing")
    print("=" * 50)
    # __doc__ 属性保存函数的三引号文档字符串
    print(f"\n  docstring 预览:\n{get_service_status.__doc__}")
    # 一行内构造模型并调用函数
    print(f"\n  调用: {get_service_status(GetServiceStatusInput(service_name='order-api'))}")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
