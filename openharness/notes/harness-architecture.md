# Harness 架构速查

> 对照 [OpenHarness 源码](https://github.com/HKUDS/OpenHarness) 与 [`../../base/openharness/notes/harness-architecture-map.md`](../../base/openharness/notes/harness-architecture-map.md)

## 四层架构

1. **能力层**：`tools/`、`skills/`
2. **安全层**：`permissions/`、`hooks/`
3. **协作扩展层**：`mcp/`、`plugins/`、`coordinator/`、`tasks/`
4. **基础设施层**：`engine/`、`config/`、`memory/`、`prompts/`、`ui/`

## Agent Loop（核心）

```
while 模型返回 tool_use:
    对每个 tool_call:
        permission 检查 → pre_hook → 执行 → post_hook → 追加结果到 messages
```

**费曼三句话**：

1. Engine 把 messages + tools 发给模型，直到不再请求 Tool。
2. Tool Registry 负责校验、权限、执行、回写上下文。
3. 与 LangChain 不同：OpenHarness 是**运行时壳**，扩展通过 Tool/Skill/Plugin/MCP 挂载。

## 公司后端关注点

| 子系统 | 公司用法 |
|--------|----------|
| tools | 禁用危险内置 Tool，加域只读 Tool |
| skills | 流程 Runbook、发布规范 |
| hooks | **审计日志**主挂载点 |
| mcp | **内部系统**主接入方式 |
| permissions | 生产 default + path_rules |
| coordinator | 复杂工单多 Agent 分工 |
