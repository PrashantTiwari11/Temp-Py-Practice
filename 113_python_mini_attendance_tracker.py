# 113_python_mini_attendance_tracker.py
# Mini Attendance Tracker - 10 practical features

students = {
    "Prashant": {"present": 18, "total": 20},
    "Aman": {"present": 16, "total": 20},
    "Riya": {"present": 19, "total": 20},
    "Neha": {"present": 14, "total": 20},
}

# 1. Display all students
print("1. Students:", list(students))

# 2. Calculate attendance percentage
for name, data in students.items():
    data["percentage"] = round(data["present"] / data["total"] * 100, 2)
print("2. Attendance:", {n: d["percentage"] for n, d in students.items()})

# 3. Students above 75%
print("3. Above 75%:", [n for n, d in students.items() if d["percentage"] >= 75])

# 4. Students below 75%
print("4. Below 75%:", [n for n, d in students.items() if d["percentage"] < 75])

# 5. Mark a student present
students["Neha"]["present"] += 1
students["Neha"]["total"] += 1
students["Neha"]["percentage"] = round(
    students["Neha"]["present"] / students["Neha"]["total"] * 100, 2
)
print("5. Updated Neha:", students["Neha"])

# 6. Mark a student absent
students["Aman"]["total"] += 1
students["Aman"]["percentage"] = round(
    students["Aman"]["present"] / students["Aman"]["total"] * 100, 2
)
print("6. Updated Aman:", students["Aman"])

# 7. Class average attendance
average = sum(d["percentage"] for d in students.values()) / len(students)
print("7. Class average:", round(average, 2))

# 8. Highest attendance
top = max(students, key=lambda n: students[n]["percentage"])
print("8. Highest attendance:", top)

# 9. Lowest attendance
low = min(students, key=lambda n: students[n]["percentage"])
print("9. Lowest attendance:", low)

# 10. Attendance report
print("10. Report:")
for name, data in students.items():
    status = "Eligible" if data["percentage"] >= 75 else "Shortage"
    print(name, data["percentage"], status)
