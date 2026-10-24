"""192 Loan EMI calculator; estimates only."""
def main():
 while True:
  print("\nLOAN CALCULATOR\n1 Calculate EMI 0 Exit")
  c=input("Choose: ").strip()
  if c=="0": break
  if c!="1": print("Invalid choice."); continue
  try:
   principal=float(input("Loan amount: ")); annual=float(input("Annual interest rate (%): ")); years=float(input("Term in years: "))
   if principal<=0 or annual<0 or years<=0: raise ValueError
  except ValueError: print("Enter a positive amount and term, and non-negative rate."); continue
  months=round(years*12); r=annual/1200
  emi=principal/months if r==0 else principal*r*(1+r)**months/((1+r)**months-1)
  total=emi*months
  print(f"Monthly EMI: {emi:,.2f}\nPayments: {months}\nTotal repayment: {total:,.2f}\nTotal interest: {total-principal:,.2f}")
  print("Estimate only; lender fees and rounding may differ.")
if __name__=="__main__": main()
