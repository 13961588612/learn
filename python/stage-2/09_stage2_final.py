"""
09_stage2_final.py - 综合：notes 包（类 + JSON 持久化）

学习要点:
1. 将模型与存储分离到包内模块
2. 通过 NoteStore 完成 CRUD 式操作
3. 数据持久化到 data/notes.json
"""

from pathlib import Path

from notes import NoteStore


def main():
    print("=" * 50)
    print("09 - Stage 2 Final")
    print("=" * 50)

    db_path = Path(__file__).parent / "data" / "notes.json"
    store = NoteStore(db_path)

    if not store.list_all():
        store.add("学习 Python", "完成 stage-1 与 stage-2")
        store.add("学习 LangChain", "进入 langchain/stage-1")
        print("\n已写入示例笔记")
    else:
        print("\n加载已有笔记")

    print("\n全部笔记:")
    for note in store.list_all():
        print(f"  [{note.id}] {note.title}: {note.content}")

    hits = store.find_by_title("python")
    print(f"\n搜索 'python': {[n.title for n in hits]}")
    print(f"\n数据文件: {db_path}")
    print("\n[OK] 阶段二综合练习完成")


if __name__ == "__main__":
    main()
