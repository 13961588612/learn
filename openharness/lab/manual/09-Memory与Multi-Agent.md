# 9 · Memory 与 Multi-Agent

[← 返回 Lab 总入口](../README.md)

---

## 9.1 MEMORY.md（跨会话记忆）

路径（项目级）：

```
.openharness/MEMORY.md
```

生成示例：

```bash
cd learn
uv run python openharness/stage-4/lab/scripts/01_seed_memory_md.py
# 写入 stage-4/lab/.openharness/MEMORY.md
```

**验证**：

1. 在 `stage-4/lab` 启动 `openh`
2. 新会话中问：「我们的发布窗口是什么时候？」（应能引用 MEMORY）
3. 或使用 `/resume` 恢复 thread

---

## 9.2 长会话与 Compaction

现象：多轮 tool 调用后 context 变长、变慢、变贵。

Harness 侧策略（概念，见 stage-4 概念脚本 `05_compaction_sim.py`）：

- **Auto-Compaction**：摘要旧消息
- **MEMORY.md**：持久事实放文件，不重复塞进每轮 prompt
- **子 Agent offload**：重检索交给子任务

---

## 9.3 Coordinator / Task / 子 Agent

复杂任务模式：

```
用户任务 → Coordinator 拆分子 Task → 子 Agent 执行 → 汇总
```

实验 prompt 示例：

> 「先调研 openharness stage-4 目录有哪些脚本，再写一段 100 字摘要。」

观察：是否出现 Task 列表、子 Agent 输出、最终汇总。

概念脚本：

- `stage-4/01_coordinator_concepts.py`
- `stage-4/03_task_lifecycle.py`
- `stage-4/02_subagent_isolation.py`

---

## 9.4 max-turns 熔断

```bash
openh -p "Keep researching until done" --max-turns 5 --output-format json
```

或 lab 脚本：

```bash
uv run python openharness/stage-4/lab/scripts/02_max_turns_prompt.py
```

**验收**：达到上限后 Agent **明确停止**，而非无限 loop。

生产：**必须配置** max-turns 或等价熔断。

---

## 9.5 与 LangGraph 对比（笔记要点）

| 维度 | OpenHarness | LangGraph |
|------|-------------|-----------|
| 定位 | Agent **运行时壳** | 业务 **编排图** |
| 扩展 | Tool / Skill / MCP / Plugin | Node / Edge / State |
| 多 Agent | Coordinator + Task | 子图 / Send |
| HITL | permission + TUI | interrupt |

详见 [notes/harness-vs-langchain.md](../../notes/harness-vs-langchain.md)。

---

## 9.6 实验清单（stage-4）

- [ ] MEMORY.md 在新会话被引用
- [ ] 多轮 tool 后观察 context 行为（记录到 experiments）
- [ ] Coordinator 类任务可演示分工
- [ ] max-turns 触发终止
- [ ] experiments/ 有对比 LangGraph 笔记

---

## 9.7 对应实验

- [stage-4/lab/README.md](../../stage-4/lab/README.md)
- [stage-1/lab/workbook/06-engine-reading.md](../../stage-1/lab/workbook/06-engine-reading.md)
- 故障：[99-故障排查索引.md](99-故障排查索引.md) → 「MEMORY 不生效」「Agent 死循环」
