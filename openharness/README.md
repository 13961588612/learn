# OpenHarness 公司 Agent 后端学习计划

> **OpenHarness**（`oh` / Windows **`openh`**）开源 Agent Harness 运行时。  
> 本轨道 = **概念脚本**（Python 模拟）+ **Lab 实操**（真实 CLI/TUI）+ **Showcase**（工程示范）。

**延伸**：[`../../base/openharness/`](../../base/openharness/)（14 周 · P0–P6）  
**Lab 总说明**：[`notes/cli-lab-guide.md`](notes/cli-lab-guide.md)  
**实操手册（查阅 / 排错）**：[`lab/README.md`](lab/README.md) · [故障排查索引](lab/manual/99-故障排查索引.md)

---

## 为什么 7 个阶段？

原 4  stage 将 P3–P6 压缩过多，且 **缺少 OpenHarness 本体使用练习**。现与 base 课表对齐：

| Stage | base | 概念脚本 | **Lab 实操** |
|-------|------|----------|--------------|
| **1** | P0 | Agent Loop、dry-run 模拟 | 安装、setup、dry-run、profile、stream-json、TUI |
| **2** | P1 | Tool/Skill/Hook 编程 | `/skills`、权限、Plan、安装 Skills |
| **3** | P2 | MCP/Plugin 结构 | MCP 配置、dry-run、plugin enable |
| **4** | P3 | Multi-Agent/Memory 模拟 | MEMORY.md、Task、max-turns |
| **5** | P4 | Gateway/会话路由 | 非交互 JSON、ohmo 探测、Webhook demo |
| **6** | P5 | 公司平台布局/审计 | docker compose、联调 checklist |
| **7** | P6 | 健康检查/故障树 | 发布 checklist、运维手册 |

---

## 学习路径（双轨）

```
每个 Stage:
  01~N 概念脚本  →  lab/ _workbook + scripts_  →  （可选）showcase/
```

```bash
# 安装 CLI（一次性）
cd learn
uv sync --group openharness-cli

# Stage 1 示例
uv run python openharness/stage-1/01_harness_concepts.py
cd openharness/stage-1/lab
uv run python scripts/01_check_install.py
openh setup
# 按 lab/workbook/*.md 完成观察题
```

---

## Stage 1 · P0 Harness 心智模型

| 类型 | 路径 |
|------|------|
| 指南 | [stage-1.md](stage-1.md) |
| 概念 | `stage-1/01` ~ `10` |
| **Lab** | [stage-1/lab/](stage-1/lab/README.md)（6 个 workbook + 3 脚本） |

---

## Stage 2 · P1 Tools + Skills + Permissions

| 类型 | 路径 |
|------|------|
| 指南 | [stage-2.md](stage-2.md) |
| 概念 | `stage-2/01` ~ `10` |
| **Lab** | [stage-2/lab/](stage-2/lab/README.md) |
| Showcase | [showcase/01_custom_tool_audit](showcase/01_custom_tool_audit/) · [02_company_skills](showcase/02_company_skills/) |

---

## Stage 3 · P2 MCP + Plugins

| 类型 | 路径 |
|------|------|
| 指南 | [stage-3.md](stage-3.md) |
| 概念 | `stage-3/01` ~ `08` |
| **Lab** | [stage-3/lab/](stage-3/lab/README.md) |
| Showcase | [showcase/03_mcp_readonly_server](showcase/03_mcp_readonly_server/) |

---

## Stage 4 · P3 Multi-Agent + Memory + Tasks

| 类型 | 路径 |
|------|------|
| 指南 | [stage-4.md](stage-4.md) |
| 概念 | `stage-4/01` ~ `08` |
| **Lab** | [stage-4/lab/](stage-4/lab/README.md) |

---

## Stage 5 · P4 Gateway + 程序化 API

| 类型 | 路径 |
|------|------|
| 指南 | [stage-5.md](stage-5.md) |
| 概念 | `stage-5/01` ~ `04` |
| **Lab** | [stage-5/lab/](stage-5/lab/README.md) |
| Showcase | [showcase/04_gateway_webhook](showcase/04_gateway_webhook/) |

---

## Stage 6 · P5 公司统一后端 MVP

| 类型 | 路径 |
|------|------|
| 指南 | [stage-6.md](stage-6.md) |
| 概念 | `stage-6/01` ~ `04` |
| **Lab** | [stage-6/lab/](stage-6/lab/README.md) |

---

## Stage 7 · P6 部署与运维

| 类型 | 路径 |
|------|------|
| 指南 | [stage-7.md](stage-7.md) |
| 概念 | `stage-7/01` ~ `03` |
| **Lab** | [stage-7/lab/](stage-7/lab/README.md) |

---

## 依赖组（uv）

| 组 | 用途 |
|----|------|
| `openharness-cli` | 含 `openharness-ai`，Lab 必需 |
| `openharness-stage-2` ~ `4` | pydantic 等概念脚本 |
| `openharness-showcase` | Gateway FastAPI demo |

---

## 推荐顺序

```
python 或 langchain 基础
  → openharness stage-1（概念+lab）→ … → stage-7
  → base/openharness p5~p6 公司 MVP
```

与 `langchain/`（业务图）、`copilotkit/`（Web 客户端）互补。
