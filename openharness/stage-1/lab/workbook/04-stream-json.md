# 实验 4：非交互 stream-json

## 命令

```bash
openh -p "List three files in the current directory" --output-format stream-json
```

辅助：`uv run python scripts/03_run_stream_json.py`

## 观察题

1. 输出中是否出现 `tool_use` 或 `content_block_delta` 类事件？
2. 与 `--output-format json` 相比，stream-json 适合什么集成场景？

## 验收

- [ ] 保存一份 stream-json 原始输出到 experiments/
