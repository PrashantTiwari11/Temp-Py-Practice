# 111_python_mini_expense_report.py
# Mini Expense Report - 10 practical features

expenses = [
    {"title": "Lunch", "category": "Food", "amount": 180},
    {"title": "Bus", "category": "Travel", "amount": 50},
    {"title": "Notebook", "category": "Study", "amount": 120},
    {"title": "Dinner", "category": "Food", "amount": 250},
    {"title": "Auto", "category": "Travel", "amount": 100},
]

# 1. Display expenses
print("1. Expenses:", expenses)

# 2. Count expenses
print("2. Expense count:", len(expenses))

# 3. Total spending
total = sum(e["amount"] for e in expenses)
print("3. Total:", total)

# 4. Average expense
print("4. Average:", round(total / len(expenses), 2))

# 5. Highest expense
print("5. Highest:", max(expenses, key=lambda e: e["amount"]))

# 6. Lowest expense
print("6. Lowest:", min(expenses, key=lambda e: e["amount"]))

# 7. Category totals
category_totals = {}
for e in expenses:
    category_totals[e["category"]] = category_totals.get(e["category"], 0) + e["amount"]
print("7. Category totals:", category_totals)

# 8. Food expenses
print("8. Food:", [e for e in expenses if e["category"] == "Food"])

# 9. Expenses above 100
print("9. Above 100:", [e for e in expenses if e["amount"] > 100])

# 10. Budget check
budget = 700
print("10. Budget:", {
    "budget": budget,
    "spent": total,
    "remaining": budget - total,
    "within_budget": total <= budget
})
