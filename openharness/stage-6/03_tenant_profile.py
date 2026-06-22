"""
03_tenant_profile.py - 多租户 profile 路由
"""

def pick_profile(tenant_id: str, env: str) -> str:
    return f"{env}-{tenant_id}-default"


def main():
    print("=" * 50)
    print("03 - Tenant Profile")
    print("=" * 50)
    print(f"  acme prod: {pick_profile('acme', 'prod')}")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
