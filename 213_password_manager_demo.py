"""213 - Password Vault Demo. Educational only; stores plain text, not secure."""
import json
from pathlib import Path

FILE = Path("password_vault_demo.json")

def main():
    try:
        entries = json.loads(FILE.read_text(encoding="utf-8")) if FILE.exists() else []
    except (OSError, json.JSONDecodeError):
        entries = []
        print("Starting with an empty demo vault.")
    while True:
        print("\n1. Add demo entry  2. View entries  3. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            entries.append({
                "site": input("Website/app label: ").strip(),
                "username": input("Demo username: ").strip(),
                "password": input("Sample password (never enter a real password): ").strip()
            })
            FILE.write_text(json.dumps(entries, indent=2), encoding="utf-8")
            print("Saved locally. Warning: this file is not encrypted.")
        elif choice == "2":
            for item in entries:
                print(f'{item["site"]} | {item["username"]} | {item["password"]}')
            if not entries:
                print("No entries saved.")
        elif choice == "3":
            break
        else:
            print("Choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
