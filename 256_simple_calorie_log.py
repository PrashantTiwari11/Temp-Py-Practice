"""Record food items and user-entered calorie estimates."""

def main():
    entries = []
    print("Add food items and calorie estimates.")
    print("Leave the food name blank when finished.")
    while True:
        food = input("Food item: ").strip()
        if not food:
            break
        try:
            calories = float(input("Calories: "))
            if calories < 0:
                print("Calories cannot be negative.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue
        entries.append((food, calories))

    if not entries:
        print("No food entries recorded.")
        return

    print("\nDaily food log")
    total = 0
    for food, calories in entries:
        print(f"- {food}: {calories:g} kcal")
        total += calories
    print(f"Total recorded: {total:g} kcal")
    print("Calorie values are estimates, not dietary advice.")

if __name__ == "__main__":
    main()
