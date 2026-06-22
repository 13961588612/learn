# 03-a2ui-catalog · 自定义 Catalog + Fixed Schema

对应 **stage-04~05 / P2–P3**。

## 文件

- `catalog/companyCatalog.ts` — Catalog 与 Fixed Surface 模板

## 集成

```tsx
// layout.tsx
<CopilotKit runtimeUrl="/api/copilotkit" /* a2ui catalog prop 见官方 v2 文档 */>
```

```ts
// route.ts — 生产
a2ui: { injectA2UITool: false }
```

## 验收

- [ ] >=3 个公司组件在 Catalog 中
- [ ] Fixed Schema 流式渲染 demo
- [ ] Catalog 白名单无任意 HTML

## 参考

[`../../base/copilotkit-a2ui/p3-a2ui-catalog`](../../../base/copilotkit-a2ui/p3-a2ui-catalog)
