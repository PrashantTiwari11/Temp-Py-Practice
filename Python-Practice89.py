# 84_python_mini_expense_tracker.py
# Mini Expense Tracker Project - 10 practical features

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add(self, title, amount, category):
        self.expenses.append({
            "title": title, "amount": amount, "category": category
        })

    def show(self):
        for expense in self.expenses:
            print(expense)

    def total(self):
        return sum(e["amount"] for e in self.expenses)

    def category_total(self, category):
        return sum(
            e["amount"] for e in self.expenses
            if e["category"].lower() == category.lower()
        )

    def search(self, keyword):
        return [
            e for e in self.expenses
            if keyword.lower() in e["title"].lower()
        ]

    def highest(self):
        return max(self.expenses, key=lambda e: e["amount"], default=None)

    def lowest(self):
        return min(self.expenses, key=lambda e: e["amount"], default=None)

    def count(self):
        return len(self.expenses)

    def average(self):
        return self.total() / self.count() if self.expenses else 0

    def budget_status(self, budget):
        spent = self.total()
        return {
            "budget": budget,
            "spent": spent,
            "remaining": budget - spent,
            "within_budget": spent <= budget
        }

tracker = ExpenseTracker()
tracker.add("Lunch", 180, "Food")
tracker.add("Bus", 50, "Travel")
tracker.add("Book", 450, "Education")
tracker.add("Dinner", 250, "Food")
tracker.add("Internet", 700, "Bills")

print("1. All expenses:")
tracker.show()

print("2. Total spending:", tracker.total())
print("3. Food total:", tracker.category_total("Food"))
print("4. Search 'book':", tracker.search("book"))
print("5. Highest expense:", tracker.highest())
print("6. Lowest expense:", tracker.lowest())
print("7. Expense count:", tracker.count())
print("8. Average expense:", tracker.average())
print("9. Budget status:", tracker.budget_status(2000))
print("10. Tracker project completed.")
