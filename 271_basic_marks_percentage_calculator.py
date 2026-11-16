"""Calculate total marks, percentage, and average for subjects."""
def main():
    try:
        count = int(input("Number of subjects: "))
        if count < 1:
            print("Enter at least one subject.")
            return
        marks = []
        for index in range(1, count + 1):
            score = float(input(f"Marks for subject {index} (out of 100): "))
            if not 0 <= score <= 100:
                print("Marks must be between 0 and 100.")
                return
            marks.append(score)
        total = sum(marks)
        print(f"Total: {total:g}/{count * 100}")
        print(f"Percentage: {total / count:.2f}%")
        print(f"Average: {total / count:.2f}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
