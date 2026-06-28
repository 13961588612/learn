"""notes 包 - stage-2 综合练习用的小型笔记模块"""

from notes.models import Note
from notes.storage import NoteStore

# __all__ 定义 from notes import * 时导出的公开名称
__all__ = ["Note", "NoteStore"]
