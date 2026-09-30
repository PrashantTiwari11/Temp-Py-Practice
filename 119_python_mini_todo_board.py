# 119_python_mini_todo_board.py
# Mini To-Do Board - 10 practical features
tasks=[{"title":"Study Python","priority":"High","done":False},{"title":"Complete IoT assignment","priority":"High","done":True},{"title":"Practice DSA","priority":"Medium","done":False},{"title":"Read AWS notes","priority":"Low","done":False}]
print("1. Tasks:",tasks)
print("2. Total:",len(tasks))
print("3. Pending:",[t["title"] for t in tasks if not t["done"]])
print("4. Completed:",[t["title"] for t in tasks if t["done"]])
print("5. High priority:",[t["title"] for t in tasks if t["priority"]=="High"])
tasks[0]["done"]=True; print("6. Completed task:",tasks[0]["title"])
tasks.append({"title":"Practice SQL","priority":"Medium","done":False}); print("7. Added:",tasks[-1])
tasks=[t for t in tasks if t["title"]!="Complete IoT assignment"]; print("8. After removal:",tasks)
completed=sum(t["done"] for t in tasks); print("9. Completion rate:",round(completed/len(tasks)*100,2),"%")
print("10. Summary:",{"total":len(tasks),"completed":completed,"pending":len(tasks)-completed,"high_priority":sum(t["priority"]=="High" for t in tasks)})
