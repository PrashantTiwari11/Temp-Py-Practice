"""Split a shared expense equally among a group."""
def main():
    try:
        total = float(input("Total expense amount: "))
        people = int(input("Number of people: "))
        if total < 0 or people < 1:
            print("Enter a non-negative amount and at least one person.")
            return
        print(f"Each person should pay: {total / people:.2f}")
    except ValueError:
        print("Please enter a valid amount and whole number.")

if __name__ == "__main__":
    main()
