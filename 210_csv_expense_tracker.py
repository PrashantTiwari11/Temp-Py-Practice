"""210 - CSV Expense Tracker; saves entries in expenses.csv."""
import csv
from datetime import date
from pathlib import Path

FILE = Path("expenses.csv")
FIELDS = ["date", "category", "description", "amount"]

def add_expense():
    category = input("Category: ").strip()
    description = input("Description: ").strip()
    try:
        amount = float(input("Amount in rupees: ").strip())
        if amount < 0:
            raise ValueError
    except ValueError:
        print("Enter a valid non-negative amount.")
        return
    new_file = not FILE.exists()
    with FILE.open("a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        if new_file:
            writer.writeheader()
        writer.writerow({"date": date.today().isoformat(), "category": category,
                         "description": description, "amount": f"{amount:.2f}"})
    print("Expense saved.")

def show_expenses():
    if not FILE.exists():
        print("No expenses saved yet.")
        return
    total = 0.0
    with FILE.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            amount = float(row["amount"])
            total += amount
            print(f'{row["date"]} | {row["category"]} | {row["description"]} | Rs {amount:.2f}')
    print(f"Total expenses: Rs {total:.2f}")

def main():
    while True:
        print("\nExpense Tracker\n1. Add expense\n2. Show expenses\n3. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_expenses()
        elif choice == "3":
            break
        else:
            print("Choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
