"""Simulate rolling one or more six-sided dice."""
import random

def main():
    try:
        count = int(input("How many dice would you like to roll? "))
        if count < 1:
            print("Enter at least 1.")
            return
        rolls = [random.randint(1, 6) for _ in range(count)]
        print("Rolls:", rolls)
        print("Total:", sum(rolls))
    except ValueError:
        print("Please enter a valid whole number.")

if __name__ == "__main__":
    main()
