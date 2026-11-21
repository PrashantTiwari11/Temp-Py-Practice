"""Project 291: Sort a List of Numbers"""
def main():
    raw = input("Enter numbers separated by spaces: ").strip()
    try:
        numbers = [float(value) for value in raw.split()]
    except ValueError:
        print("Please enter valid numbers separated by spaces.")
        return
    if not numbers:
        print("Please enter at least one number.")
        return
    print("Ascending order:", sorted(numbers))
    print("Descending order:", sorted(numbers, reverse=True))

if __name__ == "__main__":
    main()
