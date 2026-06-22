"""03_builtin_tools_catalog.py - 内置 Tool 分类"""

CATALOG = {
    "filesystem": ["Read", "Write", "Edit", "Glob", "Grep"],
    "shell": ["Bash"],
    "task": ["TaskCreate", "TaskList", "TaskGet", "TaskUpdate"],
    "meta": ["ResetTools", "SkillViewer"],
}


def main():
    print("=" * 50)
    print("03 - Builtin Tools Catalog")
    print("=" * 50)
    for cat, tools in CATALOG.items():
        print(f"  [{cat}] {', '.join(tools)}")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
