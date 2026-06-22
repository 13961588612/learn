# 5 · Provider 与 Profile

[← 返回 Lab 总入口](../README.md)

---

## 5.1 概念

- **Provider**：后端类型（OpenAI、Anthropic、OpenAI-compatible Gateway…）
- **Profile**：命名的一套连接参数（base_url、model、api_key、label）
- **环境边界**：dev / staging / prod **必须分 profile**，禁止共用一个 Key

---

## 5.2 添加公司 Gateway profile（示例）

```bash
oh provider add company-prod \
  --label "Company Prod GW" \
  --provider openai \
  --api-format openai \
  --base-url https://llm-gateway.company.com/v1 \
  --model company-default
```

Windows PowerShell 用 `openh` 替换 `oh`，长命令可分行。

本地 OpenAI 官方：

```bash
openh setup
# 或编辑 ~/.openharness/profiles/ 下对应 json
```

---

## 5.3 切换 profile

```bash
openh provider list
openh provider use dev
openh provider use company-prod
```

验证切换（同一 prompt，看 model 字段变化）：

```bash
openh -p "Say which model you are" --output-format json
```

---

## 5.4 实验：双 profile 对比

| 步骤 | profile A | profile B |
|------|-----------|-----------|
| 1 | `provider use openai-dev` | — |
| 2 | 跑 `-p "Say which model"` | 记录 JSON 中 model |
| 3 | — | `provider use company-gw` |
| 4 | — | 再跑同 prompt，对比 model / base_url 行为 |

观察题见 [stage-1/lab/workbook/03-provider-switch.md](../../stage-1/lab/workbook/03-provider-switch.md)。

---

## 5.5 凭证安全

| 做法 | 说明 |
|------|------|
| profile-scoped key | 每个 profile 独立密钥 |
| 不进 Git | `.env` 仅本地；生产用 K8s Secret |
| CI | 用 `--dry-run` 验证 profile 可读，真实 key 用 CI Secret |

---

## 5.6 故障速查

| 现象 | 检查 |
|------|------|
| 401 / invalid key | 当前 profile 的 key、base_url |
| 404 model | profile 中 model 名与 Gateway 是否一致 |
| 切换无效 | 是否在同一 shell；非交互是否指定 `--profile`（若 CLI 支持） |
| 超时 | 公司 Gateway 网络 / VPN |

更多：[99-故障排查索引.md](99-故障排查索引.md) → 「API 调用失败」

---

## 5.7 对应实验

- stage-1 workbook 03
- base：[openharness-best-practices.md §1](../../../../base/openharness/notes/openharness-best-practices.md)
