# 319 - Shopping Bill Calculator

print("=== Shopping Bill Calculator ===")
items = []

while True:
    name = input("Enter item name (or 'done' to finish): ").strip()
    if name.lower() == "done":
        break
    try:
        price = float(input(f"Enter price for {name}: ₹"))
        quantity = int(input(f"Enter quantity for {name}: "))
        if price < 0 or quantity < 0:
            print("Price and quantity cannot be negative.")
            continue
        items.append((name, price, quantity))
    except ValueError:
        print("Please enter a valid price and quantity.")

print("\n------ BILL ------")
total = 0
for name, price, quantity in items:
    amount = price * quantity
    total += amount
    print(f"{name:<20} x{quantity:<3} ₹{amount:.2f}")

print("------------------")
print(f"Total: ₹{total:.2f}")
