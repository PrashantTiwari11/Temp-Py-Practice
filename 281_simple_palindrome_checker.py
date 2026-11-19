"""Project 281: Simple Palindrome Checker"""
def main():
    text = input("Enter a word or phrase: ")
    cleaned = "".join(c.lower() for c in text if c.isalnum())
    if not cleaned:
        print("Please enter at least one letter or digit.")
    elif cleaned == cleaned[::-1]:
        print("It is a palindrome!")
    else:
        print("It is not a palindrome.")

if __name__ == "__main__":
    main()
