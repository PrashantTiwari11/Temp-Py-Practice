"""189 Contact Book."""
import json,csv
from pathlib import Path
DB=Path("contacts.json")
def load():
 try:
  d=json.loads(DB.read_text(encoding="utf-8")); return d if isinstance(d,list) else []
 except (OSError,json.JSONDecodeError): return []
def save(d): DB.write_text(json.dumps(d,indent=2,ensure_ascii=False),encoding="utf-8")
def main():
 d=load()
 while True:
  print("\nCONTACT BOOK\n1 List 2 Add 3 Search 4 Edit 5 Delete 6 Export CSV 0 Exit")
  c=input("Choose: ").strip()
  if c=="1":
   for x in d: print(f'#{x["id"]} {x["name"]} | {x["phone"]} | {x["email"]}')
   if not d: print("No contacts.")
  elif c=="2":
   n=input("Name: ").strip(); p=input("Phone: ").strip(); e=input("Email: ").strip()
   if not n: print("Name required."); continue
   d.append({"id":max((x["id"] for x in d),default=0)+1,"name":n,"phone":p,"email":e}); save(d); print("Saved.")
  elif c=="3":
   q=input("Search: ").casefold(); found=[x for x in d if q in x["name"].casefold() or q in x["phone"].casefold() or q in x["email"].casefold()]
   for x in found: print(x)
   if not found: print("No matches.")
  elif c=="4":
   try: i=int(input("Contact ID: "))
   except ValueError: print("Invalid ID."); continue
   x=next((x for x in d if x["id"]==i),None)
   if not x: print("Not found."); continue
   for k in ("name","phone","email"):
    v=input(f'{k.title()} [{x[k]}]: ').strip()
    if v: x[k]=v
   save(d); print("Updated.")
  elif c=="5":
   try: i=int(input("Contact ID: "))
   except ValueError: print("Invalid ID."); continue
   n=len(d); d[:]=[x for x in d if x["id"]!=i]; save(d); print("Deleted." if len(d)<n else "Not found.")
  elif c=="6":
   with open("contacts_export.csv","w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=["id","name","phone","email"]); w.writeheader(); w.writerows(d)
   print("Exported contacts_export.csv")
  elif c=="0": save(d); break
  else: print("Invalid choice.")
if __name__=="__main__": main()
