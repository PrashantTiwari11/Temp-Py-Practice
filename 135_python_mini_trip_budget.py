# 135 - Mini Trip Budget Planner: 10 practical features
budget = 25000.0
expenses = [
    {"category": "Transport", "description": "Train tickets", "amount": 4200.0},
    {"category": "Stay", "description": "Hotel deposit", "amount": 6000.0},
    {"category": "Food", "description": "Meals", "amount": 1800.0},
    {"category": "Activities", "description": "Museum tickets", "amount": 900.0},
]

# 1. Show expenses
def show_expenses():
    for e in expenses:
        print(f"{e['category']}: {e['description']} — ₹{e['amount']:.2f}")

# 2. Total spending
def total_spending():
    return sum(e["amount"] for e in expenses)

# 3. Remaining budget
def remaining_budget():
    return budget - total_spending()

# 4. Totals grouped by category
def spending_by_category():
    totals = {}
    for e in expenses:
        totals[e["category"]] = totals.get(e["category"], 0) + e["amount"]
    return totals

# 5. Largest expense
def largest_expense():
    return max(expenses, key=lambda e: e["amount"], default=None)

# 6. Add an expense
def add_expense(category, description, amount):
    if amount < 0:
        raise ValueError("Amount cannot be negative.")
    expenses.append({"category": category, "description": description, "amount": float(amount)})

# 7. Check budget status
def is_over_budget():
    return total_spending() > budget

# 8. Budget usage percentage
def budget_used_percent():
    return round(total_spending() / budget * 100, 2) if budget > 0 else 0

# 9. Find expensive items
def expensive_items(threshold=2000):
    return [e for e in expenses if e["amount"] > threshold]

# 10. Summary report
def report():
    show_expenses()
    print(f"Total: ₹{total_spending():.2f}")
    print(f"Remaining: ₹{remaining_budget():.2f}")
    print("Budget used:", budget_used_percent(), "%")
    print("Over budget:", is_over_budget())
    print("By category:", spending_by_category())

if __name__ == "__main__":
    print("TRIP BUDGET REPORT")
    report()
