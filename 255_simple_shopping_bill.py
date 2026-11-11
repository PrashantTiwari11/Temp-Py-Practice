"""Build a shopping bill from item names, prices, and quantities."""

def main():
    items = []
    print("Add items. Leave the item name blank to finish.")
    while True:
        name = input("Item name: ").strip()
        if not name:
            break
        try:
            price = float(input("Price per item: "))
            quantity = int(input("Quantity: "))
            if price < 0 or quantity < 1:
                print("Price must be non-negative and quantity at least 1.")
                continue
        except ValueError:
            print("Enter a valid price and whole-number quantity.")
            continue
        items.append((name, price, quantity))

    if not items:
        print("No items added.")
        return

    print("\n========== SHOPPING BILL ==========")
    total = 0
    for name, price, quantity in items:
        subtotal = price * quantity
        total += subtotal
        print(f"{name:<20} {quantity:>3} x {price:>8.2f} = {subtotal:>9.2f}")
    print("-----------------------------------")
    print(f"TOTAL: {total:.2f}")

if __name__ == "__main__":
    main()
