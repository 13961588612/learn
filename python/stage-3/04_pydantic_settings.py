"""
04_pydantic_settings.py - pydantic-settings、.env 配置类

学习要点:
1. BaseSettings 从环境变量 / .env 文件加载配置
2. 字段名 APP_NAME 对应环境变量 APP_NAME（大小写不敏感可配置）
3. 类型自动转换（如 "true" → bool）
4. 复制 .env.example 为 .env 后可在本目录覆盖默认值
"""

from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    # model_config 指定 .env 路径与编码；env_file 相对于当前工作目录
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # 忽略 .env 中未定义的额外键
    )

    app_name: str = "Stage3Demo"
    debug: bool = False
    api_timeout: float = Field(default=5.0, gt=0)
    data_dir: Path = Path("data")


def main():
    print("=" * 50)
    print("04 - Pydantic Settings")
    print("=" * 50)

    settings = AppSettings()
    print(f"\napp_name   = {settings.app_name!r}")
    print(f"debug      = {settings.debug}")
    print(f"api_timeout = {settings.api_timeout}")
    print(f"data_dir   = {settings.data_dir}")

    print("\n提示: 复制 .env.example → .env 可覆盖上述默认值")
    print("  APP_NAME=MyApp")
    print("  DEBUG=true")
    print("  API_TIMEOUT=10.0")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
