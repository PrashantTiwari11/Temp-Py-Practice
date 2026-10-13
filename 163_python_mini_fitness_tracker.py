"""Mini Fitness Tracker: 10 features."""
from datetime import date
import csv

activities = []
def log_activity(activity, minutes, calories=0, day=None):  # 1
    if minutes <= 0 or calories < 0:
        raise ValueError("Minutes must be positive and calories non-negative.")
    e = {"activity": activity, "minutes": int(minutes), "calories": float(calories),
         "date": day or date.today().isoformat()}
    activities.append(e)
    return e
def list_activities():  # 2
    return sorted(activities, key=lambda e: e["date"])
def total_minutes():  # 3
    return sum(e["minutes"] for e in activities)
def total_calories():  # 4
    return sum(e["calories"] for e in activities)
def filter_by_activity(name):  # 5
    return [e for e in activities if e["activity"].casefold() == name.casefold()]
def filter_by_date(day):  # 6
    return [e for e in activities if e["date"] == day]
def activity_summary():  # 7
    result = {}
    for e in activities:
        result[e["activity"]] = result.get(e["activity"], 0) + e["minutes"]
    return result
def goal_progress(goal_minutes):  # 8
    if goal_minutes <= 0:
        raise ValueError("Goal must be positive.")
    return min(100.0, total_minutes() / goal_minutes * 100)
def longest_activity():  # 9
    return max(activities, key=lambda e: e["minutes"], default=None)
def export_csv(filename="fitness_log.csv"):  # 10
    with open(filename, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["activity", "minutes", "calories", "date"])
        w.writeheader()
        w.writerows(list_activities())
    return filename

if __name__ == "__main__":
    log_activity("Walking", 30, 120)
    log_activity("Cycling", 45, 280)
    print(list_activities())
    print("Minutes:", total_minutes(), "Calories:", total_calories())
    print("Goal progress:", f"{goal_progress(150):.1f}%")
