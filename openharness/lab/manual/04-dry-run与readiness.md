# 4 · dry-run 与 readiness

[← 返回 Lab 总入口](../README.md)

---

## 4.1 dry-run 是什么

`openh --dry-run` **不会**：

- 调用 LLM
- 执行任何 Tool / MCP
- 修改文件系统（除读取配置做检查）

**会**：

- 检查 profile、API Key、MCP 配置、Skills 路径等
- 输出 **readiness** 与 **next actions**

适合：CI 门禁、发布前冒烟、排查「为什么一跑就挂」。

---

## 4.2 命令

```bash
openh --dry-run
openh --dry-run -p "Explain this repository" --output-format json
```

辅助脚本：

```bash
cd learn
uv run python openharness/stage-1/lab/scripts/02_run_dry_run.py
```

输出 JSON 保存在 `stage-1/lab/experiments/dry_run_*.json`。

---

## 4.3 readiness 三态

| 状态 | 含义 | 典型动作 |
|------|------|----------|
| **ready** | 可正常运行 | 继续 lab / 发布 |
| **warning** | 能跑但有风险 | 读 warnings，staging 前修复 |
| **blocked** | 不应继续 | 按 next actions 逐项修复 |

---

## 4.4 常见 blocked 原因

| 现象 | 可能原因 | 修复 |
|------|----------|------|
| 无 profile | 未 `setup` | `openh setup` |
| API Key 缺失 | profile 未配密钥 | setup 或编辑 profile |
| MCP 命令找不到 | `servers.json` 中 command 路径错误 | 修正 cwd / 绝对路径 |
| Python/uv 不在 PATH | MCP 用 `uv run` 启动 | 在 MCP env 或系统 PATH 修复 |
| Skills 路径无效 | `.openharness/skills` 结构错误 | 每 skill 一个目录 + SKILL.md |

MCP 专项见 [08-MCP与Plugin.md](08-MCP与Plugin.md)。

---

## 4.5 如何解读 json 输出

关注顶层字段（名称因版本略有不同）：

- `readiness` / `status`
- `warnings` / `issues`
- `next_actions` / `suggestions`
- `profiles` / `mcp` 子项

**练习**：将 `dry_run_json` 实验文件中的字段列表抄到 `experiments/02-dry-run-notes.md`，并用中文解释每项。

---

## 4.6 CI 用法示例

```bash
openh --dry-run -p "smoke" --output-format json | jq -e '.readiness == "ready"'
# 无 jq 时：肉眼检查 exit code 与 stdout 含 ready
```

stage-7 发布 checklist 第一项即 dry-run 全绿。

---

## 4.7 对应实验

- [stage-1/lab/workbook/02-dry-run.md](../../stage-1/lab/workbook/02-dry-run.md)
- [stage-3/lab](../../stage-3/lab/README.md) — MCP dry-run
- 故障：[99-故障排查索引.md](99-故障排查索引.md) → 「dry-run blocked」
