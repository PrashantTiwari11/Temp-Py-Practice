"""Classify a score into a simple grade band."""
def main():
    try:
        score = float(input("Enter score (0 to 100): "))
        if not 0 <= score <= 100:
            print("Score must be between 0 and 100.")
            return
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
        print(f"Grade: {grade}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
