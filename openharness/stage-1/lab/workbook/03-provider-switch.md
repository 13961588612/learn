# 实验 3：Provider profile 切换

## 步骤

1. 在 setup 或配置文件中准备 **2 个** profile（如 openai-dev / company-gateway）
2. 切换：`openh provider use <name>`（以官方文档为准）
3. 同一 prompt 跑两次，确认后端切换：

```bash
openh -p "Say which model you are" --output-format json
```

## 观察题

1. 两个 profile 的 model 字段分别是什么？
2. 切换 profile 是否需要改业务 prompt？

## 验收

- [ ] 成功切换并各跑通一次非交互 prompt
