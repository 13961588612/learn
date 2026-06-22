# OpenHarness 公司 Agent 后端学习计划

> **OpenHarness**（`oh` / Windows `openh`）是开源 **Agent Harness** 运行时：Engine、Tools、Skills、Plugins、Permissions、Hooks、MCP、Coordinator。  
> 与 [`langchain/`](../langchain/) 互补：LangChain 编排**业务逻辑**，OpenHarness 治理**运行时与扩展**。

**延伸资料**：[`../../base/openharness/`](../../base/openharness/)（14 周完整课表、P0–P6 项目骨架）  
**对照笔记**：[`notes/harness-vs-langchain.md`](notes/harness-vs-langchain.md)

---

## 最终学习目标

| 能力维度 | 具体表现 |
|---------|---------|
| **Harness 心智模型** | 能画出 Agent Loop、十子系统协作；解释「模型想、Harness 做」 |
| **扩展机制** | 自定义 Tool、Skills、Hooks、MCP、Plugin |
| **多 Agent 与记忆** | Coordinator、Task、MEMORY.md / Compaction 策略 |
| **Gateway 集成** | stream-json、Webhook 通道、会话路由 |
| **公司后端** | 权限基线、审计日志、部署与运维 |

---

## 阶段一：Harness 心智模型 + 本地跑通（P0 · 第 1–2 周）

**目标**：理解 Agent Loop；dry-run / CLI；配置 profile

- [ ] 四层架构：能力 / 安全 / 协作 / 基础设施
- [ ] Agent Loop：`stream → tool_use → permission → hook → execute → loop`
- [ ] `openh --dry-run` 解读 ready / warning / blocked
- [ ] Provider profile 切换
- [ ] stream-json 事件结构

**验收**：能手绘 Query → Engine → Tool → Permission → Hook → Loop

| 编号 | 文件 | 内容 |
|------|------|------|
| 01 | `01_harness_concepts.py` | 四层架构与十子系统速览 |
| 02 | `02_agent_loop_simulator.py` | Agent Loop 纯 Python 模拟 |
| 03 | `03_dry_run_cli.py` | 调用 `openh --dry-run`（可选） |
| 04 | `04_config_profiles.py` | profile 配置 JSON 读写 |
| 05 | `05_readiness_states.py` | ready / warning / blocked 判定 |
| 06 | `06_stream_json_events.py` | 解析 stream-json 事件流 |
| 07 | `07_tool_use_cycle.py` | tool_use → result 消息循环 |
| 08 | `08_permission_gate.py` | 工具调用前权限门禁 |
| 09 | `09_subsystems_quiz.py` | 十子系统对照自测 |
| 10 | `10_stage1_final.py` | **综合**：迷你 Harness 模拟器 |

详见 [stage-1.md](stage-1.md)。

---

## 阶段二：Tools + Skills + Permissions（P1 · 第 3–4 周）

**目标**：公司域 Tool、Skills 规范、Hooks 审计

- [ ] Pydantic Tool schema 与 docstring 路由
- [ ] PreToolUse / PostToolUse Hook
- [ ] SKILL.md 目录规范与加载
- [ ] permission mode、path_rules

| 编号 | 文件 | 内容 |
|------|------|------|
| 01 | `01_builtin_tools_catalog.py` | 内置 Tool 分类与公司禁用清单 |
| 02 | `02_custom_tool_pydantic.py` | 自定义只读 Tool + schema |
| 03 | `03_tool_docstring_routing.py` | docstring 引导模型选 Tool |
| 04 | `04_pre_tool_hook.py` | PreToolUse 拦截 |
| 05 | `05_post_tool_audit.py` | PostToolUse 审计日志 |
| 06 | `06_skill_md_format.py` | SKILL.md frontmatter 解析 |
| 07 | `07_skills_loader.py` | 扫描 `.openharness/skills/` |
| 08 | `08_permissions_rules.py` | path_rules / denied_commands |
| 09 | `09_plan_mode_concept.py` | default vs plan 模式对比 |
| 10 | `10_stage2_final.py` | **综合**：Tool + Hook + Skill |

