"""Manage product quantities in a small in-memory inventory."""
def main():
    inventory = {}
    while True:
        print("\n1. Add/update stock  2. View inventory  3. Remove product  4. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            name = input("Product name: ").strip()
            if not name:
                print("Product name cannot be empty.")
                continue
            try:
                quantity = int(input("Quantity to add: "))
                if quantity < 0:
                    print("Quantity cannot be negative.")
                    continue
            except ValueError:
                print("Enter a whole number.")
                continue
            inventory[name] = inventory.get(name, 0) + quantity
            print("Stock updated.")
        elif choice == "2":
            if inventory:
                for name, quantity in sorted(inventory.items()):
                    print(f"{name}: {quantity}")
            else:
                print("Inventory is empty.")
        elif choice == "3":
            name = input("Product name to remove: ").strip()
            if name in inventory:
                del inventory[name]
                print("Product removed.")
            else:
                print("Product not found.")
        elif choice == "4":
            break
        else:
            print("Choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
