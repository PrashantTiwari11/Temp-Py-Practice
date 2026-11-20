"""Project 287: Average Calculator for Multiple Numbers"""
def main():
    raw = input("Enter numbers separated by spaces: ").strip()
    try:
        numbers = [float(value) for value in raw.split()]
    except ValueError:
        print("Please enter valid numbers separated by spaces.")
        return
    if not numbers:
        print("You must enter at least one number.")
        return
    print("Count:", len(numbers))
    print(f"Sum: {sum(numbers):g}")
    print(f"Average: {sum(numbers) / len(numbers):g}")

if __name__ == "__main__":
    main()
