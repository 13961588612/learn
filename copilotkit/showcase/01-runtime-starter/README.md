# 01-runtime-starter · CopilotKit + Next.js 最小示范

对应 **stage-01 / P0**。

## 运行

```bash
cd learn/copilotkit/showcase/01-runtime-starter
pnpm install
cp ../../.env.example .env.local   # 填入 OPENAI_API_KEY
pnpm dev
```

浏览器打开 http://localhost:3001 ，使用 Copilot 侧边栏。

## 文件

| 文件 | 职责 |
|------|------|
| `app/layout.tsx` | CopilotKit Provider + Sidebar |
| `app/api/copilotkit/route.ts` | Runtime 端点（密钥仅服务端） |
| `app/page.tsx` | 业务页占位 |

## 验收

- [ ] 本地多轮对话 + 流式输出
- [ ] 能说明 route.ts vs layout.tsx 分工
- [ ] 客户端 bundle 无 API Key

## 下一步

[02-ag-ui-tools](../02-ag-ui-tools/)
