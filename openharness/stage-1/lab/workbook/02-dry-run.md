# 实验 2：dry-run 解读

## 命令

```bash
openh --dry-run
openh --dry-run -p "Explain this repository" --output-format json
```

辅助脚本：`uv run python scripts/02_run_dry_run.py`

## 观察题

1. readiness 是 ready / warning / blocked 哪一种？
2. 若为 blocked，列出所有 next actions
3. json 输出里有哪些顶层字段？

## 验收

- [ ] 能向他人解释「dry-run 不调用模型、不执行 Tool」
