"""214 - Searchable Contact CSV"""
import csv
from pathlib import Path

FILE = Path("contacts.csv")
FIELDS = ["name", "phone", "email"]

def ensure_file():
    if not FILE.exists():
        with FILE.open("w", newline="", encoding="utf-8") as handle:
            csv.DictWriter(handle, fieldnames=FIELDS).writeheader()

def add_contact():
    name = input("Name: ").strip()
    if not name:
        print("Name is required.")
        return
    row = {"name": name, "phone": input("Phone: ").strip(),
           "email": input("Email: ").strip()}
    with FILE.open("a", newline="", encoding="utf-8") as handle:
        csv.DictWriter(handle, fieldnames=FIELDS).writerow(row)
    print("Contact saved.")

def search_contacts():
    term = input("Search name, phone, or email: ").strip().lower()
    with FILE.open(newline="", encoding="utf-8") as handle:
        matches = [row for row in csv.DictReader(handle)
                   if any(term in value.lower() for value in row.values())]
    if matches:
        for row in matches:
            print(f'{row["name"]} | {row["phone"]} | {row["email"]}')
    else:
        print("No matching contacts.")

def main():
    ensure_file()
    while True:
        print("\nContact Search\n1. Add contact\n2. Search\n3. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contacts()
        elif choice == "3":
            break
        else:
            print("Choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
