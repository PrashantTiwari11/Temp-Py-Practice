"""182 — Inventory Manager with stock alerts and CSV export."""
import json,csv
from pathlib import Path
DB=Path("inventory.json")
def load():
 try:
  d=json.loads(DB.read_text(encoding="utf-8")); return d if isinstance(d,list) else []
 except (OSError,json.JSONDecodeError): return []
def save(d): DB.write_text(json.dumps(d,indent=2),encoding="utf-8")
def getnum(prompt):
 try:
  x=float(input(prompt))
  if x<0: raise ValueError
  return x
 except ValueError: print("Enter a non-negative number."); return None
def main():
 items=load()
 while True:
  print("\nINVENTORY\n1 List 2 Add 3 Update quantity 4 Low-stock report 5 Delete 6 Export CSV 0 Exit")
  c=input("Choose: ").strip()
  if c=="1":
   for x in items: print(f'#{x["id"]} {x["name"]}: qty={x["quantity"]:g}, price={x["price"]:.2f}, alert <= {x["threshold"]:g}')
   if not items: print("Empty inventory.")
  elif c=="2":
   name=input("Item name: ").strip()
   if not name: print("Name required."); continue
   q,p,t=getnum("Quantity: "),getnum("Unit price: "),getnum("Low-stock threshold: ")
   if None in (q,p,t): continue
   items.append({"id":max((x["id"] for x in items),default=0)+1,"name":name,"quantity":q,"price":p,"threshold":t}); save(items); print("Added.")
  elif c=="3":
   try: i=int(input("Item ID: "))
   except ValueError: print("Invalid ID."); continue
   x=next((x for x in items if x["id"]==i),None)
   if not x: print("Not found."); continue
   q=getnum("New quantity: ")
   if q is not None: x["quantity"]=q; save(items); print("Updated.")
  elif c=="4":
   low=[x for x in items if x["quantity"]<=x["threshold"]]
   for x in low: print(f'{x["name"]}: {x["quantity"]:g} left')
   if not low: print("No low-stock items.")
  elif c=="5":
   try: i=int(input("Item ID: "))
   except ValueError: print("Invalid ID."); continue
   old=len(items); items[:]=[x for x in items if x["id"]!=i]; save(items); print("Deleted." if len(items)<old else "Not found.")
  elif c=="6":
   with open("inventory_export.csv","w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=["id","name","quantity","price","threshold"]); w.writeheader(); w.writerows(items)
   print("Exported inventory_export.csv")
  elif c=="0": save(items); break
  else: print("Invalid choice.")
if __name__=="__main__": main()
