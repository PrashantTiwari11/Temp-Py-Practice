import json
from pathlib import Path

FILE = Path("todo_tasks.json")

def load_tasks():
    if not FILE.exists():
        return []
    try:
        data = json.loads(FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (OSError, json.JSONDecodeError):
        print("Could not load tasks; starting fresh.")
        return []

def save_tasks(tasks):
    FILE.write_text(json.dumps(tasks, indent=2), encoding="utf-8")

def main():
    tasks = load_tasks()
    while True:
        print("\\n1. Add  2. View  3. Complete  4. Delete  5. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            description = input("Task: ").strip()
            if description:
                tasks.append({"description": description, "completed": False})
                save_tasks(tasks)
                print("Task added.")
            else:
                print("Task cannot be empty.")
        elif choice == "2":
            if not tasks:
                print("No tasks yet.")
            for n, task in enumerate(tasks, 1):
                status = "Done" if task["completed"] else "Pending"
                print(f"{n}. [{status}] {task['description']}")
        elif choice in ("3", "4"):
            try:
                n = int(input("Task number: "))
                if not 1 <= n <= len(tasks):
                    print("Invalid task number.")
                    continue
                if choice == "3":
                    tasks[n - 1]["completed"] = True
                    print("Task marked complete.")
                else:
                    removed = tasks.pop(n - 1)
                    print("Deleted:", removed["description"])
                save_tasks(tasks)
            except ValueError:
                print("Enter a valid whole number.")
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
