"""Project 297: Random Name Picker"""
import random

def main():
    raw = input("Enter names separated by commas: ")
    names = [name.strip() for name in raw.split(",") if name.strip()]
    if not names:
        print("Please enter at least one name.")
        return
    print("Selected name:", random.choice(names))

if __name__ == "__main__":
    main()
