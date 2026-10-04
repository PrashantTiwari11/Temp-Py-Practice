# 133 - Mini Habit Tracker: 10 practical features
habits = [
    {"name": "Read", "target": 7, "completed": 5},
    {"name": "Exercise", "target": 5, "completed": 4},
    {"name": "Drink water", "target": 7, "completed": 7},
    {"name": "Practice Python", "target": 6, "completed": 3},
]

# 1. Display all habits
def show_habits():
    for h in habits:
        print(f"{h['name']}: {h['completed']}/{h['target']} days")

# 2. Count tracked habits
def count_habits():
    return len(habits)

# 3. Completion percentage
def completion_percent(h):
    return round(min(h["completed"] / h["target"], 1) * 100, 1) if h["target"] > 0 else 0

# 4. Habits whose targets are met
def completed_habits():
    return [h["name"] for h in habits if h["completed"] >= h["target"]]

# 5. Habits needing improvement
def habits_to_improve():
    return [h["name"] for h in habits if h["completed"] < h["target"]]

# 6. Rank habits by progress
def rank_habits():
    return sorted(habits, key=completion_percent, reverse=True)

# 7. Add a habit
def add_habit(name, target, completed=0):
    if target <= 0 or completed < 0:
        raise ValueError("Target must be positive; completed days cannot be negative.")
    habits.append({"name": name, "target": target, "completed": completed})

# 8. Record progress
def record_progress(name, days=1):
    for h in habits:
        if h["name"].lower() == name.lower():
            h["completed"] += days
            return True
    return False

# 9. Average completion percentage
def average_completion():
    return round(sum(completion_percent(h) for h in habits) / len(habits), 1) if habits else 0

# 10. Summary report
def report():
    print("HABIT TRACKER")
    show_habits()
    print("Total habits:", count_habits())
    print("Targets met:", completed_habits())
    print("Average completion:", average_completion(), "%")

if __name__ == "__main__":
    report()
