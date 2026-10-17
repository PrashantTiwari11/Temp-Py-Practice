#!/usr/bin/env python3
"""Expense Analyzer — totals, category analysis, date filters, and CSV export.

Run: python 167_expense_analyzer.py
Uses only the Python standard library.
"""
import csv
from datetime import date
from pathlib import Path

DATA_FILE = Path("expenses.csv")
FIELDS = ["date", "description", "category", "amount"]

def load_expenses():
    if not DATA_FILE.exists(): return []
    try:
        with DATA_FILE.open(newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        return [{"date": r["date"], "description": r["description"],
                 "category": r["category"], "amount": float(r["amount"])} for r in rows]
    except (OSError, KeyError, ValueError):
        print("Warning: expenses.csv could not be read.")
        return []

def save_expenses(expenses):
    with DATA_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for e in expenses:
            writer.writerow({**e, "amount": f'{e["amount"]:.2f}'})

def add_expense(expenses):
    raw_date = input("Date (YYYY-MM-DD): ").strip()
    try: date.fromisoformat(raw_date)
    except ValueError:
        print("Invalid date format."); return
    description = input("Description: ").strip()
    category = input("Category (e.g. food, travel): ").strip().title()
    try:
        amount = float(input("Amount: "))
        if amount <= 0: raise ValueError
    except ValueError:
        print("Amount must be a positive number."); return
    if not description or not category:
        print("Description and category are required."); return
    expenses.append({"date": raw_date, "description": description,
                     "category": category, "amount": amount})
    save_expenses(expenses)
    print("Expense saved.")

def filtered_expenses(expenses):
    start = input("Start date YYYY-MM-DD (blank = no lower limit): ").strip()
    end = input("End date YYYY-MM-DD (blank = no upper limit): ").strip()
    try:
        if start: date.fromisoformat(start)
        if end: date.fromisoformat(end)
        if start and end and start > end: raise ValueError
    except ValueError:
        print("Invalid date range."); return []
    return [e for e in expenses if (not start or e["date"] >= start)
            and (not end or e["date"] <= end)]

def show_summary(expenses):
    if not expenses:
        print("No expenses in this selection."); return
    total = sum(e["amount"] for e in expenses)
    print(f"Transactions: {len(expenses)} | Total: {total:.2f} | Average: {total/len(expenses):.2f}")
    categories = {}
    for e in expenses: categories[e["category"]] = categories.get(e["category"], 0) + e["amount"]
    print("By category:")
    for cat, amount in sorted(categories.items(), key=lambda pair: pair[1], reverse=True):
        print(f"  {cat}: {amount:.2f} ({amount/total*100:.1f}%)")

def list_expenses(expenses):
    if not expenses: print("No expenses recorded."); return
    for i, e in enumerate(sorted(expenses, key=lambda x: x["date"]), 1):
        print(f'{i}. {e["date"]} | {e["description"]} | {e["category"]} | {e["amount"]:.2f}')

def export_csv(expenses):
    output = Path("expense_export.csv")
    with output.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        writer.writeheader()
        for e in expenses: writer.writerow({**e, "amount": f'{e["amount"]:.2f}'})
    print(f"Exported {len(expenses)} records to {output.resolve()}")

def main():
    expenses = load_expenses()
    while True:
        print("\n=== EXPENSE ANALYZER ===")
        print("1. Add expense\n2. List expenses\n3. Summary by category\n4. Summary with date filter\n5. Export all CSV\n0. Save and exit")
        choice = input("Choose: ").strip()
        if choice == "1": add_expense(expenses)
        elif choice == "2": list_expenses(expenses)
        elif choice == "3": show_summary(expenses)
        elif choice == "4": show_summary(filtered_expenses(expenses))
        elif choice == "5": export_csv(expenses)
        elif choice == "0":
            save_expenses(expenses); print("Saved. Goodbye!"); break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()
