# CopilotKit + A2UI · Agent 客户端学习计划

> **CopilotKit v2** + **Next.js App Router** + **AG-UI / A2UI**  
> 延伸：[`../../base/copilotkit-a2ui/`](../../base/copilotkit-a2ui/)（12 周完整课表）

面向 **React/TS** 开发者，构建生产级 Agent 客户端（Generative UI、共享状态、HITL）。

**依赖管理**：本轨道在 `copilotkit/` 目录内使用 **pnpm** + `package.json`（Node 轨道自治，不用根目录 uv）。

---

## 能力画像

| 维度 | 完成标准 |
|------|----------|
| Runtime | Next `route.ts` + `createCopilotRuntimeHandler` + BuiltInAgent |
| 客户端原语 | useAgentContext、Frontend Tool、Interrupt |
| A2UI | Surface 消息流、Fixed Schema、Catalog 白名单 |
| 后端对接 | LangGraphAgent、JWT onRequest |
| 生产 | 鉴权、降级、a11y、部署 checklist |

---

## 阶段总览（7 阶段，可灵活增删）

| 阶段 | 目录 | 主题 | 对应 base |
|------|------|------|-----------|
| 一 | `stage-01/` | CopilotKit v2 + Runtime + 安全 | P0 |
| 二 | `stage-02/` | Agent Context、Frontend Tool | P1 |
| 三 | `stage-03/` | Interrupt、Generative UI 选型 | P1 |
| 四 | `stage-04/` | A2UI 协议、Fixed Schema、Catalog 安全 | P2 |
| 五 | `stage-05/` | 自定义 Catalog、Fixed vs Dynamic | P3 |
| 六 | `stage-06/` | LangGraph、鉴权、错误降级 | P4 |
| 七 | `stage-07/` | 部署、a11y、MVP checklist | P5 |

每阶段含 **编号 TypeScript 练习**（`tsx` 可运行）+ **stage-N.md** 指南。  
完整 Next.js 应用见 **showcase/**。

---

## 快速开始

```bash
cd learn/copilotkit
pnpm install

# 阶段一
pnpm run stage:01
npx tsx stage-01/06_stage01_final.ts

# 专业示范（Next.js）
cd showcase/01-runtime-starter
pnpm install
cp ../../.env.example .env.local
pnpm dev
```

---

## 练习脚本索引（stage-01 示例）

| 编号 | 文件 | 内容 |
|------|------|------|
| 01 | `01_stack_overview.ts` | 协议栈 |
| 02 | `02_runtime_config.ts` | Runtime 配置 |
| 03 | `03_env_security_audit.ts` | 环境变量审计 |
| 04 | `04_ag_ui_event_parser.ts` | AG-UI 事件 |
| 05 | `05_single_route_mode.ts` | 同源部署 |
| 06 | `06_stage01_final.ts` | **综合** |

其他阶段见各 `stage-N.md`。

---

## 专业示范

| 目录 | 说明 |
|------|------|
| [showcase/01-runtime-starter](showcase/01-runtime-starter/) | Provider + Runtime + CopilotChat |
| [showcase/02-ag-ui-tools](showcase/02-ag-ui-tools/) | Context + Frontend Tool + Interrupt |
| [showcase/03-a2ui-catalog](showcase/03-a2ui-catalog/) | 公司 Catalog + Fixed Schema |

---

## 推荐学习顺序

```
react/TS 基础（或外部 reactjs 轨）
        ↓
copilotkit/stage-01 → … → stage-07
        ↓
showcase/ 三个示范
        ↓
langchain/stage-2 + base/copilotkit-a2ui P4 LangGraph 联调
        ↓
base/copilotkit-a2ui/p5 公司 Agent UI MVP
```

---

## 与兄弟轨道

| 轨道 | 分工 |
|------|------|
| `langchain/` | LangGraph 业务图、Tool、RAG |
| `openharness/` | CLI/Gateway/IM、Harness 治理 |
| **copilotkit/** | Web Agent UX、A2UI Catalog |

---

## 资源

| 资源 | 链接 |
|------|------|
| 官方文档 | https://docs.copilotkit.ai |
| 仓库 | https://github.com/CopilotKit/CopilotKit |
| A2UI | https://a2ui.org |
| 本仓库笔记 | [notes/](notes/) |
