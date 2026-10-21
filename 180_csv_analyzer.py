"""180 — CSV Analyzer: inspect CSV columns, missing values, numeric stats, and export filtered rows."""
import csv
from pathlib import Path

def load_csv(path):
    with path.open("r", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise ValueError("CSV has no header row.")
        return reader.fieldnames, list(reader)

def main():
    raw = input("CSV file path: ").strip().strip('"')
    path = Path(raw).expanduser()
    if not path.is_file():
        print("File not found."); return
    try:
        headers, rows = load_csv(path)
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        print("Could not read CSV:", exc); return
    print(f"Rows: {len(rows)} | Columns: {len(headers)}")
    print("Columns:", ", ".join(headers))
    for col in headers:
        values = [r.get(col, "") or "" for r in rows]
        missing = sum(not v.strip() for v in values)
        numeric = []
        for value in values:
            try:
                if value.strip(): numeric.append(float(value))
            except ValueError:
                numeric = []; break
        print(f"\n{col}: missing={missing}/{len(rows)}")
        if numeric:
            print(f"  numeric count={len(numeric)}, min={min(numeric):g}, max={max(numeric):g}, mean={sum(numeric)/len(numeric):g}")
        else:
            print("  sample values:", ", ".join(v for v in values if v.strip())[:160] or "(no values)")
    if input("\nFilter rows by exact column value and export? (y/n): ").strip().lower() in {"y","yes"}:
        col = input("Column name: ").strip()
        if col not in headers:
            print("Unknown column."); return
        value = input("Exact value to keep: ")
        filtered = [r for r in rows if (r.get(col) or "") == value]
        out = path.with_name(path.stem + "_filtered.csv")
        try:
            with out.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=headers)
                writer.writeheader(); writer.writerows(filtered)
            print(f"Exported {len(filtered)} rows to {out}")
        except OSError as exc:
            print("Could not export:", exc)

if __name__ == "__main__":
    main()
