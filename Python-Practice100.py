# 98_python_datetime_scheduler.py
# Date and Time Utilities - 10 practical features
from datetime import datetime, date, timedelta, timezone

now = datetime.now()
print("1. Now:", now)
print("2. Date:", now.date())
print("3. Time:", now.time())
print("4. Formatted:", now.strftime("%d-%m-%Y %H:%M:%S"))

exam_date = datetime.strptime("25-12-2026", "%d-%m-%Y")
print("5. Parsed date:", exam_date.date())
print("6. After 7 days:", (now + timedelta(days=7)).date())

birth = date(2005, 1, 1)
print("7. Days since sample date:", (date.today() - birth).days)
print("8. Weekday:", now.strftime("%A"))

tasks = {
    (now + timedelta(days=1)).date(): "Python practice",
    (now + timedelta(days=2)).date(): "DSA practice",
    (now + timedelta(days=3)).date(): "Project work"
}
print("9. Schedule:", tasks)
print("10. UTC:", datetime.now(timezone.utc))
