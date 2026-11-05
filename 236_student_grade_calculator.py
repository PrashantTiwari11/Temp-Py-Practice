def calculate_grade(average):
    if average >= 90:
        return "A+"
    if average >= 80:
        return "A"
    if average >= 70:
        return "B"
    if average >= 60:
        return "C"
    if average >= 40:
        return "D"
    return "F"

def main():
    name = input("Student name: ").strip() or "Student"
    try:
        count = int(input("Number of subjects: "))
        if count <= 0:
            raise ValueError
        marks = []
        for index in range(count):
            mark = float(input(f"Marks for subject {index + 1} (0-100): "))
            if not 0 <= mark <= 100:
                raise ValueError
            marks.append(mark)
    except ValueError:
        print("Enter a positive subject count and marks from 0 to 100.")
        return

    total = sum(marks)
    average = total / count
    passed = all(mark >= 40 for mark in marks)
    print(f"\nResult for {name}")
    print(f"Total: {total:g}/{count * 100}")
    print(f"Average: {average:.2f}%")
    print(f"Grade: {calculate_grade(average)}")
    print("Status:", "Pass" if passed else "Needs improvement")

if __name__ == "__main__":
    main()
