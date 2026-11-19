"""Project 284: Simple Text File Line Counter"""
from pathlib import Path

def main():
    filename = input("Enter the text file path: ").strip()
    try:
        content = Path(filename).read_text(encoding="utf-8")
    except FileNotFoundError:
        print("File not found. Please check the path.")
        return
    except OSError as error:
        print("Could not read the file:", error)
        return

    lines = content.splitlines()
    non_empty = [line for line in lines if line.strip()]
    print("Total lines:", len(lines))
    print("Non-empty lines:", len(non_empty))
    print("Empty lines:", len(lines) - len(non_empty))

if __name__ == "__main__":
    main()
