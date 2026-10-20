"""Educational banking demo only; not real banking software."""
import json,csv
from pathlib import Path
from datetime import datetime
DB=Path("bank_demo.json")
def main():
 try: d=json.loads(DB.read_text())
 except (OSError,json.JSONDecodeError): d={"balance":0.0,"transactions":[]}
 while True:
  print(f'\nBANK DEMO | Balance {d["balance"]:.2f}\n1 Deposit  2 Withdraw  3 History  4 Export CSV  0 Exit')
  c=input("Choose: ").strip()
  if c in ("1","2"):
   try: a=round(float(input("Amount: ")),2); assert a>0
   except (ValueError,AssertionError): print("Enter a positive amount."); continue
   if c=="2" and a>d["balance"]: print("Insufficient demo balance."); continue
   d["balance"]=round(d["balance"]+(a if c=="1" else -a),2)
   d["transactions"].append({"time":datetime.now().isoformat(timespec="seconds"),"type":"Deposit" if c=="1" else "Withdrawal","amount":a,"balance":d["balance"],"note":input("Note: ").strip()})
   DB.write_text(json.dumps(d,indent=2)); print("Recorded.")
  elif c=="3":
   for t in d["transactions"]: print(t)
   if not d["transactions"]: print("No transactions.")
  elif c=="4":
   with open("bank_history.csv","w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=["time","type","amount","balance","note"]); w.writeheader(); w.writerows(d["transactions"])
   print("Exported bank_history.csv")
  elif c=="0": DB.write_text(json.dumps(d,indent=2)); break
  else: print("Invalid choice.")
if __name__=="__main__": main()
