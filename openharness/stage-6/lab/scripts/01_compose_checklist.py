"""检查 base openharness docker-compose 是否存在并打印服务列表"""

from pathlib import Path  # Path 对象支持 / 拼接、exists()、read_text()

# parents[5] 从 lab/scripts/ 向上 6 级到仓库 learn 根目录
STUDY_ROOT = Path(__file__).resolve().parents[5]  # Path
# Path / str：用 / 运算符拼接路径段
compose = STUDY_ROOT / "base" / "openharness" / "docker-compose.yml"  # Path


def main():
    print("=" * 50)   # 字符串 * 整数：重复 50 次
    print("Lab - Docker Compose Checklist")
    print("=" * 50)

    if not compose.exists():  # 文件不存在则提前 return
        print(f"  未找到: {compose}")
        return

    text = compose.read_text(encoding="utf-8")  # str
    print(f"  路径: {compose}")
    for line in text.splitlines():  # str
        # strip() 去空白；startswith / in 过滤 image 与 container_name 行
        if line.strip().startswith("image:") or "container_name:" in line:
            print(f"  {line.strip()}")
    print("\n  运行: cd base/openharness && docker compose up -d")
    print("\n[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
