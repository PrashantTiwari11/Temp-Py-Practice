# 320 - Daily Task Tracker

tasks = []

print("=== Daily Task Tracker ===")
while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Mark task complete")
    print("4. Delete task")
    print("5. Exit")

    choice = input("Choose an option: ").strip()

    if choice == "1":
        task = input("Enter task: ").strip()
        if task:
            tasks.append({"task": task, "done": False})
            print("Task added.")
    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for index, task in enumerate(tasks, start=1):
                status = "✓" if task["done"] else " "
                print(f"{index}. [{status}] {task['task']}")
    elif choice == "3":
        try:
            index = int(input("Task number to complete: ")) - 1
            tasks[index]["done"] = True
            print("Task marked complete.")
        except (ValueError, IndexError):
            print("Invalid task number.")
    elif choice == "4":
        try:
            index = int(input("Task number to delete: ")) - 1
            removed = tasks.pop(index)
            print(f"Deleted: {removed['task']}")
        except (ValueError, IndexError):
            print("Invalid task number.")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Try again.")
