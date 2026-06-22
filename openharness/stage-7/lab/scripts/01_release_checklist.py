RELEASE_CHECKLIST = [
    "openh --dry-run 全绿",
    "staging 冒烟 stream-json",
    "审计日志采样 review",
    "权限 settings.json 与 prod 一致",
    "回滚方案 documented",
]


def main():
    print("=" * 50)
    print("Lab - Release Checklist")
    print("=" * 50)
    for i, item in enumerate(RELEASE_CHECKLIST, 1):
        print(f"  [ ] {i}. {item}")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
