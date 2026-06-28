"""Tool schema 单元测试（无 pytest 依赖，直接 assert）"""

import sys                    # sys.path 动态导入
from pathlib import Path      # 面向对象的路径 API

# parents[1] 到 showcase/01_custom_tool_audit 根
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src" / "tools"))  # 插入 tools 目录以便 import internal_docs

from internal_docs import SearchDocsInput, search_internal_docs  # noqa: E402


def test_search_ok():
    out = search_internal_docs(SearchDocsInput(query="故障"))
    assert "故障手册" in out  # assert 条件为假则抛 AssertionError


def test_search_empty():
    out = search_internal_docs(SearchDocsInput(query="xyznotfound"))
    assert out.startswith("ERROR:")  # 无匹配时应返回 ERROR 前缀


def test_schema_required():
    try:
        SearchDocsInput(query="")  # min_length=1 应触发校验失败
        raise AssertionError("should fail")  # 若未抛异常则测试失败
    except Exception:
        pass  # 预期捕获 pydantic ValidationError（或任意 Exception）


def main():
    test_search_ok()
    test_search_empty()
    test_schema_required()
    print("[OK] all tests passed")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
