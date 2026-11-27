# Simple Multiplication Table
try:
    number = int(input("Enter a number: "))
    limit = int(input("How many multiples should be displayed? "))
    if limit < 1:
        print("The limit must be at least 1.")
    else:
        print(f"\nMultiplication table of {number}:")
        for i in range(1, limit + 1):
            print(f"{number} x {i} = {number * i}")
except ValueError:
    print("Please enter valid whole numbers.")
