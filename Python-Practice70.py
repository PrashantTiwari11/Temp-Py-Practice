# 63_file_handling_projects.py
# File Handling - 10 practical programs/features
from pathlib import Path
import json, csv, tempfile

work = Path(tempfile.gettempdir()) / "python_file_demo"
work.mkdir(exist_ok=True)

text_file = work / "notes.txt"
text_file.write_text("Python\nFile handling\nPractice", encoding="utf-8")
print("1. File created:", text_file)
content = text_file.read_text(encoding="utf-8")
print("2. Read:", content)
print("3. Lines:", len(content.splitlines()))
print("4. Words:", len(content.split()))
with text_file.open("a", encoding="utf-8") as f: f.write("\nPython projects")
print("5. Appended:", text_file.read_text(encoding="utf-8"))
print("6. Contains Python:", "Python" in text_file.read_text(encoding="utf-8"))

json_file = work / "student.json"
student = {"name":"Prashant", "course":"B.Tech Computer Engineering", "year":2}
json_file.write_text(json.dumps(student, indent=2), encoding="utf-8")
print("7. JSON saved.")
print("8. JSON loaded:", json.loads(json_file.read_text(encoding="utf-8")))

csv_file = work / "marks.csv"
rows = [["Name","Marks"],["Aman",82],["Riya",91],["Karan",76]]
with csv_file.open("w", newline="", encoding="utf-8") as f: csv.writer(f).writerows(rows)
with csv_file.open("r", newline="", encoding="utf-8") as f: print("9. CSV:", list(csv.reader(f)))
print("10. Project files:", sorted(p.name for p in work.iterdir()))
