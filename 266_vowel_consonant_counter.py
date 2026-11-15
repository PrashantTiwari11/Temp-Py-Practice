"""Count vowels, consonants, digits, and spaces in text."""
def main():
    text = input("Enter a sentence: ")
    vowels = sum(c.lower() in "aeiou" for c in text if c.isalpha())
    consonants = sum(c.isalpha() and c.lower() not in "aeiou" for c in text)
    digits = sum(c.isdigit() for c in text)
    spaces = sum(c.isspace() for c in text)
    print(f"Vowels: {vowels}")
    print(f"Consonants: {consonants}")
    print(f"Digits: {digits}")
    print(f"Spaces: {spaces}")

if __name__ == "__main__":
    main()
