"""220 - Markdown To-Do Manager. Saves tasks in tasks.md."""
from pathlib import Path
from datetime import date

FILE = Path("tasks.md")

def add_task():
    task = input("Enter task: ").strip()
    if not task:
        print("Task cannot be empty.")
        return
    if not FILE.exists():
        FILE.write_text(f"# To-Do List - {date.today()}\n\n", encoding="utf-8")
    with FILE.open("a", encoding="utf-8") as handle:
        handle.write(f"- [ ] {task}\n")
    print("Task added.")

def show_tasks():
    if FILE.exists():
        print(FILE.read_text(encoding="utf-8"))
    else:
        print("No tasks saved yet.")

def main():
    while True:
        print("\n1. Add task\n2. View tasks\n3. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            break
        else:
            print("Choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
