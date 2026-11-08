def generate_table(number, limit=10):
    for multiplier in range(1, limit + 1):
        print(f"{number} x {multiplier} = {number * multiplier}")

def main():
    try:
        number = int(input("Enter a number: "))
        limit = int(input("How many multiples? [10]: ") or "10")
        if limit <= 0: raise ValueError
        generate_table(number, limit)
    except ValueError:
        print("Enter whole numbers and a positive limit.")

if __name__ == "__main__":
    main()
