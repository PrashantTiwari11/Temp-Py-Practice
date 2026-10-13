"""Mini Sales Dashboard: 10 features."""
from datetime import date
import csv

sales = []
def add_sale(product, units, unit_price, day=None):  # 1
    if units <= 0 or unit_price < 0:
        raise ValueError("Units must be positive and price non-negative.")
    s = {"product": product, "units": int(units), "unit_price": float(unit_price),
         "date": day or date.today().isoformat()}
    s["revenue"] = s["units"] * s["unit_price"]
    sales.append(s)
    return s
def list_sales():  # 2
    return sorted(sales, key=lambda s: s["date"])
def total_revenue():  # 3
    return sum(s["revenue"] for s in sales)
def total_units():  # 4
    return sum(s["units"] for s in sales)
def filter_by_product(product):  # 5
    return [s for s in sales if s["product"].casefold() == product.casefold()]
def filter_by_date(day):  # 6
    return [s for s in sales if s["date"] == day]
def revenue_by_product():  # 7
    result = {}
    for s in sales:
        result[s["product"]] = result.get(s["product"], 0.0) + s["revenue"]
    return result
def best_selling_product():  # 8
    units = {}
    for s in sales:
        units[s["product"]] = units.get(s["product"], 0) + s["units"]
    return max(units, key=units.get) if units else None
def average_sale_value():  # 9
    return total_revenue() / len(sales) if sales else 0.0
def export_csv(filename="sales_report.csv"):  # 10
    with open(filename, "w", newline="", encoding="utf-8") as f:
        fields = ["product", "units", "unit_price", "date", "revenue"]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(list_sales())
    return filename

if __name__ == "__main__":
    add_sale("Notebook", 12, 45)
    add_sale("Pen", 30, 10)
    add_sale("Notebook", 8, 45)
    print("Revenue:", f"₹{total_revenue():,.2f}")
    print("Units:", total_units())
    print("Revenue by product:", revenue_by_product())
    print("Best seller:", best_selling_product())
