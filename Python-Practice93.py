# 88_python_mini_student_management.py
# Mini Student Management System - 10 practical features

class StudentManager:
    def __init__(self): self.students = {}
    def add(self, roll, name, marks):
        self.students[roll] = {"name": name, "marks": marks}
    def remove(self, roll): return self.students.pop(roll, None)
    def update_marks(self, roll, marks):
        if roll in self.students:
            self.students[roll]["marks"] = marks
            return True
        return False
    def find(self, roll): return self.students.get(roll)
    def average(self):
        return sum(x["marks"] for x in self.students.values()) / len(self.students) if self.students else 0
    def topper(self):
        return max(self.students.items(), key=lambda x: x[1]["marks"], default=None)
    def above(self, threshold):
        return {r: s for r, s in self.students.items() if s["marks"] >= threshold}
    def grade(self, marks):
        if marks >= 90: return "A+"
        if marks >= 80: return "A"
        if marks >= 70: return "B"
        if marks >= 60: return "C"
        return "D"
    def display(self):
        for r, s in self.students.items():
            print(r, s["name"], s["marks"], self.grade(s["marks"]))
    def count(self): return len(self.students)

m = StudentManager()
m.add("101", "Prashant", 85)
m.add("102", "Aman", 72)
m.add("103", "Riya", 91)
m.add("104", "Neha", 78)

print("1. All students:")
m.display()
print("2. Count:", m.count())
print("3. Find 101:", m.find("101"))
m.update_marks("102", 80)
print("4. Updated 102:", m.find("102"))
print("5. Average:", m.average())
print("6. Topper:", m.topper())
print("7. Students >= 80:", m.above(80))
print("8. Grade 85:", m.grade(85))
print("9. Removed:", m.remove("104"))
print("10. Final count:", m.count())
