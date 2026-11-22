"""Project 295: Word Length Analyzer"""
def main():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    if not words:
        print("No words were entered.")
        return
    print("Word lengths:")
    for word in words:
        cleaned = word.strip(".,!?;:\"'()[]{}")
        print(f"{cleaned}: {len(cleaned)} characters")
    longest = max(words, key=len)
    shortest = min(words, key=len)
    print(f"Longest word: {longest} ({len(longest)} characters)")
    print(f"Shortest word: {shortest} ({len(shortest)} characters)")

if __name__ == "__main__":
    main()
