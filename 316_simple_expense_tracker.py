# Simple Expense Tracker
expenses = []
while True:
    print("\nSimple Expense Tracker")
    print("1. Add expense")
    print("2. Show expenses")
    print("3. Show total")
    print("4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        name = input("Expense description: ")
        try:
            amount = float(input("Amount: ₹"))
            if amount < 0:
                print("Amount cannot be negative.")
                continue
            expenses.append((name, amount))
            print("Expense added.")
        except ValueError:
            print("Please enter a valid amount.")
    elif choice == "2":
        if not expenses:
            print("No expenses recorded.")
        else:
            print("\nRecorded expenses:")
            for index, (name, amount) in enumerate(expenses, start=1):
                print(f"{index}. {name}: ₹{amount:.2f}")
    elif choice == "3":
        total = sum(amount for _, amount in expenses)
        print(f"Total expenses: ₹{total:.2f}")
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
