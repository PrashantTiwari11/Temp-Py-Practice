# 107_python_mini_task_manager.py
# Mini Task Manager - 10 practical features

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add(self, title, priority="Medium"):
        self.tasks.append({"title": title, "priority": priority, "completed": False})

    def complete(self, title):
        for task in self.tasks:
            if task["title"].lower() == title.lower():
                task["completed"] = True
                return True
        return False

    def remove(self, title):
        before = len(self.tasks)
        self.tasks = [t for t in self.tasks if t["title"].lower() != title.lower()]
        return len(self.tasks) < before

    def all_tasks(self):
        return self.tasks

    def pending(self):
        return [t for t in self.tasks if not t["completed"]]

    def completed(self):
        return [t for t in self.tasks if t["completed"]]

    def search(self, keyword):
        return [t for t in self.tasks if keyword.lower() in t["title"].lower()]

    def count(self):
        return len(self.tasks)

    def completed_count(self):
        return len(self.completed())

    def completion_percentage(self):
        return self.completed_count() / self.count() * 100 if self.count() else 0


manager = TaskManager()
manager.add("Complete Python assignment", "High")
manager.add("Practice DSA", "High")
manager.add("Read IoT notes", "Medium")
manager.add("Update GitHub", "Low")
manager.complete("Practice DSA")

print("1. All tasks:", manager.all_tasks())
print("2. Pending:", manager.pending())
print("3. Completed:", manager.completed())
print("4. Search:", manager.search("Python"))
print("5. Task count:", manager.count())
print("6. Completed count:", manager.completed_count())
print("7. Completion:", manager.completion_percentage(), "%")
print("8. Remove result:", manager.remove("Update GitHub"))
print("9. Remaining:", manager.all_tasks())
print("10. Final completion:", manager.completion_percentage(), "%")
