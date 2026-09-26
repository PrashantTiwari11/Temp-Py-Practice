# 103_python_inventory_tracker.py
# Inventory Tracker - 10 practical features

inventory = {
    "Laptop": {"price": 55000, "stock": 5},
    "Mouse": {"price": 700, "stock": 20},
    "Keyboard": {"price": 1500, "stock": 10},
    "Monitor": {"price": 12000, "stock": 4},
}

print("1. Products:", list(inventory))
print("2. Product count:", len(inventory))
print("3. Total stock units:", sum(x["stock"] for x in inventory.values()))
print("4. Inventory value:", sum(x["price"] * x["stock"] for x in inventory.values()))

inventory["Webcam"] = {"price": 2500, "stock": 8}
print("5. Added Webcam:", inventory["Webcam"])

inventory["Mouse"]["stock"] += 5
print("6. Updated Mouse stock:", inventory["Mouse"]["stock"])

print("7. Low stock:", [n for n, x in inventory.items() if x["stock"] < 5])
expensive = max(inventory, key=lambda n: inventory[n]["price"])
print("8. Most expensive:", expensive)

search = "key"
print("9. Search result:", [n for n in inventory if search in n.lower()])

summary = {
    "products": len(inventory),
    "units": sum(x["stock"] for x in inventory.values()),
    "value": sum(x["price"] * x["stock"] for x in inventory.values())
}
print("10. Summary:", summary)
