from collections import Counter
import re
from pathlib import Path

def analyze(text):
    return Counter(re.findall(r"\b[\w']+\b", text.lower()))

def main():
    path = Path(input("Enter a text file path: ").strip())
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print("File not found.")
        return
    except UnicodeDecodeError:
        print("Could not read the file as UTF-8 text.")
        return
    counts = analyze(text)
    if not counts:
        print("No words found.")
        return
    print(f"Total words: {sum(counts.values())}")
    print(f"Unique words: {len(counts)}")
    print("\nMost common words:")
    for word, count in counts.most_common(15):
        print(f"{word:<20} {count}")

if __name__ == "__main__":
    main()
