# 10 · Gateway 与程序化 API

[← 返回 Lab 总入口](../README.md)

---

## 10.1 架构分层

```
IM / Web / 内部服务
        ↓ HTTP Webhook / REST
   Gateway（ohmo / 自研 FastAPI）  ← 无状态，鉴权，路由 channel
        ↓ spawn / 连接池
   OpenHarness 进程（openh -p / stream-json）
        ↓
   Tools / Skills / MCP
```

**原则**：Gateway 与 Harness **分离**；session 存 Postgres/Redis；stream 解析与 IM 适配分开。

---

## 10.2 非交互 API（最小集成）

同步 JSON：

```bash
openh -p "用户问题" --output-format json
```

流式：

```bash
openh -p "用户问题" --output-format stream-json
```

lab 脚本：

```bash
uv run python openharness/stage-5/lab/scripts/01_noninteractive_json.py
uv run python openharness/stage-5/lab/scripts/02_gateway_help_probe.py
```

REST 封装思路：用 subprocess 或 SDK 调 `openh`，HTTP 层只负责 auth + 转发。

---

## 10.3 Gateway / ohmo 探测

```bash
openh gateway --help
# 或独立安装的 ohmo 子命令 — 以本机 --help 为准
```

记录到 `stage-5/lab/experiments/`：

- 支持的 channel 类型
- 配置文件路径
- 与 profile 的关系

---

## 10.4 Webhook 示范

本仓库 FastAPI demo：

```
learn/openharness/showcase/04_gateway_webhook/
```

```bash
cd learn
uv sync --group openharness-showcase
uv run uvicorn openharness.showcase.04_gateway_webhook.app.main:app --reload
# 或按 showcase README 启动
curl -X POST http://127.0.0.1:8000/webhook -H "Content-Type: application/json" -d '{"text":"hello"}'
```

---

## 10.5 会话 resume

同一 **thread / session id** 第二次请求应能接续上下文（取决于 Gateway 持久化实现）。

实验：

1. 非交互或 TUI 中完成一轮对话
2. 记录 thread id（若 json 输出提供）
3. 带 id 发第二次请求，确认 Agent 记得上文

stage-5 lab README 第 5 项。

---

## 10.6 鉴权（公司 MVP）

Gateway 层常见：

- JWT `onRequest` 校验
- channel → tenant → profile 映射
- 审计字段：`user_id`, `channel`, `trace_id`

与 stage-6 公司平台 lab 联调。

---

## 10.7 对应实验

- [stage-5/lab/README.md](../../stage-5/lab/README.md)
- [showcase/04_gateway_webhook](../../showcase/04_gateway_webhook/README.md)
- base：[p4-gateway-backend](../../../../base/openharness/p4-gateway-backend/README.md)
- 故障：[99-故障排查索引.md](99-故障排查索引.md) → 「Webhook 不通」「JSON 解析失败」
