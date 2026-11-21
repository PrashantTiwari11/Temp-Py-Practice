"""Project 292: Remove Vowels from Text"""
def main():
    text = input("Enter a sentence: ")
    vowels = "aeiouAEIOU"
    result = "".join(char for char in text if char not in vowels)
    print("Text without vowels:", result)
    print("Vowels removed:", len(text) - len(result))

if __name__ == "__main__":
    main()
