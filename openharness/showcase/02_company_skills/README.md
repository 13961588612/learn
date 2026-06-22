# 02_company_skills · 公司 Skills 库

对应 **P2** · [`../../base/openharness/p2-company-skills`](../../base/openharness/p2-company-skills)

## 安装到 Harness

```bash
mkdir -p ~/.openharness/skills
cp -r skills/* ~/.openharness/skills/

# 或项目级
mkdir -p .openharness/skills
cp -r skills/* .openharness/skills/
```

## Skills

| 目录 | 用途 |
|------|------|
| `incident-response/` | P0/P1 故障响应 |
| `release-checklist/` | 发布前检查 |
| `security-baseline/` | 安全基线 |

## 验证

```bash
uv run python openharness/stage-2/07_skills_loader.py
```
