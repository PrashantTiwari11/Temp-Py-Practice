import json
from pathlib import Path
DB=Path("tasks.json")
def main():
 try: tasks=json.loads(DB.read_text())
 except (OSError,json.JSONDecodeError): tasks=[]
 while True:
  print("\nTO-DO MANAGER\n1 List  2 Add  3 Complete  4 Delete  0 Exit")
  c=input("Choose: ").strip()
  if c=="1":
   for t in tasks: print(f'{t["id"]}. [{"x" if t["done"] else " "}] {t["title"]} | {t["priority"]} | due {t["due"] or "-"}')
   if not tasks: print("No tasks.")
  elif c=="2":
   title=input("Task: ").strip(); p=input("Priority low/medium/high: ").lower().strip() or "medium"; due=input("Due date (optional): ").strip()
   if not title or p not in {"low","medium","high"}: print("Invalid title/priority."); continue
   tasks.append({"id":max((t["id"] for t in tasks),default=0)+1,"title":title,"priority":p,"due":due,"done":False})
   DB.write_text(json.dumps(tasks,indent=2)); print("Saved.")
  elif c=="3":
   try: i=int(input("Task ID: "))
   except ValueError: print("Invalid ID."); continue
   t=next((x for x in tasks if x["id"]==i),None)
   if t: t["done"]=True; DB.write_text(json.dumps(tasks,indent=2)); print("Completed.")
   else: print("Not found.")
  elif c=="4":
   try: i=int(input("Task ID: "))
   except ValueError: print("Invalid ID."); continue
   tasks[:]=[t for t in tasks if t["id"]!=i]; DB.write_text(json.dumps(tasks,indent=2)); print("Deleted if it existed.")
  elif c=="0": DB.write_text(json.dumps(tasks,indent=2)); break
  else: print("Invalid choice.")
if __name__=="__main__": main()
