"""
02_session_routing.py - 会话 ID / 用户 ID 映射
"""

from dataclasses import dataclass


@dataclass
class SessionRoute:
    channel: str
    external_user_id: str
    harness_thread_id: str
    profile: str


def route_im_message(channel: str, user_id: str, tenant: str) -> SessionRoute:
    profile = f"tenant-{tenant}"
    thread = f"{channel}:{user_id}"
    return SessionRoute(channel, user_id, thread, profile)


def main():
    print("=" * 50)
    print("02 - Session Routing")
    print("=" * 50)
    r = route_im_message("feishu", "u-1001", "acme")
    print(f"  {r}")
    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
