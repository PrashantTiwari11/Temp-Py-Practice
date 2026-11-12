"""Store contacts and search by name."""
def main():
    contacts = {}
    while True:
        print("\n1. Add contact  2. Search  3. Show all  4. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            if name and phone:
                contacts[name.lower()] = (name, phone)
                print("Contact saved.")
            else:
                print("Both fields are required.")
        elif choice == "2":
            query = input("Search name: ").strip().lower()
            matches = [v for k, v in contacts.items() if query in k]
            if matches:
                for name, phone in matches:
                    print(f"{name}: {phone}")
            else:
                print("No matching contact.")
        elif choice == "3":
            for name, phone in contacts.values():
                print(f"{name}: {phone}")
            if not contacts:
                print("No contacts saved.")
        elif choice == "4":
            break
        else:
            print("Choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
