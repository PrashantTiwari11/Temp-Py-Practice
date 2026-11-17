"""Calculate basic statistics for a list of numbers."""
def main():
    raw = input("Enter numbers separated by commas: ")
    try:
        numbers = [float(item.strip()) for item in raw.split(",") if item.strip()]
        if not numbers:
            print("Please enter at least one number.")
            return
    except ValueError:
        print("One or more entries are not valid numbers.")
        return

    values = sorted(numbers)
    middle = len(values) // 2
    median = (values[middle] if len(values) % 2 else
              (values[middle - 1] + values[middle]) / 2)
    print(f"Count: {len(numbers)}")
    print(f"Sum: {sum(numbers):g}")
    print(f"Average: {sum(numbers) / len(numbers):g}")
    print(f"Minimum: {min(numbers):g}")
    print(f"Maximum: {max(numbers):g}")
    print(f"Median: {median:g}")

if __name__ == "__main__":
    main()
