"""Project 288: Month Days Finder"""
import calendar

def main():
    try:
        month = int(input("Enter month number (1-12): "))
        year = int(input("Enter year: "))
    except ValueError:
        print("Please enter whole numbers.")
        return
    if not 1 <= month <= 12:
        print("Month must be between 1 and 12.")
        return
    if year < 1:
        print("Year must be greater than zero.")
        return
    days = calendar.monthrange(year, month)[1]
    print(f"{calendar.month_name[month]} {year} has {days} days.")

if __name__ == "__main__":
    main()
