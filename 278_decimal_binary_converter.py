"""Project 278: Decimal and Binary Converter"""

def main():
    print("1. Decimal to binary")
    print("2. Binary to decimal")
    choice = input("Choose 1 or 2: ").strip()
    try:
        if choice == "1":
            number = int(input("Enter a decimal whole number: "))
            binary = bin(abs(number))[2:]
            print("Binary:", ("-" if number < 0 else "") + binary)
        elif choice == "2":
            binary_text = input("Enter a binary number: ").strip()
            print("Decimal:", int(binary_text, 2))
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid whole number or binary value.")


if __name__ == "__main__":
    main()
