import json
import csv
from pathlib import Path

def main():
    source = Path(input("Enter JSON file path: ").strip())
    destination = Path(input("Enter output CSV file path (e.g. output.csv): ").strip())
    try:
        data = json.loads(source.read_text(encoding="utf-8"))
        if not isinstance(data, list) or not data:
            raise ValueError("JSON must contain a non-empty list of objects.")
        if not all(isinstance(row, dict) for row in data):
            raise ValueError("Every item must be an object.")
        fields = list(dict.fromkeys(key for row in data for key in row))
        with destination.open("w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writeheader()
            writer.writerows(data)
        print(f"Converted {len(data)} records to {destination}")
    except FileNotFoundError:
        print("Input file was not found.")
    except (json.JSONDecodeError, ValueError) as error:
        print(f"Could not convert file: {error}")

if __name__ == "__main__":
    main()
