"""Reverse the order of words in a sentence."""
def main():
    sentence = input("Enter a sentence: ").strip()
    if not sentence:
        print("No text was entered.")
        return
    print("Reversed word order:")
    print(" ".join(sentence.split()[::-1]))

if __name__ == "__main__":
    main()
