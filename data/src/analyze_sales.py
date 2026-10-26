import csv
from collections import defaultdict
from pathlib import Path

DATA_FILE = Path(file).resolve().parent.parent / "data" / "sales_data.csv"

def load_sales(file_path=DATA_FILE):
"""Load sales records from a CSV file."""
with open(file_path, "r", newline="", encoding="utf-8") as file:
reader = csv.DictReader(file)
required_columns = {
"order_id", "date", "product", "category",
"quantity", "unit_price", "region"
}

    if not reader.fieldnames or not required_columns.issubset(reader.fieldnames):
        raise ValueError("Sales CSV is missing required columns.")

    sales = []
    for row in reader:
        quantity = int(row["quantity"])
        unit_price = float(row["unit_price"])

        if quantity <= 0 or unit_price < 0:
            raise ValueError("Quantity must be positive and price cannot be negative.")

        row["quantity"] = quantity
        row["unit_price"] = unit_price
        row["revenue"] = quantity * unit_price
        sales.append(row)

    return sales

def summarize_sales(sales):
"""Calculate revenue by product and region."""
total_revenue = sum(row["revenue"] for row in sales)
product_revenue = defaultdict(float)
region_revenue = defaultdict(float)

for row in sales:
    product_revenue[row["product"]] += row["revenue"]
    region_revenue[row["region"]] += row["revenue"]

return {
    "total_orders": len(sales),
    "total_revenue": round(total_revenue, 2),
    "product_revenue": dict(sorted(product_revenue.items())),
    "region_revenue": dict(sorted(region_revenue.items())),
}

def main():
sales = load_sales()
summary = summarize_sales(sales)

print("SALES ANALYSIS REPORT")
print("=" * 30)
print(f"Total orders: {summary['total_orders']}")
print(f"Total revenue: ${summary['total_revenue']:,.2f}")

print("\nRevenue by product:")
for product, revenue in sorted(
    summary["product_revenue"].items(),
    key=lambda item: item[1],
    reverse=True,
):
    print(f"  {product}: ${revenue:,.2f}")

print("\nRevenue by region:")
for region, revenue in summary["region_revenue"].items():
    print(f"  {region}: ${revenue:,.2f}")

if name == "main":
main()
