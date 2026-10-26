"""197 To-do list with JSON persistence."""
import json
from pathlib import Path
from datetime import date
DB=Path("todo_tasks.json")
def load():
 try:
  d=json.loads(DB.read_text(encoding="utf-8")); return d if isinstance(d,list) else []
 except (OSError,json.JSONDecodeError): return []
def save(d): DB.write_text(json.dumps(d,indent=2,ensure_ascii=False),encoding="utf-8")
def main():
 tasks=load()
 while True:
  print("\nTO-DO LIST\n1 List 2 Add 3 Complete/reopen 4 Delete 0 Exit")
  c=input("Choose: ").strip()
  if c=="1":
   for t in tasks: print(f'#{t["id"]} [{"x" if t["done"] else " "}] {t["title"]} | {t["priority"]} | due {t["due"] or "-"}')
   if not tasks: print("No tasks.")
  elif c=="2":
   title=input("Title: ").strip()
   if not title: print("Title required."); continue
   priority=input("Priority low/medium/high [medium]: ").strip().lower() or "medium"
   if priority not in {"low","medium","high"}: print("Invalid priority."); continue
   due=input("Due date YYYY-MM-DD (optional): ").strip()
   if due:
    try: date.fromisoformat(due)
    except ValueError: print("Invalid date."); continue
   tasks.append({"id":max((t["id"] for t in tasks),default=0)+1,"title":title,"priority":priority,"due":due,"done":False}); save(tasks); print("Added.")
  elif c=="3":
   try: i=int(input("Task ID: "))
   except ValueError: print("Invalid ID."); continue
   t=next((t for t in tasks if t["id"]==i),None)
   if t: t["done"]=not t["done"]; save(tasks); print("Updated.")
   else: print("Not found.")
  elif c=="4":
   try: i=int(input("Task ID: "))
   except ValueError: print("Invalid ID."); continue
   n=len(tasks); tasks[:]=[t for t in tasks if t["id"]!=i]; save(tasks); print("Deleted." if len(tasks)<n else "Not found.")
  elif c=="0": save(tasks); break
  else: print("Invalid choice.")
if __name__=="__main__": main()
