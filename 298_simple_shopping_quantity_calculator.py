"""Project 298: Shopping Quantity Cost Calculator"""
def main():
    try:
        price = float(input("Enter price per item: ₹"))
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("Please enter a valid price and whole-number quantity.")
        return
    if price < 0 or quantity < 0:
        print("Price and quantity cannot be negative.")
        return
    print(f"Subtotal: ₹{price * quantity:.2f}")
    print(f"Quantity: {quantity}")

if __name__ == "__main__":
    main()
