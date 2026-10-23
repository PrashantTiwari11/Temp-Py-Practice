"""188 — Date calculator: date difference, add/subtract days, weekday, days until."""
from datetime import date,datetime,timedelta
def parse_date(prompt):
 raw=input(prompt).strip()
 for fmt in ("%Y-%m-%d","%d-%m-%Y"):
  try: return datetime.strptime(raw,fmt).date()
  except ValueError: pass
 raise ValueError("Use YYYY-MM-DD or DD-MM-YYYY.")
def main():
 while True:
  print("\nDATE CALCULATOR\n1 Difference 2 Add/subtract days 3 Weekday 4 Days until date 0 Exit")
  c=input("Choose: ").strip()
  try:
   if c=="1":
    a,b=parse_date("Start date: "),parse_date("End date: "); delta=(b-a).days
    print(f"Absolute difference {abs(delta)} day(s); signed difference {delta}")
   elif c=="2":
    d=parse_date("Date: "); n=int(input("Days to add (negative subtracts): ")); print(d+timedelta(days=n))
   elif c=="3":
    print(parse_date("Date: ").strftime("%A"))
   elif c=="4":
    d=parse_date("Target date: "); print((d-date.today()).days,"day(s) from today; negative means past.")
   elif c=="0": break
   else: print("Invalid choice.")
  except (ValueError,OverflowError) as e: print("Input error:",e)
if __name__=="__main__": main()
