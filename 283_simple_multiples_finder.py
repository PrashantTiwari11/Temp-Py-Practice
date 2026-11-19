"""Project 283: Simple Multiples Finder"""
def main():
    try:
        number = int(input("Enter a number: "))
        count = int(input("How many multiples should be shown? "))
    except ValueError:
        print("Please enter whole numbers.")
        return

    if count <= 0:
        print("Count must be greater than zero.")
        return

    print(f"First {count} multiples of {number}:")
    for multiplier in range(1, count + 1):
        print(f"{number} x {multiplier} = {number * multiplier}")

if __name__ == "__main__":
    main()
