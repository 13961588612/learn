import json
from pathlib import Path

from notes.models import Note


class NoteStore:
    """JSON 文件持久化的简单笔记仓库"""

    def __init__(self, path: Path):
        self.path = path
        self._notes: list[Note] = []
        self._next_id = 1
        self._load()

    def _load(self) -> None:
        if not self.path.exists():
            return
        data = json.loads(self.path.read_text(encoding="utf-8"))
        self._notes = [Note.from_dict(item) for item in data.get("notes", [])]
        self._next_id = data.get("next_id", 1)

    def _save(self) -> None:
        payload = {
            "next_id": self._next_id,
            "notes": [n.to_dict() for n in self._notes],
        }
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    def add(self, title: str, content: str) -> Note:
        note = Note(id=self._next_id, title=title, content=content)
        self._next_id += 1
        self._notes.append(note)
        self._save()
        return note

    def list_all(self) -> list[Note]:
        return list(self._notes)

    def find_by_title(self, keyword: str) -> list[Note]:
        kw = keyword.lower()
        return [n for n in self._notes if kw in n.title.lower()]
