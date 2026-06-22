# 阶段一：Harness 心智模型 + 本地跑通（P0）

> 对应 [`../../base/openharness/`](../../base/openharness/) P0 · W1–W2

## 前置

- 建议先完成 `python/stage-1` 或 `langchain/stage-1`
- Python 3.11+；可选安装 `openharness-ai`（`pip install openharness-ai`）

## 启动学习

```bash
# 项目根目录
uv sync --group openharness-stage-1   # 可选，含 python-dotenv

uv run python openharness/stage-1/01_harness_concepts.py
# ... 按编号至 10
uv run python openharness/stage-1/10_stage1_final.py
```

## 练习脚本速览

| 编号 | 文件 | 核心知识点 | 需 CLI |
|------|------|-----------|:---:|
| 01 | `01_harness_concepts.py` | 四层架构、十子系统 | |
| 02 | `02_agent_loop_simulator.py` | Agent Loop 模拟 | |
| 03 | `03_dry_run_cli.py` | `openh --dry-run` | 可选 |
| 04 | `04_config_profiles.py` | profile 切换 | |
| 05 | `05_readiness_states.py` | ready/warning/blocked | |
| 06 | `06_stream_json_events.py` | stream-json 事件 | |
| 07 | `07_tool_use_cycle.py` | tool_result 消息 | |
| 08 | `08_permission_gate.py` | path_rules / deny | |
| 09 | `09_subsystems_quiz.py` | 子系统速查 | |
| 10 | `10_stage1_final.py` | **综合**迷你 Harness | |

## P0 验收

- [ ] 白板画出 Agent Loop
- [ ] 解释 blocked 的 next actions
- [ ] 完成 `10_stage1_final.py`

## 下一步

[stage-2.md](stage-2.md)（Tools + Skills + Permissions）
