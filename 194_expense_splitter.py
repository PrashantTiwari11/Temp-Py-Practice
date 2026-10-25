"""194 Expense Splitter: calculate balances and suggested settlements."""
def main():
 try:
  total=float(input("Total bill: ")); people=int(input("Number of people: "))
  if total<0 or people<1: raise ValueError
 except ValueError: print("Enter a non-negative bill and at least one person."); return
 print(f"Equal share of stated bill: {total/people:.2f}")
 paid=[]
 for i in range(people):
  try: x=float(input(f"Person {i+1} paid: "))
  except ValueError: print("Invalid amount."); return
  if x<0: print("Payments cannot be negative."); return
  paid.append(x)
 # Settle actual contributions to the group average, so net transfers balance.
 target=sum(paid)/people
 debtors=[[i+1,-(x-target)] for i,x in enumerate(paid) if x<target-0.005]
 creditors=[[i+1,x-target] for i,x in enumerate(paid) if x>target+0.005]
 i=j=0; print(f"Average contribution based on entered payments: {target:.2f}\nSuggested settlements:")
 while i<len(debtors) and j<len(creditors):
  amount=min(debtors[i][1],creditors[j][1])
  print(f"Person {debtors[i][0]} pays Person {creditors[j][0]}: {amount:.2f}")
  debtors[i][1]-=amount; creditors[j][1]-=amount
  if debtors[i][1]<0.01: i+=1
  if creditors[j][1]<0.01: j+=1
if __name__=="__main__": main()
