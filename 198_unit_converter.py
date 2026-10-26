"""198 Unit converter: length, mass, and temperature."""
def main():
 while True:
  print("\nUNIT CONVERTER\n1 Length 2 Weight 3 Temperature 0 Exit")
  c=input("Choose: ").strip()
  if c=="0": break
  try:
   if c=="1":
    v=float(input("Value: ")); a=input("From (mm/cm/m/km): ").lower().strip(); b=input("To (mm/cm/m/km): ").lower().strip()
    f={"mm":.001,"cm":.01,"m":1,"km":1000}
    if a not in f or b not in f: raise ValueError("Use mm, cm, m, km.")
    print(f"{v:g} {a} = {v*f[a]/f[b]:g} {b}")
   elif c=="2":
    v=float(input("Value: ")); a=input("From (mg/g/kg): ").lower().strip(); b=input("To (mg/g/kg): ").lower().strip()
    f={"mg":.001,"g":1,"kg":1000}
    if a not in f or b not in f: raise ValueError("Use mg, g, kg.")
    print(f"{v:g} {a} = {v*f[a]/f[b]:g} {b}")
   elif c=="3":
    v=float(input("Temperature: ")); a=input("From (C/F/K): ").upper().strip(); b=input("To (C/F/K): ").upper().strip()
    k=v+273.15 if a=="C" else (v-32)*5/9+273.15 if a=="F" else v if a=="K" else None
    if k is None or k<0: raise ValueError("Use C/F/K and stay above absolute zero.")
    vals={"C":k-273.15,"F":(k-273.15)*9/5+32,"K":k}
    if b not in vals: raise ValueError("Use C/F/K.")
    print(f"{v:g}°{a} = {vals[b]:.4g}°{b}")
   else: print("Invalid choice.")
  except ValueError as e: print("Input error:",e)
if __name__=="__main__": main()
