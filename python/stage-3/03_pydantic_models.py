"""
03_pydantic_models.py - BaseModel、校验、嵌套模型、model_dump

学习要点:
1. Pydantic 在运行时校验数据并自动类型转换
2. Field 约束字段规则（范围、长度等）
3. 嵌套 BaseModel 表达复杂结构
4. model_dump / model_dump_json 序列化为 dict / JSON
"""

from pydantic import BaseModel, Field, ValidationError


class Address(BaseModel):
    city: str
    country: str = "CN"  # 默认值


class User(BaseModel):
    id: int
    name: str = Field(min_length=1, max_length=50)
    email: str
    age: int = Field(ge=0, le=150)  # ge/le：大于等于 / 小于等于
    address: Address | None = None  # 嵌套模型，可选


def demo_valid_model():
    print("\n=== 合法数据 ===")
    user = User(
        id=1,
        name="Alice",
        email="alice@example.com",
        age=30,
        address={"city": "Shanghai"},  # dict 自动转为 Address
    )
    print(f"User: {user}")
    print(f"model_dump(): {user.model_dump()}")
    print(f"model_dump_json(): {user.model_dump_json()}")


def demo_validation_error():
    print("\n=== 校验失败 ===")
    try:
        User(id=2, name="", email="bad", age=-1)
    except ValidationError as e:
        # e.errors() 返回结构化错误列表，便于 API 返回 422
        for err in e.errors():
            loc = ".".join(str(x) for x in err["loc"])
            print(f"  {loc}: {err['msg']}")


def demo_nested():
    print("\n=== 嵌套模型 ===")
    team = {
        "lead": {"id": 1, "name": "Bob", "email": "b@ex.com", "age": 35},
        "members": [
            {"id": 2, "name": "Carol", "email": "c@ex.com", "age": 28},
        ],
    }

    class Team(BaseModel):
        lead: User
        members: list[User]

    parsed = Team.model_validate(team)  # model_validate：从 dict 解析并校验
    print(f"团队负责人: {parsed.lead.name}, 成员数: {len(parsed.members)}")


def main():
    print("=" * 50)
    print("03 - Pydantic Models")
    print("=" * 50)
    demo_valid_model()
    demo_validation_error()
    demo_nested()
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
