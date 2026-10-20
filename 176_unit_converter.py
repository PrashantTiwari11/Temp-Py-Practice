LENGTH={"mm":.001,"cm":.01,"m":1,"km":1000,"in":.0254,"ft":.3048,"mi":1609.344}
WEIGHT={"mg":.001,"g":1,"kg":1000,"oz":28.349523125,"lb":453.59237}
VOLUME={"ml":1,"l":1000,"tsp":4.92892159375,"tbsp":14.78676478125,"cup":236.5882365}
def main():
 while True:
  print("\nUNIT CONVERTER\n1 Length  2 Weight  3 Volume  4 Temperature  0 Exit")
  c=input("Choose: ").strip()
  if c=="0": break
  if c not in {"1","2","3","4"}: print("Invalid choice."); continue
  try: v=float(input("Value: "))
  except ValueError: print("Enter a number."); continue
  if c=="4":
   a=input("From C/F/K: ").upper().strip(); b=input("To C/F/K: ").upper().strip()
   if a not in "CFK" or b not in "CFK": print("Invalid unit."); continue
   k=v+273.15 if a=="C" else (v-32)*5/9+273.15 if a=="F" else v
   if k<0: print("Below absolute zero."); continue
   out=k-273.15 if b=="C" else (k-273.15)*9/5+32 if b=="F" else k
  else:
   units={"1":LENGTH,"2":WEIGHT,"3":VOLUME}[c]; print("Units:",", ".join(units))
   a=input("From: ").lower().strip(); b=input("To: ").lower().strip()
   if a not in units or b not in units: print("Unknown unit."); continue
   out=v*units[a]/units[b]
  print(f"{v:g} {a} = {out:.6g} {b}")
if __name__=="__main__": main()
