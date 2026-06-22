import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src" / "tools"))
from internal_docs import search_internal_docs


def test_search_hit():
    out = search_internal_docs("发布")
    assert "D1" in out


def test_search_miss():
    out = search_internal_docs("不存在xyz")
    assert out.startswith("ERROR:")


if __name__ == "__main__":
    test_search_hit()
    test_search_miss()
    print("[OK] tests passed")
