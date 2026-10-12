"""160 Smart Grocery List: 10 features."""
items={}
def add(name,quantity=1,category="Other",price=0.0):
    if quantity<=0 or price<0: raise ValueError("Quantity must be positive and price non-negative")
    key=name.strip().lower()
    if key in items: items[key]["quantity"]+=quantity
    else: items[key]={"name":name.strip(),"quantity":quantity,"category":category,"price":float(price)}
def all_items(): return list(items.values())
def mark_purchased(name):
    key=name.strip().lower()
    if key not in items: return False
    items[key]["purchased"]=True; return True
def to_buy(): return [i for i in items.values() if not i.get("purchased",False)]
def by_category(category): return [i for i in items.values() if i["category"].lower()==category.lower()]
def remove(name): return items.pop(name.strip().lower(),None)
def estimated_total(): return round(sum(i["quantity"]*i["price"] for i in items.values()),2)
def update_quantity(name,quantity):
    if quantity<=0: raise ValueError("Quantity must be positive")
    items[name.strip().lower()]["quantity"]=quantity
def summary(): return {"unique_items":len(items),"units":sum(i["quantity"] for i in items.values()),"cost":estimated_total(),"to_buy":len(to_buy())}
def export_csv(path="grocery_list.csv"):
    import csv
    with open(path,"w",newline="",encoding="utf-8") as f:
        fields=["name","quantity","category","price","purchased"]; w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
        for i in items.values(): w.writerow({**i,"purchased":i.get("purchased",False)})
if __name__=="__main__":
    add("Milk",2,"Dairy",30); add("Rice",1,"Grains",70); add("Milk",1,"Dairy",30)
    print("1 All:",all_items()); print("2 Mark rice purchased:",mark_purchased("Rice"))
    print("3 To buy:",to_buy()); print("4 Dairy:",by_category("Dairy")); print("5 Estimated total:",estimated_total())
    update_quantity("rice",2); print("6 Updated rice:",items["rice"]); print("7 Summary:",summary())
    print("8 Remove with remove(name)"); print("9 Export CSV with export_csv()")
    print("10 Add with add(name, quantity, category, price)")
