"""
04_config_profiles.py - Provider profile 配置

学习要点:
1. 多 profile 切换模型后端而不改业务 prompt
2. JSON 配置结构（简化模拟 ~/.openharness/）
"""

import json
from pathlib import Path


def demo_profiles():
    config_dir = Path(__file__).parent / "data" / "mock_config"
    config_dir.mkdir(parents=True, exist_ok=True)
    profiles_path = config_dir / "profiles.json"

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

    profiles_path.write_text(json.dumps(profiles, indent=2), encoding="utf-8")
    loaded = json.loads(profiles_path.read_text(encoding="utf-8"))

    print(f"  配置文件: {profiles_path}")
    print(f"  当前 active: {loaded['active']}")
    print(f"  可用 profiles: {list(loaded['profiles'].keys())}")

    # 模拟切换
    loaded["active"] = "openai-dev"
    profiles_path.write_text(json.dumps(loaded, indent=2), encoding="utf-8")
    print(f"  切换后 active: {loaded['active']}")


def main():
    print("=" * 50)
    print("04 - Config Profiles")
    print("=" * 50)
    demo_profiles()
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
