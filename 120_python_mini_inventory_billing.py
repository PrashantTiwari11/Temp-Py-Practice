# 120_python_mini_inventory_billing.py
# Mini Inventory and Billing System - 10 practical features
inventory={"Keyboard":{"price":800,"stock":10},"Mouse":{"price":500,"stock":15},"Monitor":{"price":7000,"stock":5},"USB Cable":{"price":250,"stock":20}}
cart={"Keyboard":2,"Mouse":1,"USB Cable":3}
print("1. Inventory:",inventory)
print("2. Product count:",len(inventory))
print("3. Low stock:",[n for n,x in inventory.items() if x["stock"]<10])
keyword="mouse"; print("4. Search:",[n for n in inventory if keyword.lower() in n.lower()])
item_totals={n:inventory[n]["price"]*q for n,q in cart.items()}; print("5. Item totals:",item_totals)
subtotal=sum(item_totals.values()); print("6. Subtotal:",subtotal)
discount=subtotal*5/100; after_discount=subtotal-discount; print("7. After discount:",round(after_discount,2))
tax=after_discount*18/100; grand_total=after_discount+tax; print("8. Grand total:",round(grand_total,2))
for n,q in cart.items(): inventory[n]["stock"]-=q
print("9. Updated stock:",{n:x["stock"] for n,x in inventory.items()})
print("10. BILL:",{"subtotal":subtotal,"discount":round(discount,2),"tax":round(tax,2),"grand_total":round(grand_total,2)})
