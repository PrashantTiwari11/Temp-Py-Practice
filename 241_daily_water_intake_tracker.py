def main():
    goal, total = 2000, 0
    print("Daily Water Intake Tracker")
    while True:
        print("\\n1. Add water  2. View progress  3. Change goal  4. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            try:
                amount = int(input("Water consumed (ml): "))
                if amount <= 0: raise ValueError
                total += amount
                print(f"Added {amount} ml.")
            except ValueError:
                print("Enter a positive whole number.")
        elif choice == "2":
            print(f"Consumed: {total} / {goal} ml")
            print(f"Remaining: {max(goal-total, 0)} ml")
            if total >= goal: print("Daily goal achieved!")
        elif choice == "3":
            try:
                value = int(input("New goal (ml): "))
                if value <= 0: raise ValueError
                goal = value
            except ValueError:
                print("Goal must be a positive whole number.")
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
