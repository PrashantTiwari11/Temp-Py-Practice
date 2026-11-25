# Simple Calculator with History

history = []

while True:
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Show history")
    print("6. Exit")

    choice = input("Choose an option: ")

    if choice in ("1", "2", "3", "4"):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            result = a + b
            operation = "+"
        elif choice == "2":
            result = a - b
            operation = "-"
        elif choice == "3":
            result = a * b
            operation = "*"
        else:
            if b == 0:
                print("Cannot divide by zero.")
                continue
            result = a / b
            operation = "/"

        entry = f"{a} {operation} {b} = {result}"
        print("Result:", result)
        history.append(entry)

    elif choice == "5":
        if history:
            print("Calculation history:")
            for item in history:
                print(item)
        else:
            print("No calculations yet.")

    elif choice == "6":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
