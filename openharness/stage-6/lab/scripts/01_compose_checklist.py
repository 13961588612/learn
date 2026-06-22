"""检查 base openharness docker-compose 是否存在并打印服务列表"""

from pathlib import Path

STUDY_ROOT = Path(__file__).resolve().parents[5]
compose = STUDY_ROOT / "base" / "openharness" / "docker-compose.yml"


def main():
    print("=" * 50)
    print("Lab - Docker Compose Checklist")
    print("=" * 50)

    if not compose.exists():
        print(f"  未找到: {compose}")
        return

    text = compose.read_text(encoding="utf-8")
    print(f"  路径: {compose}")
    for line in text.splitlines():
        if line.strip().startswith("image:") or "container_name:" in line:
            print(f"  {line.strip()}")
    print("\n  运行: cd base/openharness && docker compose up -d")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
