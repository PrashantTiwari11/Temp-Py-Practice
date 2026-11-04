import csv
from pathlib import Path

FILE = Path("expenses.csv")

def add_expense():
    date = input("Date (YYYY-MM-DD): ").strip()
    category = input("Category: ").strip()
    try:
        amount = float(input("Amount: ₹"))
        if amount <= 0:
            raise ValueError
    except ValueError:
        print("Enter a positive valid amount.")
        return
    is_new = not FILE.exists()
    with FILE.open("a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if is_new:
            writer.writerow(["date", "category", "amount"])
        writer.writerow([date, category, f"{amount:.2f}"])
    print("Expense saved.")

def show_summary():
    if not FILE.exists():
        print("No expenses recorded yet.")
        return
    total, categories = 0.0, {}
    with FILE.open(newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            amount = float(row["amount"])
            total += amount
            categories[row["category"]] = categories.get(row["category"], 0) + amount
    print(f"Total expenses: ₹{total:.2f}")
    for category, amount in sorted(categories.items()):
        print(f"{category}: ₹{amount:.2f}")

def main():
    while True:
        print("\n1. Add expense  2. View summary  3. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_expense()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
