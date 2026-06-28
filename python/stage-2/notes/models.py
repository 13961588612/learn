from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class Note:
    title: str
    content: str
    id: int | None = None  # int | None 等价于 Optional[int]（Python 3.10+ 联合类型写法）
    # default_factory 每次实例化时调用，避免可变默认值陷阱
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict:
        """实例 → 可 JSON 序列化的 dict"""
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Note":
        """dict → Note 实例；类方法便于反序列化"""
        return cls(
            id=data.get("id"),  # .get 键缺失时返回 None 而非 KeyError
            title=data["title"],
            content=data["content"],
            created_at=data.get("created_at", datetime.now(timezone.utc).isoformat()),
        )
