"""Calculate age in years, months, and days from a birth date."""
from datetime import date
import calendar

def main():
    text = input("Date of birth (YYYY-MM-DD): ").strip()
    try:
        birth = date.fromisoformat(text)
        today = date.today()
        if birth > today:
            print("Date of birth cannot be in the future.")
            return
        years = today.year - birth.year
        months = today.month - birth.month
        days = today.day - birth.day
        if days < 0:
            months -= 1
            prev_month = today.month - 1 or 12
            prev_year = today.year if today.month > 1 else today.year - 1
            days += calendar.monthrange(prev_year, prev_month)[1]
        if months < 0:
            years -= 1
            months += 12
        print(f"Age: {years} years, {months} months, {days} days")
    except ValueError:
        print("Invalid date. Use YYYY-MM-DD.")

if __name__ == "__main__":
    main()
