"""181 — JSON Notes App."""
import json, csv
from pathlib import Path
from datetime import datetime
DB=Path("notes.json")
def load():
 try:
  d=json.loads(DB.read_text(encoding="utf-8")); return d if isinstance(d,list) else []
 except (OSError,json.JSONDecodeError): return []
def save(d): DB.write_text(json.dumps(d,indent=2,ensure_ascii=False),encoding="utf-8")
def main():
 notes=load()
 while True:
  print("\nNOTES APP\n1 List 2 Add 3 Search 4 Edit 5 Delete 6 Export CSV 0 Exit")
  c=input("Choose: ").strip()
  if c=="1":
   for n in notes: print(f'#{n["id"]} {n["title"]} [{n["created"]}]\n{n["body"]}')
   if not notes: print("No notes.")
  elif c=="2":
   title=input("Title: ").strip(); body=input("Note: ").strip()
   if not title or not body: print("Both required."); continue
   notes.append({"id":max((n["id"] for n in notes),default=0)+1,"title":title,"body":body,"created":datetime.now().isoformat(timespec="seconds")}); save(notes); print("Saved.")
  elif c=="3":
   term=input("Search: ").casefold(); found=[n for n in notes if term in n["title"].casefold() or term in n["body"].casefold()]
   for n in found: print(f'#{n["id"]} {n["title"]}: {n["body"]}')
   if not found: print("No matches.")
  elif c=="4":
   try: i=int(input("Note ID: "))
   except ValueError: print("Invalid ID."); continue
   n=next((x for x in notes if x["id"]==i),None)
   if not n: print("Not found."); continue
   t=input(f'Title [{n["title"]}]: ').strip(); b=input("New body (blank keeps): ").strip()
   if t: n["title"]=t
   if b: n["body"]=b
   save(notes); print("Updated.")
  elif c=="5":
   try: i=int(input("Note ID: "))
   except ValueError: print("Invalid ID."); continue
   old=len(notes); notes[:]=[n for n in notes if n["id"]!=i]; save(notes); print("Deleted." if len(notes)<old else "Not found.")
  elif c=="6":
   with open("notes_export.csv","w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=["id","title","body","created"]); w.writeheader(); w.writerows(notes)
   print("Exported notes_export.csv")
  elif c=="0": save(notes); break
  else: print("Invalid choice.")
if __name__=="__main__": main()
