import json,csv
from pathlib import Path
from datetime import date
DB=Path("attendance.json")
def main():
 try: d=json.loads(DB.read_text())
 except (OSError,json.JSONDecodeError): d={"students":[],"records":[]}
 while True:
  print("\nATTENDANCE TRACKER\n1 Add student  2 Mark attendance  3 Report  4 CSV export  0 Exit")
  c=input("Choose: ").strip()
  if c=="1":
   name=input("Name: ").strip()
   if not name: print("Name required."); continue
   d["students"].append({"id":max((s["id"] for s in d["students"]),default=0)+1,"name":name})
   print("Added.")
  elif c=="2":
   day=input("Date YYYY-MM-DD (blank=today): ").strip() or date.today().isoformat()
   try: date.fromisoformat(day)
   except ValueError: print("Invalid date."); continue
   for s in d["students"]:
    a=input(f'{s["id"]} {s["name"]} P/A/L: ').strip().upper()
    if a in {"P","A","L"}:
     d["records"]=[r for r in d["records"] if not (r["student_id"]==s["id"] and r["date"]==day)]
     d["records"].append({"student_id":s["id"],"date":day,"status":a})
   print("Attendance updated.")
  elif c=="3":
   for s in d["students"]:
    r=[x for x in d["records"] if x["student_id"]==s["id"]]; p=sum(x["status"]=="P" for x in r)
    print(f'{s["name"]}: present {p}, absent {sum(x["status"]=="A" for x in r)}, late {sum(x["status"]=="L" for x in r)}, attendance {100*p/len(r) if r else 0:.1f}%')
  elif c=="4":
   with open("attendance_export.csv","w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=["student_id","student_name","date","status"]); w.writeheader()
    for r in d["records"]:
     s=next((x for x in d["students"] if x["id"]==r["student_id"]),{})
     w.writerow({"student_id":r["student_id"],"student_name":s.get("name",""),"date":r["date"],"status":r["status"]})
   print("Exported attendance_export.csv")
  elif c=="0": DB.write_text(json.dumps(d,indent=2)); break
  else: print("Invalid choice.")
  DB.write_text(json.dumps(d,indent=2))
if __name__=="__main__": main()
