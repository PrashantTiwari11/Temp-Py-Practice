"""Project 277: Simple Text Case Converter"""

def main():
    text = input("Enter some text: ")
    print("\nChoose a format:")
    print("1. UPPERCASE")
    print("2. lowercase")
    print("3. Title Case")
    print("4. Sentence case")
    choice = input("Your choice (1-4): ").strip()

    conversions = {
        "1": str.upper,
        "2": str.lower,
        "3": str.title,
        "4": str.capitalize,
    }
    if choice not in conversions:
        print("Invalid choice.")
        return
    print("\nConverted text:", conversions[choice](text))


if __name__ == "__main__":
    main()
