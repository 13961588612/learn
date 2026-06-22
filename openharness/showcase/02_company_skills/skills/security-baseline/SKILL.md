---
name: security-baseline
description: Company security rules for agent tool use and code changes.
---

# Security Baseline

## When to use
- Agent 请求执行写操作或访问敏感路径
- Code review 安全项核对

## Rules
1. 禁止 `.env`、密钥、token 写入仓库
2. MCP Tool 默认只读
3. Bash/WebFetch 生产环境禁用
4. 审计日志保留 90 天

## Do NOT
- 将 API Key 粘贴到 prompt 或 SKILL.md
