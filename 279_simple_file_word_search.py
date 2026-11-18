"""Project 279: Search for a Word in a Text File"""

from pathlib import Path

def main():
    filename = input("Enter the text file path: ").strip()
    search_word = input("Enter the word to find: ").strip()
    if not search_word:
        print("Search word cannot be empty.")
        return

    try:
        content = Path(filename).read_text(encoding="utf-8")
    except FileNotFoundError:
        print("File not found. Check the path and try again.")
        return
    except OSError as error:
        print("Could not read the file:", error)
        return

    matches = [
        (number, line.strip())
        for number, line in enumerate(content.splitlines(), start=1)
        if search_word.casefold() in line.casefold()
    ]
    if not matches:
        print(f"'{search_word}' was not found.")
        return

    print(f"Found '{search_word}' on {len(matches)} line(s):")
    for number, line in matches:
        print(f"Line {number}: {line}")


if __name__ == "__main__":
    main()
