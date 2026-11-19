"""Project 282: Simple Tip Calculator"""
def main():
    try:
        bill = float(input("Enter the bill amount: ₹"))
        tip_percent = float(input("Enter tip percentage: "))
        people = int(input("How many people are sharing the bill? "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    if bill < 0 or tip_percent < 0 or people <= 0:
        print("Bill and tip cannot be negative; people must be at least 1.")
        return

    tip = bill * tip_percent / 100
    total = bill + tip
    print(f"Tip amount: ₹{tip:.2f}")
    print(f"Total bill: ₹{total:.2f}")
    print(f"Each person pays: ₹{total / people:.2f}")

if __name__ == "__main__":
    main()
