"""184 — Habit tracker with daily logs and current streaks."""
import json
from datetime import date,timedelta
from pathlib import Path
DB=Path("habits.json")
def load():
 try: return json.loads(DB.read_text(encoding="utf-8"))
 except (OSError,json.JSONDecodeError): return {"habits":[],"logs":{}}
def save(d): DB.write_text(json.dumps(d,indent=2),encoding="utf-8")
def main():
 d=load()
 while True:
  print("\nHABIT TRACKER\n1 List 2 Add 3 Log today 4 Report 5 Remove 0 Exit")
  c=input("Choose: ").strip()
  if c=="1":
   for i,h in enumerate(d["habits"],1): print(i,h)
   if not d["habits"]: print("No habits.")
  elif c=="2":
   h=input("Habit name: ").strip()
   if not h: print("Name required."); continue
   if any(h.casefold()==x.casefold() for x in d["habits"]): print("Already exists."); continue
   d["habits"].append(h); save(d); print("Added.")
  elif c=="3":
   day=date.today().isoformat(); d["logs"].setdefault(day,[])
   for h in d["habits"]:
    a=input(f"Completed {h}? y/n: ").strip().lower()
    if a in {"y","yes"} and h not in d["logs"][day]: d["logs"][day].append(h)
    if a in {"n","no"} and h in d["logs"][day]: d["logs"][day].remove(h)
   save(d); print("Logged.")
  elif c=="4":
   for h in d["habits"]:
    days=[day for day,done in d["logs"].items() if h in done]; streak=0; cursor=date.today()
    while cursor.isoformat() in days: streak+=1; cursor-=timedelta(days=1)
    print(f"{h}: {len(days)} completed day(s), current streak {streak}")
   if not d["habits"]: print("No habits.")
  elif c=="5":
   h=input("Exact habit name: ").strip()
   if h not in d["habits"]: print("Not found."); continue
   d["habits"].remove(h)
   for day in d["logs"]: d["logs"][day]=[x for x in d["logs"][day] if x!=h]
   save(d); print("Removed.")
  elif c=="0": save(d); break
  else: print("Invalid choice.")
if __name__=="__main__": main()
