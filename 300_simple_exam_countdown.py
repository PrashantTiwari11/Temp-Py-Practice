"""Project 300: Exam Countdown Calculator"""
from datetime import date

def main():
    try:
        year = int(input("Enter exam year (YYYY): "))
        month = int(input("Enter exam month (1-12): "))
        day = int(input("Enter exam day: "))
        exam_date = date(year, month, day)
    except ValueError:
        print("Please enter a valid calendar date.")
        return

    remaining = (exam_date - date.today()).days
    if remaining > 0:
        print(f"Your exam is in {remaining} day(s). Keep preparing!")
    elif remaining == 0:
        print("Your exam is today. Best of luck!")
    else:
        print(f"Your exam date was {-remaining} day(s) ago.")

if __name__ == "__main__":
    main()
