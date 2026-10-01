# 123_python_mini_grade_calculator.py
# Mini Grade Calculator - 10 practical features

students = {
    "Aman": [78, 82, 75, 88, 80],
    "Riya": [92, 89, 95, 91, 94],
    "Karan": [65, 70, 68, 72, 66],
    "Neha": [55, 62, 58, 64, 60],
}

print("1. Student marks:", students)

totals = {name: sum(marks) for name, marks in students.items()}
print("2. Totals:", totals)

averages = {
    name: round(sum(marks) / len(marks), 2)
    for name, marks in students.items()
}
print("3. Averages:", averages)

topper = max(averages, key=averages.get)
print("4. Topper:", topper, averages[topper])

lowest = min(averages, key=averages.get)
print("5. Lowest:", lowest, averages[lowest])

def get_grade(mark):
    if mark >= 90:
        return "A+"
    if mark >= 80:
        return "A"
    if mark >= 70:
        return "B"
    if mark >= 60:
        return "C"
    return "D"

grades = {name: get_grade(avg) for name, avg in averages.items()}
print("6. Grades:", grades)

status = {
    name: "Pass" if min(marks) >= 40 else "Fail"
    for name, marks in students.items()
}
print("7. Status:", status)

print("8. Above 80:", [name for name, avg in averages.items() if avg >= 80])

class_average = sum(averages.values()) / len(averages)
print("9. Class average:", round(class_average, 2))

print("10. Result:")
for name in students:
    print(name, "Total:", totals[name], "Average:", averages[name],
          "Grade:", grades[name], status[name])
