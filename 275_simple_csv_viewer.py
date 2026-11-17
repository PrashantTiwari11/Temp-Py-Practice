"""Read and display rows from a CSV file."""
import csv
from pathlib import Path

def main():
    path = Path(input("Enter CSV file path: ").strip().strip('"')).expanduser()
    if not path.is_file():
        print("File not found. Check the path and try again.")
        return
    try:
        with path.open("r", newline="", encoding="utf-8-sig") as file:
            rows = list(csv.reader(file))
        if not rows:
            print("The CSV file is empty.")
            return
        for row in rows:
            print(" | ".join(row))
        print(f"\nTotal rows: {len(rows)}")
    except (OSError, UnicodeError, csv.Error) as error:
        print(f"Could not read the CSV file: {error}")

if __name__ == "__main__":
    main()
