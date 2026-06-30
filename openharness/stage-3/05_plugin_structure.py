"""
05_plugin_structure.py - Plugin 目录约定

学习要点:
1. Plugin = 可分发「扩展包」：斜杠命令 + Hook（+ 可选子 Agent）
2. 与 Skill（流程文档）、Tool（可执行函数）、MCP（外部协议）的分工
3. 目录三部分：.claude-plugin/plugin.json、commands/、hooks/
4. oh plugin list / enable / disable 启用与卸载
"""

from pathlib import Path


# ---------------------------------------------------------------------------
# 1. 完整目录树（带职责标注）
# ---------------------------------------------------------------------------
PLUGIN_LAYOUT = """
my-plugin/                          # 插件根目录（可来自官方市场或公司 Git 仓库）
├── .claude-plugin/
│   └── plugin.json                 # 清单：name / version / description（身份与版本）
├── commands/                       # 斜杠命令：用户在 TUI 输入 /deploy-check 触发
│   └── deploy-check.md             # 每个 .md = 一条命令的提示词模板
└── hooks/
    └── hooks.json                  # Hook 注册表：PreToolUse / PostToolUse（见 06）
"""

# ---------------------------------------------------------------------------
# 2. plugin.json 最小示例（清单文件，不含业务逻辑）
# ---------------------------------------------------------------------------
PLUGIN_MANIFEST = {
    "name": "company-deploy-guard",
    "version": "1.0.0",
    "description": "发布前检查 + 禁止写生产路径",
}

# ---------------------------------------------------------------------------
# 3. 与 Skill / Tool / MCP 对比（避免混淆）
# ---------------------------------------------------------------------------
COMPARISON = [
    ("Plugin", "打包分发", "commands/ + hooks/ + plugin.json", "公司级策略一键启用"),
    ("Skill", "流程文档", "skills/<name>/SKILL.md", "Runbook、发布规范（按需注入上下文）"),
    ("Tool", "可执行能力", "Python 函数 / MCP tool", "查库、读文件、调 API"),
    ("MCP", "外部协议", "servers.json + Server 进程", "工单系统、内部 API 只读接入"),
]

# ---------------------------------------------------------------------------
# 4. 启用流程（Harness 加载顺序概念）
# ---------------------------------------------------------------------------
LOAD_STEPS = [
    "openh plugin list          # 列出已安装插件",
    "openh plugin enable <name> # 启用：合并 commands + 注册 hooks",
    "openh                      # 重启 TUI 后 /命令 与 Hook 生效",
    "openh plugin disable <name># 禁用：撤销合并，不删文件",
]


def print_section(title: str) -> None:
    print(f"\n=== {title} ===")


def main():
    print("=" * 50)
    print("05 - Plugin Structure")
    print("=" * 50)

    print_section("Plugin 是什么")
    print("  Plugin 把「斜杠命令」和「Hook 策略」打成一个可安装包。")
    print("  公司场景：安全审计、发布门禁、合规检查 —— 一次 enable，全员生效。")
    print("  与 stage-2 Hook 的关系：Hook 是机制；Plugin 是 Hook 的打包与分发方式。")

    print_section("目录结构")
    print(PLUGIN_LAYOUT)

    print_section("plugin.json 示例")
    for key, val in PLUGIN_MANIFEST.items():  # key: str；val: str
        print(f"  {key}: {val}")

    print_section("commands/ 做什么")
    print("  每个 .md 文件定义一条 /斜杠命令 的行为（类似 Skill 但更短、更可操作）。")
    print("  例：commands/deploy-check.md → 用户在 TUI 输入 /deploy-check")
    print("       Harness 把该 md 内容注入上下文，引导模型按公司 checklist 执行。")

    print_section("hooks/ 做什么")
    print("  hooks/hooks.json 声明 PreToolUse / PostToolUse 规则（详见 06_plugin_hooks.py）。")
    print("  例：Write|Edit 前拦截 /prod 路径；所有 Tool 调用后写审计日志。")
    print("  Plugin enable 时，Harness 把这些规则并入全局 Hook 链。")

    print_section("与 Skill / Tool / MCP 对比")
    for kind, essence, format_, use in COMPARISON:  # kind: str；essence: str；format_: str；use: str
        print(f"\n  [{kind}] {essence}")
        print(f"    形态: {format_}")
        print(f"    场景: {use}")

    print_section("安装位置（类比 Skills）")
    print("  用户级: ~/.openharness/plugins/<name>/")
    print("  项目级: <repo>/.openharness/plugins/<name>/")
    print("  官方插件: openh plugin list 可见（如 security-guidance）")

    print_section("启用流程")
    for step in LOAD_STEPS:  # str
        print(f"  {step}")

    print_section("本仓库参考")
    showcase = Path(__file__).resolve().parents[1] / "showcase" / "01_custom_tool_audit"  # Path
    print(f"  {showcase.name}/  → Tool + Hook 示范（未打成 Plugin 包）")
    print("  完整 Plugin 示例见官方文档 / base/openharness")
    print("  下一步: 06_plugin_hooks.py 深入 hooks.json 字段")

    print("\n[OK] 完成")


if __name__ == "__main__":
    main()
