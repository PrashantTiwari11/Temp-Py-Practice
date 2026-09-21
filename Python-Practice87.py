# 82_python_csv_excel_data.py
# CSV and Tabular Data Processing - 10 practical programs/features
import csv
import io

csv_text = """name,course,marks
Prashant,Computer Engineering,85
Aman,Computer Engineering,72
Riya,Information Technology,91
"""

reader = csv.DictReader(io.StringIO(csv_text))
rows = list(reader)

print("1. CSV rows:", rows)
print("2. Names:", [row["name"] for row in rows])

marks = [int(row["marks"]) for row in rows]
print("3. Marks:", marks)
print("4. Average:", sum(marks) / len(marks))

top = max(rows, key=lambda row: int(row["marks"]))
print("5. Top student:", top["name"])

high = [row["name"] for row in rows if int(row["marks"]) >= 80]
print("6. Marks >= 80:", high)

sorted_rows = sorted(rows, key=lambda row: int(row["marks"]), reverse=True)
print("7. Sorted:", [(r["name"], r["marks"]) for r in sorted_rows])

output = io.StringIO()
writer = csv.DictWriter(output, fieldnames=["name", "marks"])
writer.writeheader()
writer.writerows([{"name": "Neha", "marks": 88}, {"name": "Raj", "marks": 76}])
print("8. Generated CSV:\n" + output.getvalue())

print("9. Dictionary keys:", list(rows[0].keys()))

for row in rows:
    mark = int(row["marks"])
    row["grade"] = "A" if mark >= 80 else "B" if mark >= 60 else "C"

print("10. With grades:", rows)
