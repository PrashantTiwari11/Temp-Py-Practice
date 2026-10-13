"""Mini Event Planner: 10 features."""
from datetime import date
import csv

events = []
def add_event(title, event_date, category="General", location="TBD"):  # 1
    event = {"title": title, "date": event_date, "category": category, "location": location}
    events.append(event)
    return event
def list_events():  # 2
    return sorted(events, key=lambda e: e["date"])
def search_events(keyword):  # 3
    k = keyword.casefold()
    return [e for e in events if k in e["title"].casefold() or k in e["location"].casefold()]
def filter_by_category(category):  # 4
    return [e for e in events if e["category"].casefold() == category.casefold()]
def filter_by_date(day):  # 5
    return [e for e in events if e["date"] == day]
def update_location(title, location):  # 6
    for e in events:
        if e["title"].casefold() == title.casefold():
            e["location"] = location
            return True
    return False
def remove_event(title):  # 7
    for e in events:
        if e["title"].casefold() == title.casefold():
            events.remove(e)
            return True
    return False
def upcoming_events(from_date=None):  # 8
    day = from_date or date.today().isoformat()
    return [e for e in list_events() if e["date"] >= day]
def event_count():  # 9
    return len(events)
def export_csv(filename="events.csv"):  # 10
    with open(filename, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["title", "date", "category", "location"])
        w.writeheader()
        w.writerows(list_events())
    return filename

if __name__ == "__main__":
    add_event("Python Practice", "2026-10-15", "Learning", "Home")
    add_event("Team Meeting", "2026-10-14", "Work", "Online")
    print(list_events())
    print("Upcoming:", upcoming_events())
    print("Count:", event_count())
