"""155 Trip Budget — 10 features."""
expenses=[]
def add_expense(category,amount,note=""):
    if amount<0: raise ValueError("Amount cannot be negative")
    expenses.append({"category":category,"amount":round(float(amount),2),"note":note})
def total(): return round(sum(e["amount"] for e in expenses),2)
def category_totals():
    result={}
    for e in expenses: result[e["category"]]=result.get(e["category"],0)+e["amount"]
    return {k:round(v,2) for k,v in result.items()}
def remaining(budget): return round(budget-total(),2)
def over_budget(budget): return total()>budget
def largest(): return max(expenses,key=lambda e:e["amount"],default=None)
def average(): return round(total()/len(expenses),2) if expenses else 0
def by_category(category): return [e for e in expenses if e["category"].lower()==category.lower()]
def remove(index): return expenses.pop(index-1)
def export_csv(path="trip_expenses.csv"):
    import csv
    with open(path,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["category","amount","note"]); w.writeheader(); w.writerows(expenses)
if __name__=="__main__":
    add_expense("Travel",1200,"Train"); add_expense("Food",450,"Meals"); add_expense("Stay",1800,"Hotel"); budget=5000
    print("1 Expenses:",expenses); print("2 Total:",total()); print("3 Category totals:",category_totals())
    print("4 Remaining:",remaining(budget)); print("5 Over budget:",over_budget(budget))
    print("6 Largest:",largest()); print("7 Average:",average()); print("8 Food:",by_category("Food"))
    print("9 Remove with remove(index)"); print("10 Export CSV with export_csv()")
