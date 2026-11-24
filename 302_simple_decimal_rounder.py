"""Project 302: Round a Decimal Number"""
def main():
    try:
        number = float(input("Enter a decimal number: "))
        places = int(input("How many decimal places? "))
    except ValueError:
        print("Please enter a valid number and whole-number decimal places.")
        return
    if places < 0:
        print("Decimal places cannot be negative.")
        return
    print(f"Rounded result: {number:.{places}f}")

if __name__ == "__main__":
    main()
