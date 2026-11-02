"""221 - CSV Data Summary. Usage: python 221_csv_data_summary.py [file.csv]"""
import csv
import sys
from pathlib import Path

def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(input("CSV path: ").strip())
    if not path.is_file():
        print("File not found:", path)
        return
    with path.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        print("CSV has no data rows.")
        return
    print("Rows:", len(rows))
    print("Columns:", ", ".join(rows[0].keys()))
    for column in rows[0]:
        values = []
        for row in rows:
            try:
                values.append(float(row[column]))
            except (ValueError, TypeError):
                continue
        if values:
            print(f"{column}: count={len(values)}, min={min(values):.2f}, "
                  f"max={max(values):.2f}, average={sum(values)/len(values):.2f}")

if __name__ == "__main__":
    main()
