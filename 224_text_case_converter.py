"""224 - Text Case Converter"""

def main():
    text = input("Enter text: ")
    while True:
        print("\n1. UPPERCASE  2. lowercase  3. Title Case")
        print("4. Sentence case  5. Swap Case  6. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            print(text.upper())
        elif choice == "2":
            print(text.lower())
        elif choice == "3":
            print(text.title())
        elif choice == "4":
            print(text.capitalize())
        elif choice == "5":
            print(text.swapcase())
        elif choice == "6":
            break
        else:
            print("Choose a number from 1 to 6.")

if __name__ == "__main__":
    main()
