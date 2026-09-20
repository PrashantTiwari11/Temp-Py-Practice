# 80_python_mini_inventory_system.py
# Mini Inventory Management System - 10 practical features
class Inventory:
    def __init__(self): self.products={}
    def add_product(self,name,price,quantity): self.products[name]={'price':price,'quantity':quantity}
    def remove_product(self,name): return self.products.pop(name,None) is not None
    def update_quantity(self,name,quantity):
        if name in self.products: self.products[name]['quantity']=quantity; return True
        return False
    def sell(self,name,quantity):
        if name not in self.products: return False,'Product not found'
        if self.products[name]['quantity']<quantity: return False,'Insufficient stock'
        self.products[name]['quantity']-=quantity
        return True,self.products[name]['price']*quantity
    def search(self,keyword): return [n for n in self.products if keyword.lower() in n.lower()]
    def low_stock(self,limit=5): return [n for n,d in self.products.items() if d['quantity']<=limit]
    def total_value(self): return sum(d['price']*d['quantity'] for d in self.products.values())
    def count(self): return len(self.products)
    def display(self):
        for name,data in self.products.items(): print(name,'=>',data)
    def most_valuable(self):
        if not self.products: return None
        return max(self.products.items(),key=lambda item:item[1]['price']*item[1]['quantity'])

inventory=Inventory()
inventory.add_product('Laptop',55000,4); inventory.add_product('Mouse',800,20); inventory.add_product('Keyboard',1500,8); inventory.add_product('Monitor',12000,3)
print('1. Inventory:'); inventory.display()
print('2. Product count:',inventory.count())
print("3. Search 'lap':",inventory.search('lap'))
print('4. Low stock:',inventory.low_stock())
success,result=inventory.sell('Mouse',3); print('5. Sale:',success,result)
print('6. Mouse stock:',inventory.products['Mouse']['quantity'])
print('7. Inventory value:',inventory.total_value())
inventory.update_quantity('Monitor',10); print('8. Updated monitor:',inventory.products['Monitor'])
print('9. Most valuable:',inventory.most_valuable())
print('10. Remove keyboard:',inventory.remove_product('Keyboard'))
