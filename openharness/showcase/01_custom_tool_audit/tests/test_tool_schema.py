"""Tool schema 单元测试（无 pytest 依赖，直接 assert）"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src" / "tools"))

from internal_docs import SearchDocsInput, search_internal_docs  # noqa: E402


def test_search_ok():
    out = search_internal_docs(SearchDocsInput(query="故障"))
    assert "故障手册" in out


def test_search_empty():
    out = search_internal_docs(SearchDocsInput(query="xyznotfound"))
    assert out.startswith("ERROR:")


def test_schema_required():
    try:
        SearchDocsInput(query="")
        raise AssertionError("should fail")
    except Exception:
        pass


def main():
    test_search_ok()
    test_search_empty()
    test_schema_required()
    print("[OK] all tests passed")


if __name__ == "__main__":
    main()