详见 [stage-2.md](stage-2.md)。

---

## 阶段三：MCP + Plugins（P2 · 第 5–6 周）

**目标**：MCP Server 暴露内部只读能力；Plugin 结构

- [ ] MCP stdio 最小 Server
- [ ] Harness 侧 MCP 配置校验
- [ ] Plugin：commands + hooks 脚手架

| 编号 | 文件 | 内容 |
|------|------|------|
| 01 | `01_mcp_concepts.py` | MCP 角色与 Tool 暴露 |
| 02 | `02_mcp_tool_schema.py` | MCP Tool JSON Schema |
| 03 | `03_mcp_mock_server.py` | 模拟 MCP 请求/响应 |
| 04 | `04_mcp_config_validate.py` | servers.json 校验 |
| 05 | `05_plugin_structure.py` | Plugin 目录约定 |
| 06 | `06_plugin_hooks.py` | Plugin Hook 注册 |
| 07 | `07_mcp_security_baseline.py` | 只读 / 超时 / 白名单 |
| 08 | `08_stage3_final.py` | **综合**：MCP + 配置 + 安全 |

详见 [stage-3.md](stage-3.md)。

---

## 阶段四：Multi-Agent + Memory + Gateway 入门（P3–P4 · 第 7–10 周）

**目标**：Coordinator、Task、Memory；Gateway Webhook 概念

- [ ] 子 Agent 上下文隔离
- [ ] Task 生命周期；`--max-turns` 熔断
- [ ] MEMORY.md 与 Compaction
- [ ] Gateway stream-json 契约（概念 + 模拟）

| 编号 | 文件 | 内容 |
|------|------|------|
| 01 | `01_coordinator_concepts.py` | Coordinator / 子 Agent |
| 02 | `02_subagent_isolation.py` | 上下文隔离演示 |
| 03 | `03_task_lifecycle.py` | Task Create → Output → Stop |
| 04 | `04_memory_md.py` | MEMORY.md 读写策略 |
| 05 | `05_compaction_sim.py` | 长会话压缩模拟 |
| 06 | `06_max_turns_breaker.py` | tool 死循环熔断 |
| 07 | `07_vs_langgraph.py` | 与 LangGraph 子图对照 |
| 08 | `08_stage4_final.py` | **综合**：调研 Agent + 汇总 Agent |

详见 [stage-4.md](stage-4.md)。

---

## 阶段五 & 六（P5–P6 · 专业示范）

P5 公司统一后端 MVP、P6 部署运维 → 见 [`showcase/`](showcase/README.md) 四个可运行小项目。

| 示范 | 对应 | 要点 |
|------|------|------|
| `01_custom_tool_audit/` | P1 | 只读 Tool + 审计 Hook |
| `02_company_skills/` | P2 | ≥3 个 SKILL.md |
| `03_mcp_readonly_server/` | P2–P3 | stdio MCP 只读查询 |
| `04_gateway_webhook/` | P4–P5 | FastAPI Webhook + stream 模拟 |

---

## 推荐学习顺序

```
python/stage-1~2 或 langchain/stage-1
        ↓
openharness/stage-1 → stage-2 → stage-3 → stage-4
        ↓
openharness/showcase/（专业示范）
        ↓
../../base/openharness/p5~p6（公司 MVP 与部署）
```

---

## 推荐资源

| 资源 | 链接 |
|------|------|
| 官方仓库 | https://github.com/HKUDS/OpenHarness |
| 安装 | `pip install openharness-ai` / `uv sync --group openharness-stage-1` |
| 架构笔记 | [notes/harness-architecture.md](notes/harness-architecture.md) |
| 与 LangChain 对照 | [notes/harness-vs-langchain.md](notes/harness-vs-langchain.md) |
