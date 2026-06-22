# 实验 6：Engine 源码阅读

## 步骤

1. 克隆或浏览 [OpenHarness engine/](https://github.com/HKUDS/OpenHarness/tree/main/openharness/engine)
2. 找到 Agent Loop：`while` + `tool_use` + execute
3. 对照 [notes/harness-architecture.md](../../notes/harness-architecture.md)

## 观察题

1. stop_reason 为 tool_use 时 Harness 做什么？
2. Permission 检查在 execute 之前还是之后？
3. 用三句话费曼解释「模型想、Harness 做」

## 验收

- [ ] experiments/06-engine-sketch.md 含手绘循环伪代码
