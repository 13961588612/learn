"""
09_stage1_final.py - 综合：读 CSV → 聚合统计 → 写 JSON 报告

学习要点:
1. 组合 pathlib、csv、json 完成小数据处理流水线
2. 按 category 汇总数量与金额
3. 将结果写入 data/report.json
"""

import csv
import json
from collections import defaultdict
from pathlib import Path


def load_orders(csv_path: Path) -> list[dict]:
    with csv_path.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def aggregate(orders: list[dict]) -> dict:
    stats: dict[str, dict] = defaultdict(lambda: {"quantity": 0, "amount": 0.0})

    for row in orders:
        cat = row["category"]
        qty = int(row["quantity"])
        price = float(row["unit_price"])
        stats[cat]["quantity"] += qty
        stats[cat]["amount"] += qty * price

    total_qty = sum(s["quantity"] for s in stats.values())
    total_amount = sum(s["amount"] for s in stats.values())

    return {
        "by_category": dict(stats),
        "total_quantity": total_qty,
        "total_amount": round(total_amount, 2),
    }


def main():
    print("=" * 50)
    print("09 - Stage 1 Final")
    print("=" * 50)

    base = Path(__file__).parent
    csv_path = base / "data" / "orders.csv"
    report_path = base / "data" / "report.json"

    orders = load_orders(csv_path)
    print(f"\n读取 {len(orders)} 条订单")

    report = aggregate(orders)
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")

    print("\n按类别汇总:")
    for cat, info in report["by_category"].items():
        print(f"  {cat}: 数量={info['quantity']}, 金额={info['amount']:.2f}")

    print(f"\n总计: 数量={report['total_quantity']}, 金额={report['total_amount']}")
    print(f"\n报告已写入: {report_path}")
    print("\n[OK] 阶段一综合练习完成")


if __name__ == "__main__":
    main()
