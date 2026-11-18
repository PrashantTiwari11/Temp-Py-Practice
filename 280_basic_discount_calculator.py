"""Project 280: Basic Discount Calculator"""

def main():
    try:
        price = float(input("Enter the original price: ₹"))
        discount = float(input("Enter discount percentage: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if price < 0:
        print("Price cannot be negative.")
        return
    if not 0 <= discount <= 100:
        print("Discount must be between 0 and 100.")
        return

    saved = price * discount / 100
    print(f"Discount amount: ₹{saved:.2f}")
    print(f"Final price: ₹{price - saved:.2f}")


if __name__ == "__main__":
    main()
