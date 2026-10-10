"""149 Study Planner: 10 practical features."""
from datetime import date
tasks = []
def add_task(subject, topic, due, minutes):
    tasks.append({"subject": subject, "topic": topic, "due": due, "minutes": minutes, "done": False})
def list_tasks():
    for i, t in enumerate(tasks, 1): print(i, t)
def mark_done(index): tasks[index-1]["done"] = True
def pending_minutes(): return sum(t["minutes"] for t in tasks if not t["done"])
def by_subject(subject): return [t for t in tasks if t["subject"].lower() == subject.lower()]
def overdue(today=None): return [t for t in tasks if not t["done"] and t["due"] < (today or date.today().isoformat())]
def daily_plan(limit=180):
    result, total = [], 0
    for t in tasks:
        if not t["done"] and total + t["minutes"] <= limit: result.append(t); total += t["minutes"]
    return result
def completion(): return round(100*sum(t["done"] for t in tasks)/len(tasks), 1) if tasks else 0
def remove_task(index): return tasks.pop(index-1)
def save_report(path="study_plan.txt"):
    with open(path, "w", encoding="utf-8") as f:
        for t in tasks: f.write(str(t)+"\n")
if __name__ == "__main__":
    add_task("Python", "Functions", date.today().isoformat(), 45)
    add_task("IoT", "MQTT revision", date.today().isoformat(), 30)
    print("1 List tasks"); list_tasks()
    print("2 Pending minutes:", pending_minutes())
    print("3 Python tasks:", by_subject("Python"))
    print("4 Overdue:", overdue())
    print("5 Suggested daily plan:", daily_plan())
    mark_done(1); print("6 Completion:", completion(), "%")
    print("7 Pending minutes now:", pending_minutes())
    print("8 Remove task with remove_task(index)")
    print("9 Save report with save_report()")
    print("10 Add tasks with add_task(subject, topic, due, minutes)")
