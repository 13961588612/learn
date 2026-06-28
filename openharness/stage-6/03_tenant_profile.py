"""
03_tenant_profile.py - 多租户 profile 路由
"""


def pick_profile(tenant_id: str, env: str) -> str:
    # f-string 拼接环境名与租户 ID；-> str 标注返回字符串
    return f"{env}-{tenant_id}-default"


def main():
    print("=" * 50)   # 字符串 * 整数：重复 50 次
    print("03 - Tenant Profile")
    print("=" * 50)
    print(f"  acme prod: {pick_profile('acme', 'prod')}")
    print("\n[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
