# 140 - Smart Grocery List: 10 practical features
grocery_items = [
    {"name": "Rice", "quantity": 2, "unit": "kg", "price": 70.0, "bought": False},
    {"name": "Milk", "quantity": 2, "unit": "litre", "price": 32.0, "bought": True},
    {"name": "Apples", "quantity": 1, "unit": "kg", "price": 140.0, "bought": False},
    {"name": "Bread", "quantity": 1, "unit": "pack", "price": 45.0, "bought": True},
]
# 1. Display items
def show_items():
    for i in grocery_items:
        print(f"{i['name']}: {i['quantity']} {i['unit']} @ Rs {i['price']:.2f} - {'Bought' if i['bought'] else 'Needed'}")
# 2. Count items
def item_count(): return len(grocery_items)
# 3. Search items
def search_item(query): return [i for i in grocery_items if query.lower() in i["name"].lower()]
# 4. Add item
def add_item(name, quantity, unit, price):
    if quantity <= 0 or price < 0: raise ValueError("Quantity must be positive and price non-negative.")
    grocery_items.append({"name": name, "quantity": quantity, "unit": unit, "price": float(price), "bought": False})
# 5. Mark item bought
def mark_bought(name):
    for i in grocery_items:
        if i["name"].lower() == name.lower():
            i["bought"] = True
            return True
    return False
# 6. List needed items
def needed_items(): return [i for i in grocery_items if not i["bought"]]
# 7. Estimate cost
def estimated_total(only_needed=False):
    items = needed_items() if only_needed else grocery_items
    return round(sum(i["quantity"] * i["price"] for i in items), 2)
# 8. Find highest unit-price item
def most_expensive_item(): return max(grocery_items, key=lambda i: i["price"], default=None)
# 9. Sort by unit price
def sort_by_price(): return sorted(grocery_items, key=lambda i: i["price"])
# 10. Print summary
def report():
    print("GROCERY LIST")
    show_items()
    print("Items:", item_count(), "| Needed:", len(needed_items()))
    print(f"Full-list estimate: Rs {estimated_total():.2f}")
    print(f"Needed-items estimate: Rs {estimated_total(True):.2f}")
if __name__ == "__main__": report()
