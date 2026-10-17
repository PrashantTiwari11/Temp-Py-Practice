#!/usr/bin/env python3
"""Library Manager — book inventory, borrowing, returns, and JSON saving.

Run: python 166_library_manager.py
Uses only the Python standard library.
"""
import json
from pathlib import Path

DATA_FILE = Path("library.json")

def load_data():
    if DATA_FILE.exists():
        try:
            data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
            if isinstance(data, dict) and "books" in data and "loans" in data:
                return data
        except (OSError, json.JSONDecodeError):
            print("Warning: could not load library.json; starting fresh.")
    return {"books": [], "loans": []}

def save_data(data):
    DATA_FILE.write_text(json.dumps(data, indent=2), encoding="utf-8")

def list_books(data):
    if not data["books"]:
        print("No books in inventory.")
    for b in data["books"]:
        available = b["quantity"] - sum(1 for loan in data["loans"]
                                          if loan["book_id"] == b["id"] and not loan["returned"])
        print(f'ID {b["id"]} | {b["title"]} — {b["author"]} | total={b["quantity"]} | available={available}')

def add_book(data):
    title = input("Book title: ").strip()
    author = input("Author: ").strip()
    if not title or not author:
        print("Title and author are required.")
        return
    try:
        quantity = int(input("Number of copies: "))
        if quantity < 1: raise ValueError
    except ValueError:
        print("Quantity must be a positive integer.")
        return
    next_id = max((b["id"] for b in data["books"]), default=0) + 1
    data["books"].append({"id": next_id, "title": title, "author": author, "quantity": quantity})
    save_data(data)
    print(f"Book added with ID {next_id}.")

def borrow_book(data):
    try:
        book_id = int(input("Book ID to borrow: "))
    except ValueError:
        print("Enter a valid numeric ID.")
        return
    book = next((b for b in data["books"] if b["id"] == book_id), None)
    if not book:
        print("Book not found.")
        return
    active = sum(1 for loan in data["loans"] if loan["book_id"] == book_id and not loan["returned"])
    if active >= book["quantity"]:
        print("No copies currently available.")
        return
    borrower = input("Borrower's name: ").strip()
    if not borrower:
        print("Borrower's name is required.")
        return
    loan_id = max((x["id"] for x in data["loans"]), default=0) + 1
    data["loans"].append({"id": loan_id, "book_id": book_id, "borrower": borrower,
                          "borrowed_on": input("Borrow date (YYYY-MM-DD): ").strip(),
                          "returned": False, "returned_on": None})
    save_data(data)
    print(f"Loan recorded with ID {loan_id}.")

def return_book(data):
    try:
        loan_id = int(input("Loan ID to return: "))
    except ValueError:
        print("Enter a valid numeric loan ID.")
        return
    loan = next((x for x in data["loans"] if x["id"] == loan_id), None)
    if not loan:
        print("Loan not found.")
        return
    if loan["returned"]:
        print("This loan is already marked returned.")
        return
    loan["returned"] = True
    loan["returned_on"] = input("Return date (YYYY-MM-DD): ").strip()
    save_data(data)
    print("Return recorded.")

def show_loans(data):
    if not data["loans"]:
        print("No borrowing records.")
    for loan in data["loans"]:
        book = next((b for b in data["books"] if b["id"] == loan["book_id"]), None)
        title = book["title"] if book else "(deleted book)"
        status = "Returned" if loan["returned"] else "Borrowed"
        print(f'Loan {loan["id"]} | {title} | {loan["borrower"]} | {status} | '
              f'{loan["borrowed_on"]} -> {loan["returned_on"] or "-"}')

def search_books(data):
    term = input("Search title/author: ").strip().lower()
    results = [b for b in data["books"] if term in b["title"].lower() or term in b["author"].lower()]
    for b in results:
        print(f'ID {b["id"]}: {b["title"]} — {b["author"]}')
    if not results:
        print("No matching books.")

def delete_book(data):
    try:
        book_id = int(input("Book ID to delete: "))
    except ValueError:
        print("Enter a valid numeric ID.")
        return
    if any(x["book_id"] == book_id and not x["returned"] for x in data["loans"]):
        print("Cannot delete a book with active loans.")
        return
    before = len(data["books"])
    data["books"] = [b for b in data["books"] if b["id"] != book_id]
    save_data(data)
    print("Book deleted." if len(data["books"]) < before else "Book not found.")

def main():
    data = load_data()
    menu = {
        "1": ("List inventory", lambda: list_books(data)),
        "2": ("Add book", lambda: add_book(data)),
        "3": ("Borrow book", lambda: borrow_book(data)),
        "4": ("Return book", lambda: return_book(data)),
        "5": ("View loans", lambda: show_loans(data)),
        "6": ("Search books", lambda: search_books(data)),
        "7": ("Delete book", lambda: delete_book(data)),
    }
    while True:
        print("\n=== LIBRARY MANAGER ===")
        for key, (label, _) in menu.items(): print(f"{key}. {label}")
        print("0. Exit")
        choice = input("Choose: ").strip()
        if choice == "0":
            save_data(data)
            print("Saved. Goodbye!")
            break
        if choice in menu: menu[choice][1]()
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()
