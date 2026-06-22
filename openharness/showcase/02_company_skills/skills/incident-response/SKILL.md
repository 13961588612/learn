---
name: incident-response
description: Use when handling production incidents. Step-by-step runbook.
---

# Incident Response

## When to use
- P0/P1 alert fired
- User reports widespread outage

## Steps
1. 确认影响范围与开始时间
2. 拉 war room，指定 incident commander
3. 若需 rollback，按 release-checklist 执行
4. 记录 timeline，事后 blameless postmortem

## Do NOT
- 未经审批重启生产核心服务
- 在公开频道讨论未脱敏客户数据
