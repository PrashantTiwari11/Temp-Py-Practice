#!/usr/bin/env python3
"""Student Gradebook — marks, averages, grades, rankings, and CSV export.

Run: python 165_student_gradebook.py
Uses only the Python standard library.
"""
import csv
import json
from pathlib import Path

DATA_FILE = Path("gradebook.json")
CSV_FILE = Path("gradebook_export.csv")

def load_students():
    if DATA_FILE.exists():
        try:
            data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
            return data if isinstance(data, list) else []
        except (json.JSONDecodeError, OSError):
            print("Warning: could not read gradebook.json; starting empty.")
    return []

def save_students(students):
    DATA_FILE.write_text(json.dumps(students, indent=2), encoding="utf-8")

def grade_for(avg):
    if avg >= 90: return "A+"
    if avg >= 80: return "A"
    if avg >= 70: return "B"
    if avg >= 60: return "C"
    if avg >= 50: return "D"
    return "F"

def show_students(students):
    ranked = sorted(students, key=lambda s: s["average"], reverse=True)
    if not ranked:
        print("No students found.")
        return
    print("\nRank | ID | Name | Average | Grade")
    print("-" * 58)
    for rank, s in enumerate(ranked, 1):
        print(f'{rank:>4} | {s["id"]} | {s["name"]} | {s["average"]:.2f} | {s["grade"]}')

def add_student(students):
    sid = input("Student ID: ").strip()
    if not sid or any(s["id"] == sid for s in students):
        print("ID must be non-empty and unique.")
        return
    name = input("Student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    raw = input("Enter marks separated by commas (e.g. 78, 84, 91): ")
    try:
        marks = [float(x.strip()) for x in raw.split(",") if x.strip()]
        if not marks or any(m < 0 or m > 100 for m in marks):
            raise ValueError
    except ValueError:
        print("Enter one or more numeric marks from 0 to 100.")
        return
    avg = sum(marks) / len(marks)
    students.append({"id": sid, "name": name, "marks": marks,
                     "average": avg, "grade": grade_for(avg)})
    save_students(students)
    print("Student added and saved.")

def update_marks(students):
    sid = input("Student ID to update: ").strip()
    student = next((s for s in students if s["id"] == sid), None)
    if not student:
        print("Student not found.")
        return
    raw = input("New marks separated by commas: ")
    try:
        marks = [float(x.strip()) for x in raw.split(",") if x.strip()]
        if not marks or any(m < 0 or m > 100 for m in marks):
            raise ValueError
    except ValueError:
        print("Enter one or more numeric marks from 0 to 100.")
        return
    student["marks"] = marks
    student["average"] = sum(marks) / len(marks)
    student["grade"] = grade_for(student["average"])
    save_students(students)
    print("Marks updated.")

def find_student(students):
    term = input("Search by ID or name: ").strip().lower()
    matches = [s for s in students if term in s["id"].lower() or term in s["name"].lower()]
    if matches:
        for s in matches:
            print(f'{s["id"]}: {s["name"]} | marks={s["marks"]} | average={s["average"]:.2f} | grade={s["grade"]}')
    else:
        print("No matching students.")

def export_csv(students):
    ranked = sorted(students, key=lambda s: s["average"], reverse=True)
    with CSV_FILE.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Rank", "Student ID", "Name", "Marks", "Average", "Grade"])
        for rank, s in enumerate(ranked, 1):
            writer.writerow([rank, s["id"], s["name"], ";".join(map(str, s["marks"])),
                             f'{s["average"]:.2f}', s["grade"]])
    print(f"Exported {len(ranked)} students to {CSV_FILE.resolve()}")

def main():
    students = load_students()
    actions = {
        "1": ("List students and rankings", lambda: show_students(students)),
        "2": ("Add student", lambda: add_student(students)),
        "3": ("Update student marks", lambda: update_marks(students)),
        "4": ("Search student", lambda: find_student(students)),
        "5": ("Export CSV", lambda: export_csv(students)),
        "6": ("Show class statistics", lambda: print(
            f"Students: {len(students)} | Class average: "
            f"{sum(s['average'] for s in students)/len(students):.2f}"
            if students else "No data available.")),
        "7": ("Delete student", lambda: delete_student(students)),
    }
    while True:
        print("\n=== STUDENT GRADEBOOK ===")
        for key, (label, _) in actions.items():
            print(f"{key}. {label}")
        print("0. Exit")
        choice = input("Choose: ").strip()
        if choice == "0":
            save_students(students)
            print("Saved. Goodbye!")
            break
        if choice in actions:
            actions[choice][1]()
        else:
            print("Invalid choice.")

def delete_student(students):
    sid = input("Student ID to delete: ").strip()
    for i, student in enumerate(students):
        if student["id"] == sid:
            del students[i]
            save_students(students)
            print("Student deleted.")
            return
    print("Student not found.")

if __name__ == "__main__":
    main()
