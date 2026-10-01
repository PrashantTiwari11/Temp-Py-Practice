# 121_python_mini_employee_manager.py
# Mini Employee Manager - 10 practical features

employees = [
    {"id": 101, "name": "Amit", "department": "IT", "salary": 45000},
    {"id": 102, "name": "Riya", "department": "HR", "salary": 40000},
    {"id": 103, "name": "Karan", "department": "IT", "salary": 55000},
    {"id": 104, "name": "Neha", "department": "Finance", "salary": 48000},
]

print("1. Employees:", employees)
print("2. Employee count:", len(employees))

keyword = "riya"
print("3. Name search:", [e for e in employees if keyword in e["name"].lower()])

department = "IT"
print("4. IT employees:", [e["name"] for e in employees if e["department"] == department])

limit = 45000
print("5. Salary above 45000:", [e["name"] for e in employees if e["salary"] > limit])

highest = max(employees, key=lambda e: e["salary"])
print("6. Highest salary:", highest["name"], highest["salary"])

lowest = min(employees, key=lambda e: e["salary"])
print("7. Lowest salary:", lowest["name"], lowest["salary"])

average = sum(e["salary"] for e in employees) / len(employees)
print("8. Average salary:", round(average, 2))

employees.append({"id": 105, "name": "Priya", "department": "IT", "salary": 50000})
print("9. Added employee:", employees[-1])

summary = {}
for e in employees:
    summary[e["department"]] = summary.get(e["department"], 0) + 1
print("10. Department summary:", summary)
