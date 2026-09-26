# 102_python_student_gradebook.py
# Student Gradebook - 10 practical features

students = {
    "Prashant": [85, 78, 92],
    "Aman": [72, 68, 80],
    "Riya": [91, 88, 95],
    "Neha": [65, 74, 70],
}

print("1. Students:", list(students))
averages = {name: sum(marks) / len(marks) for name, marks in students.items()}
print("2. Averages:", averages)
topper = max(averages, key=averages.get)
print("3. Topper:", topper, averages[topper])
lowest = min(averages, key=averages.get)
print("4. Lowest:", lowest, averages[lowest])

def grade(avg):
    if avg >= 90: return "A+"
    if avg >= 80: return "A"
    if avg >= 70: return "B"
    if avg >= 60: return "C"
    return "D"

print("5. Grades:", {n: grade(a) for n, a in averages.items()})
print("6. Above 80:", [n for n, a in averages.items() if a >= 80])
print("7. Class average:", round(sum(averages.values()) / len(averages), 2))
print("8. Highest mark:", max(max(m) for m in students.values()))
print("9. Passed students:", sum(a >= 40 for a in averages.values()))
report = {n: {"marks": m, "average": round(averages[n], 2), "grade": grade(averages[n])}
          for n, m in students.items()}
print("10. Grade report:", report)
