# Day 9 - 36: Mini Project - Expense Tracker

expenses = []

# 1. Add expense
def add_expense(category, amount, note=""):
    expenses.append({"category": category, "amount": float(amount), "note": note})

# 2. Display expenses
def show_expenses():
    for i, item in enumerate(expenses, 1):
        print(f"{i}. {item['category']} - Rs.{item['amount']:.2f} - {item['note']}")

# 3. Total expenses
def total():
    return sum(x["amount"] for x in expenses)

# 4. Category total
def category_total(category):
    return sum(x["amount"] for x in expenses if x["category"].lower() == category.lower())

# 5. Largest expense
def largest():
    return max(expenses, key=lambda x: x["amount"]) if expenses else None

# 6. Average expense
def average():
    return total()/len(expenses) if expenses else 0

# 7. Delete expense
def delete(index):
    return expenses.pop(index) if 0 <= index < len(expenses) else None

# 8. Filter expensive items
def above(amount):
    return [x for x in expenses if x["amount"] > amount]

# 9. Sort by amount
def sorted_expenses():
    return sorted(expenses, key=lambda x: x["amount"], reverse=True)

# 10. Generate summary
def summary():
    categories = {}
    for x in expenses:
        categories[x["category"]] = categories.get(x["category"], 0) + x["amount"]
    print("Total:", total())
    print("Average:", average())
    print("Categories:", categories)

if __name__ == "__main__":
    add_expense("Food", 250, "Lunch")
    add_expense("Travel", 120, "Metro")
    add_expense("Food", 180, "Dinner")
    add_expense("Shopping", 850, "Clothes")
    add_expense("Travel", 60, "Bus")
    show_expenses()
    print("Total:", total())
    print("Food:", category_total("Food"))
    print("Largest:", largest())
    print("Above 200:", above(200))
    print("Sorted:", sorted_expenses())
    summary()
