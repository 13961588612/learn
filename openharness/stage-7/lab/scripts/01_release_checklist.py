"""发布前检查清单"""

# 字符串列表：每项是一条发布前需确认的事项
RELEASE_CHECKLIST = [
    "openh --dry-run 全绿",
    "staging 冒烟 stream-json",
    "审计日志采样 review",
    "权限 settings.json 与 prod 一致",
    "回滚方案 documented",
]


def main():
    print("=" * 50)   # 字符串 * 整数：重复 50 次
    print("Lab - Release Checklist")
    print("=" * 50)
    # enumerate(iterable, start=1)：同时得到序号 i（从 1 起）与元素 item
    for i, item in enumerate(RELEASE_CHECKLIST, 1):
        print(f"  [ ] {i}. {item}")
    print("\n[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
