# Stage-5 Lab · P4 Gateway + 程序化 API 实操

> **查阅手册**：[10-Gateway与程序化API](../../lab/manual/10-Gateway与程序化API.md) · [06-输出格式](../../lab/manual/06-输出格式与集成.md) · [故障排查](../../lab/manual/99-故障排查索引.md)

## 实验

| # | 内容 |
|---|------|
| 1 | 非交互 API：`-p "..." --output-format json` 封装为内部 REST 契约 |
| 2 | stream-json 管道：lab 脚本保存 NDJSON，写解析器 |
| 3 | ohmo（若已安装）：`gateway` 子命令探索，记录 channel 配置 |
| 4 | 运行 [showcase/04_gateway_webhook](../../showcase/04_gateway_webhook/)，POST Webhook 模拟 IM |
| 5 | 会话 resume：同 thread 第二次请求能接续 |

## 脚本

```bash
uv run python scripts/01_noninteractive_json.py
uv run python scripts/02_gateway_help_probe.py
```

## 验收

- [ ] 非 TUI 客户端能收流式/JSON 响应
- [ ] Webhook demo 可 curl 通
- [ ] 文档说明 channel 级配置
