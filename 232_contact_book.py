import json
from pathlib import Path

FILE = Path("contacts.json")

def load_contacts():
    if not FILE.exists():
        return {}
    try:
        data = json.loads(FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, dict) else {}
    except (json.JSONDecodeError, OSError):
        print("Contacts file could not be read; starting with an empty book.")
        return {}

def save_contacts(contacts):
    FILE.write_text(json.dumps(contacts, indent=2), encoding="utf-8")

def main():
    contacts = load_contacts()
    while True:
        print("\n1. Add  2. Search  3. Show all  4. Delete  5. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            name, phone = input("Name: ").strip(), input("Phone: ").strip()
            if name and phone:
                contacts[name] = phone
                save_contacts(contacts)
                print("Contact saved.")
            else:
                print("Name and phone cannot be empty.")
        elif choice == "2":
            name = input("Name to search: ").strip()
            print(f"{name}: {contacts[name]}" if name in contacts else "Contact not found.")
        elif choice == "3":
            if not contacts:
                print("No contacts saved.")
            for name, phone in sorted(contacts.items()):
                print(f"{name}: {phone}")
        elif choice == "4":
            name = input("Name to delete: ").strip()
            if name in contacts:
                del contacts[name]
                save_contacts(contacts)
                print("Contact deleted.")
            else:
                print("Contact not found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
