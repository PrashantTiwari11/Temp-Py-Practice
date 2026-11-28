# 318 - Even/Odd List Checker

def check_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(f"{number} is Even")
        else:
            print(f"{number} is Odd")

print("=== Even/Odd List Checker ===")
raw = input("Enter numbers separated by spaces: ")

try:
    numbers = [int(value) for value in raw.split()]
    if not numbers:
        print("Please enter at least one number.")
    else:
        check_numbers(numbers)
except ValueError:
    print("Invalid input. Please enter integers only.")
