# 109_python_csv_student_report.py
# CSV Student Report - 10 practical features
import csv, io

rows = [
    ["Name", "Python", "DSA", "IoT"],
    ["Prashant", 85, 78, 92],
    ["Aman", 72, 68, 80],
    ["Riya", 91, 88, 95],
    ["Neha", 65, 74, 70],
]

# 1. Create CSV
buffer = io.StringIO()
csv.writer(buffer).writerows(rows)
csv_text = buffer.getvalue()
print("1. CSV created:\n", csv_text)

# 2. Read CSV
reader = list(csv.reader(io.StringIO(csv_text)))
print("2. Row count:", len(reader))

# 3. Header
header = reader[0]
print("3. Header:", header)

# 4. Dictionary records
records = [dict(zip(header, row)) for row in reader[1:]]
print("4. First record:", records[0])

# 5. Student averages
for r in records:
    marks = [int(r["Python"]), int(r["DSA"]), int(r["IoT"])]
    r["Average"] = round(sum(marks) / len(marks), 2)
print("5. Averages:", [(r["Name"], r["Average"]) for r in records])

# 6. Topper
topper = max(records, key=lambda r: r["Average"])
print("6. Topper:", topper["Name"])

# 7. Class average
class_avg = sum(r["Average"] for r in records) / len(records)
print("7. Class average:", round(class_avg, 2))

# 8. Students above 80
print("8. Above 80:", [r["Name"] for r in records if r["Average"] >= 80])

# 9. Ranking
ranking = sorted(records, key=lambda r: r["Average"], reverse=True)
print("9. Ranking:", [(r["Name"], r["Average"]) for r in ranking])

# 10. Export report
report = io.StringIO()
w = csv.writer(report)
w.writerow(["Name", "Average"])
for r in ranking:
    w.writerow([r["Name"], r["Average"]])
print("10. Exported report:\n", report.getvalue())
