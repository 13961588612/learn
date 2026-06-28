"""
04_config_profiles.py - Provider profile 配置

学习要点:
1. 多 profile 切换模型后端而不改业务 prompt
2. JSON 配置结构（简化模拟 ~/.openharness/）
"""

import json              # dumps/loads 序列化与反序列化 JSON
from pathlib import Path  # 面向对象的路径操作，跨平台


def demo_profiles():
    """创建 mock 配置文件、读写 JSON、模拟 profile 切换。"""
    # Path(__file__) 当前脚本路径；.parent 上级目录；/ 运算符拼接路径
    config_dir = Path(__file__).parent / "data" / "mock_config"
    # mkdir(parents=True, exist_ok=True)：递归创建目录，已存在不报错
    config_dir.mkdir(parents=True, exist_ok=True)
    profiles_path = config_dir / "profiles.json"

    # 嵌套字典字面量，模拟 OpenHarness profiles 配置结构
    profiles = {
        "default": "company-gateway",
        "profiles": {
            "company-gateway": {
                "provider": "anthropic-compatible",
                "base_url": "https://internal.example/v1",
                "model": "company-default",
            },
            "openai-dev": {
                "provider": "openai-compatible",
                "base_url": "https://api.openai.com/v1",
                "model": "gpt-4o-mini",
            },
        },
        "active": "company-gateway",
    }

    # write_text：写入字符串；json.dumps 转 JSON，indent=2 美化缩进
    profiles_path.write_text(json.dumps(profiles, indent=2), encoding="utf-8")
    loaded = json.loads(profiles_path.read_text(encoding="utf-8"))

    print(f"  配置文件: {profiles_path}")
    print(f"  当前 active: {loaded['active']}")
    # .keys() 返回字典键视图；list() 转为可打印的列表
    print(f"  可用 profiles: {list(loaded['profiles'].keys())}")

    # 模拟切换 active profile
    loaded["active"] = "openai-dev"
    profiles_path.write_text(json.dumps(loaded, indent=2), encoding="utf-8")
    print(f"  切换后 active: {loaded['active']}")


def main():
    print("=" * 50)
    print("04 - Config Profiles")
    print("=" * 50)
    demo_profiles()
    print("\n[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
