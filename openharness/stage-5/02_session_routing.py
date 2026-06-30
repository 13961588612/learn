"""
02_session_routing.py - 会话 ID / 用户 ID 映射
"""

from dataclasses import dataclass  # @dataclass 自动生成 __init__、__repr__ 等


# @dataclass 装饰器：为下面字段生成数据类，省去手写样板代码
@dataclass
class SessionRoute:
    channel: str              # IM 通道标识，如 feishu
    external_user_id: str     # 外部系统用户 ID
    harness_thread_id: str    # Harness 内部线程 ID
    profile: str              # 租户 profile 名


def route_im_message(channel: str, user_id: str, tenant: str) -> SessionRoute:
    # f-string 拼接 profile 名；-> SessionRoute 标注返回值类型
    profile = f"tenant-{tenant}"  # str
    thread = f"{channel}:{user_id}"  # str：用冒号组合通道与用户，形成唯一 thread key
    # 位置参数构造 SessionRoute；dataclass 按字段顺序接收
    return SessionRoute(channel, user_id, thread, profile)


def main():
    print("=" * 50)   # 字符串 * 整数：重复 50 次
    print("02 - Session Routing")
    print("=" * 50)
    r = route_im_message("feishu", "u-1001", "acme")  # SessionRoute
    print(f"  {r}")   # dataclass 自动生成 __repr__，打印可读字段
    print("\n[OK] 完成")


# 直接运行本文件时 __name__ == "__main__"；被 import 时为模块名
if __name__ == "__main__":
    main()
