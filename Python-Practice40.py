# Day 9 - 34: Date and Time Calculations
from datetime import date, datetime, timedelta

# 1. Current date and time
def now():
    return datetime.now()

# 2. Format a date
def format_date(d):
    return d.strftime("%d-%m-%Y")

# 3. Calculate age
def age(dob):
    today = date.today()
    years = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        years -= 1
    return years

# 4. Add days
def add_days(d, days):
    return d + timedelta(days=days)

# 5. Difference between dates
def date_difference(a, b):
    return abs((b-a).days)

# 6. Day name
def day_name(d):
    return d.strftime("%A")

# 7. Parse datetime text
def parse_datetime(text):
    return datetime.strptime(text, "%Y-%m-%d %H:%M")

# 8. Count weekdays
def weekdays(start, end):
    count = 0
    current = start
    while current <= end:
        count += current.weekday() < 5
        current += timedelta(days=1)
    return count

# 9. Days until a target date
def days_until(target):
    return (target-date.today()).days

# 10. Time duration
def duration(start, end):
    return end-start

if __name__ == "__main__":
    print(now())
    print(format_date(date.today()))
    print(age(date(2000,1,1)))
    print(add_days(date.today(), 30))
    print(date_difference(date(2026,1,1), date(2026,12,31)))
    print(day_name(date.today()))
    print(parse_datetime("2026-09-07 21:30"))
    print(weekdays(date(2026,9,1), date(2026,9,10)))
    print(days_until(date(2026,12,31)))
    print(duration(datetime(2026,9,7,9), datetime(2026,9,7,17)))
