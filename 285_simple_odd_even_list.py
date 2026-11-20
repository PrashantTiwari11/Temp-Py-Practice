"""Project 285: Odd and Even Number List Separator"""
def main():
    raw = input("Enter whole numbers separated by spaces: ").strip()
    try:
        numbers = [int(value) for value in raw.split()]
    except ValueError:
        print("Please enter only whole numbers.")
        return
    print("Even numbers:", [n for n in numbers if n % 2 == 0])
    print("Odd numbers:", [n for n in numbers if n % 2 != 0])

if __name__ == "__main__":
    main()
