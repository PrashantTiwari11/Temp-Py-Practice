# 144 - Mini Inventory Alert System: 10 practical features
inventory=[{'name':'Keyboard','stock':12,'reorder_level':5,'price':850},{'name':'Mouse','stock':4,'reorder_level':6,'price':500},{'name':'Monitor','stock':3,'reorder_level':4,'price':9000},{'name':'USB Cable','stock':25,'reorder_level':10,'price':250}]
# 1. Display inventory
def show_inventory():
    for i in inventory: print(f"{i['name']} | Stock:{i['stock']} | Reorder:{i['reorder_level']} | Rs {i['price']}")
# 2. Product count
def product_count(): return len(inventory)
# 3. Low-stock products
def low_stock_items(): return [i for i in inventory if i['stock']<=i['reorder_level']]
# 4. Search products
def search_product(query): return [i for i in inventory if query.lower() in i['name'].lower()]
# 5. Add stock
def add_stock(name,quantity):
    for i in inventory:
        if i['name'].lower()==name.lower(): i['stock']+=quantity; return True
    return False
# 6. Remove stock
def remove_stock(name,quantity):
    for i in inventory:
        if i['name'].lower()==name.lower() and i['stock']>=quantity: i['stock']-=quantity; return True
    return False
# 7. Add product
def add_product(name,stock,reorder_level,price): inventory.append({'name':name,'stock':stock,'reorder_level':reorder_level,'price':price})
# 8. Inventory value
def inventory_value(): return sum(i['stock']*i['price'] for i in inventory)
# 9. Highest-value product
def highest_value_product(): return max(inventory,key=lambda i:i['stock']*i['price'],default=None)
# 10. Alert report
def report():
    show_inventory(); low=low_stock_items(); print('Products:',product_count()); print('Low-stock alerts:',[i['name'] for i in low]); print(f'Total inventory value: Rs {inventory_value():.2f}')
if __name__=='__main__': report()
