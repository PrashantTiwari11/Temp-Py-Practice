# 142 - Mini Expense Splitter: 10 practical features
people=['Aman','Riya','Prashant']; expenses=[{'paid_by':'Aman','description':'Dinner','amount':1200},{'paid_by':'Riya','description':'Tickets','amount':900},{'paid_by':'Prashant','description':'Cab','amount':600}]
# 1. Display expenses
def show_expenses():
    for e in expenses: print(f"{e['paid_by']} paid Rs {e['amount']:.2f} for {e['description']}")
# 2. Total expense
def total_expense(): return sum(e['amount'] for e in expenses)
# 3. Equal share
def equal_share(): return total_expense()/len(people) if people else 0
# 4. Amount paid by each person
def paid_by_person():
    r={p:0 for p in people}
    for e in expenses: r[e['paid_by']]=r.get(e['paid_by'],0)+e['amount']
    return r
# 5. Balances
def balances(): return {p:round(paid_by_person().get(p,0)-equal_share(),2) for p in people}
# 6. Add expense
def add_expense(paid_by,description,amount): expenses.append({'paid_by':paid_by,'description':description,'amount':float(amount)})
# 7. Add person
def add_person(name):
    if name and name not in people: people.append(name)
# 8. Biggest expense
def biggest_expense(): return max(expenses,key=lambda e:e['amount'],default=None)
# 9. Top payer
def top_payer():
    p=paid_by_person(); return max(p,key=p.get) if p else None
# 10. Report
def report():
    show_expenses(); print(f'Total: Rs {total_expense():.2f}'); print(f'Equal share: Rs {equal_share():.2f}'); print('Paid:',paid_by_person()); print('Balances:',balances()); print('Top payer:',top_payer())
if __name__=='__main__': report()
