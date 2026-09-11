"""52 - Mini Project: Task Manager with 10 practical features"""

class TaskManager:
    def __init__(self):
        self.tasks, self.next_id = [], 1

    # 1. Add task
    def add_task(self, title, priority="Medium"):
        task = {"id":self.next_id, "title":title, "priority":priority, "completed":False}
        self.tasks.append(task); self.next_id += 1
        return task

    # 2. List tasks
    def list_tasks(self): return self.tasks

    # 3. Complete task
    def complete(self, task_id):
        task = self.get(task_id)
        if task: task["completed"] = True
        return bool(task)

    # 4. Delete task
    def delete(self, task_id):
        old = len(self.tasks)
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        return len(self.tasks) < old

    # 5. Find task
    def get(self, task_id):
        return next((t for t in self.tasks if t["id"] == task_id), None)

    # 6. Search by keyword
    def search(self, keyword):
        return [t for t in self.tasks if keyword.lower() in t["title"].lower()]

    # 7. Filter by priority
    def by_priority(self, priority):
        return [t for t in self.tasks if t["priority"].lower() == priority.lower()]

    # 8. Pending tasks
    def pending(self): return [t for t in self.tasks if not t["completed"]]

    # 9. Completed tasks
    def completed(self): return [t for t in self.tasks if t["completed"]]

    # 10. Summary
    def summary(self):
        done = sum(t["completed"] for t in self.tasks)
        return {"total":len(self.tasks), "completed":done, "pending":len(self.tasks)-done}

if __name__ == "__main__":
    tm = TaskManager()
    tm.add_task("Learn Python", "High")
    tm.add_task("Practice DSA", "High")
    tm.add_task("Read documentation", "Low")
    tm.add_task("Build GitHub project", "Medium")
    tm.complete(1)

    print("1. All:", tm.list_tasks())
    print("2. Search:", tm.search("python"))
    print("3. High:", tm.by_priority("High"))
    print("4. Pending:", tm.pending())
    print("5. Completed:", tm.completed())
    print("6. Summary:", tm.summary())
    print("7. Task #2:", tm.get(2))
    print("8. Delete #3:", tm.delete(3))
    print("9. Remaining:", tm.list_tasks())
    tm.add_task("Push project to GitHub", "Medium")
    print("10. Final:", tm.summary())
