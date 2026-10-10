"""152 Inventory Alert System: 10 practical features."""
inventory = {}
def add_item(name, quantity, reorder_level, price=0.0):
    if min(quantity, reorder_level, price) < 0: raise ValueError("Values must be non-negative")
    inventory[name] = {"quantity": quantity, "reorder_level": reorder_level, "price": price}
def restock(name, quantity):
    if quantity <= 0: raise ValueError("Restock quantity must be positive")
    inventory[name]["quantity"] += quantity
def sell(name, quantity):
    if quantity <= 0: raise ValueError("Sale quantity must be positive")
    if name not in inventory: raise KeyError("Item not found")
    if inventory[name]["quantity"] < quantity: raise ValueError("Not enough stock")
    inventory[name]["quantity"] -= quantity
def low_stock(): return {n: d for n, d in inventory.items() if d["quantity"] <= d["reorder_level"]}
def stock_value(): return round(sum(d["quantity"]*d["price"] for d in inventory.values()), 2)
def search(query): return {n: d for n, d in inventory.items() if query.lower() in n.lower()}
def update_price(name, price):
    if price < 0: raise ValueError("Price cannot be negative")
    inventory[name]["price"] = price
def remove_item(name): return inventory.pop(name, None)
def report():
    for name, d in inventory.items(): print(f"{name}: qty={d['quantity']}, reorder={d['reorder_level']}, price={d['price']:.2f}")
def export_csv(path="inventory_report.csv"):
    import csv
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(["item", "quantity", "reorder_level", "price"])
        for n, d in inventory.items(): w.writerow([n, d["quantity"], d["reorder_level"], d["price"]])
if __name__ == "__main__":
    add_item("Notebook", 8, 5, 45); add_item("Pen", 3, 10, 10); add_item("USB Drive", 12, 4, 350)
    print("1 Inventory:"); report()
    print("2 Low-stock alerts:", low_stock())
    print("3 Total stock value:", stock_value())
    print("4 Search pen:", search("pen"))
    restock("Pen", 15); print("5 After restock:", inventory["Pen"])
    sell("Notebook", 2); print("6 After sale:", inventory["Notebook"])
    update_price("Notebook", 50); print("7 Updated price:", inventory["Notebook"])
    print("8 Remove item with remove_item(name)")
    print("9 Export CSV with export_csv()")
    print("10 Add items with add_item(name, quantity, reorder_level, price)")
