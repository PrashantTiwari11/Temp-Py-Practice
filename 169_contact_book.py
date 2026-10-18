"""169 Contact Book: manage contacts and export them to CSV."""
import csv, json
from pathlib import Path
DB = Path("contacts.json")

def load():
    try:
        data = json.loads(DB.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (OSError, json.JSONDecodeError):
        return []

def save(data):
    DB.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

def main():
    data = load()
    while True:
        print("\nCONTACT BOOK\n1 List  2 Add  3 Search  4 Edit  5 Delete  6 Export CSV  0 Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            for c in sorted(data, key=lambda x: x["name"].casefold()):
                print(f'{c["id"]}: {c["name"]} | {c["phone"]} | {c["email"]} | {c["group"]}')
            if not data: print("No contacts.")
        elif choice == "2":
            name, phone = input("Name: ").strip(), input("Phone: ").strip()
            email, group = input("Email (optional): ").strip(), input("Group: ").strip() or "General"
            if not name or not phone: print("Name and phone are required."); continue
            if any(c["phone"] == phone for c in data): print("Phone already exists."); continue
            data.append({"id": max((c["id"] for c in data), default=0)+1,
                         "name": name, "phone": phone, "email": email, "group": group})
            save(data); print("Contact saved.")
        elif choice == "3":
            term = input("Search: ").casefold().strip()
            found = [c for c in data if any(term in str(c[k]).casefold() for k in ("name","phone","email","group"))]
            for c in found: print(c)
            if not found: print("No matches.")
        elif choice == "4":
            try: cid = int(input("ID to edit: "))
            except ValueError: print("Invalid ID."); continue
            c = next((x for x in data if x["id"] == cid), None)
            if not c: print("Not found."); continue
            for key in ("name","phone","email","group"):
                value = input(f'{key.title()} [{c[key]}] (Enter keeps): ').strip()
                if value: c[key] = value
            if not c["name"] or not c["phone"]: print("Name and phone required."); continue
            if any(x["id"] != cid and x["phone"] == c["phone"] for x in data):
                print("Phone belongs to another contact."); continue
            save(data); print("Updated.")
        elif choice == "5":
            try: cid = int(input("ID to delete: "))
            except ValueError: print("Invalid ID."); continue
            c = next((x for x in data if x["id"] == cid), None)
            if c and input(f'Delete {c["name"]}? Type YES: ') == "YES":
                data.remove(c); save(data); print("Deleted.")
            else: print("Cancelled or not found.")
        elif choice == "6":
            with open("contacts_export.csv", "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=["id","name","phone","email","group"])
                w.writeheader(); w.writerows(data)
            print("Exported contacts_export.csv")
        elif choice == "0":
            save(data); print("Saved. Goodbye."); break
        else: print("Invalid choice.")

if __name__ == "__main__": main()
