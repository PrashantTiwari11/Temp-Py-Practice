"""150 Expense Splitter: 10 practical features."""
from collections import defaultdict
expenses = []
def add_expense(payer, amount, description):
    if amount < 0: raise ValueError("Amount cannot be negative")
    expenses.append({"payer": payer, "amount": round(amount, 2), "description": description})
def total(): return round(sum(e["amount"] for e in expenses), 2)
def people(): return sorted({e["payer"] for e in expenses})
def paid_totals():
    result = defaultdict(float)
    for e in expenses: result[e["payer"]] += e["amount"]
    return {k: round(v, 2) for k, v in result.items()}
def equal_share(): return round(total()/len(people()), 2) if people() else 0
def balances():
    paid = paid_totals()
    return {name: round(paid.get(name, 0)-equal_share(), 2) for name in people()}
def by_person(name): return [e for e in expenses if e["payer"].lower() == name.lower()]
def largest(): return max(expenses, key=lambda e: e["amount"], default=None)
def summary(): return {"total": total(), "share": equal_share(), "paid": paid_totals(), "balances": balances()}
def export_csv(path="shared_expenses.csv"):
    import csv
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["payer", "amount", "description"]); w.writeheader(); w.writerows(expenses)
if __name__ == "__main__":
    add_expense("Asha", 600, "Groceries"); add_expense("Ravi", 300, "Taxi"); add_expense("Asha", 150, "Snacks")
    print("1 Sample expenses:", expenses)
    print("2 Total:", total())
    print("3 People:", people())
    print("4 Paid totals:", paid_totals())
    print("5 Equal share:", equal_share())
    print("6 Balances:", balances())
    print("7 Asha's expenses:", by_person("Asha"))
    print("8 Largest expense:", largest())
    print("9 Summary:", summary())
    print("10 Export CSV with export_csv()")
