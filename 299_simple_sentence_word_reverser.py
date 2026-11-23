"""Project 299: Reverse the Order of Words in a Sentence"""
def main():
    sentence = input("Enter a sentence: ").strip()
    words = sentence.split()
    if not words:
        print("Please enter a sentence.")
        return
    print("Words in reverse order:", " ".join(reversed(words)))

if __name__ == "__main__":
    main()
