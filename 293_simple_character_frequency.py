"""Project 293: Character Frequency Counter"""
from collections import Counter

def main():
    text = input("Enter some text: ")
    if not text:
        print("Please enter some text.")
        return
    counts = Counter(char for char in text if not char.isspace())
    print("Character frequencies:")
    for char, count in sorted(counts.items(), key=lambda item: item[0].lower()):
        print(f"{char}: {count}")

if __name__ == "__main__":
    main()
