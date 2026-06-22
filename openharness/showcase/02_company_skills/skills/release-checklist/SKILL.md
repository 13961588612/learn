---
name: release-checklist
description: Pre-release verification checklist for staging to production.
---

# Release Checklist

## When to use
- Before merging release branch
- Before prod deploy window (Tue/Thu 20:00-22:00)

## Steps
1. CI green on release branch
2. Staging smoke test passed
3. DB migration reviewed (if any)
4. Rollback plan documented
5. On-call notified

## Do NOT
- Skip staging for "hotfix" without EM approval
