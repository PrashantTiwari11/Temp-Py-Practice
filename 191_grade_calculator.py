"""191 Grade Calculator."""
def grade(p):
 return "A" if p>=90 else "B" if p>=80 else "C" if p>=70 else "D" if p>=60 else "E" if p>=50 else "F"
def main():
 rows=[]
 while True:
  print("\nGRADE CALCULATOR\n1 Add subject 2 Report 3 Clear 0 Exit")
  c=input("Choose: ").strip()
  if c=="1":
   name=input("Subject: ").strip()
   try: got=float(input("Marks obtained: ")); maximum=float(input("Maximum marks: "))
   except ValueError: print("Enter numeric marks."); continue
   if not name or maximum<=0 or got<0 or got>maximum: print("Invalid input."); continue
   rows.append((name,got,maximum)); print("Added.")
  elif c=="2":
   if not rows: print("Add subjects first."); continue
   for n,g,m in rows: print(f"{n}: {g:g}/{m:g} = {100*g/m:.2f}% grade {grade(100*g/m)}")
   got=sum(r[1] for r in rows); maximum=sum(r[2] for r in rows); p=100*got/maximum
   print(f"Overall: {got:g}/{maximum:g} = {p:.2f}% grade {grade(p)}")
  elif c=="3":
   if input("Clear all subjects? y/n: ").lower().strip() in {"y","yes"}: rows.clear(); print("Cleared.")
  elif c=="0": break
  else: print("Invalid choice.")
if __name__=="__main__": main()
