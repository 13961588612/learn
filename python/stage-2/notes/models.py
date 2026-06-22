from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class Note:
    title: str
    content: str
    id: int | None = None
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Note":
        return cls(
            id=data.get("id"),
            title=data["title"],
            content=data["content"],
            created_at=data.get("created_at", datetime.now(timezone.utc).isoformat()),
        )
