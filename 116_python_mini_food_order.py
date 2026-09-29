# 116_python_mini_food_order.py
# Mini Food Ordering System - 10 practical features

menu = {
    "Burger": 120,
    "Pizza": 250,
    "Sandwich": 100,
    "Pasta": 180,
    "Coffee": 80,
}

cart = {
    "Burger": 2,
    "Coffee": 1,
    "Pasta": 1,
}

# 1. Display menu
print("1. Menu:", menu)

# 2. Count menu items
print("2. Menu item count:", len(menu))

# 3. Search menu item
keyword = "pizza"
print("3. Search:", [item for item in menu if keyword.lower() in item.lower()])

# 4. Find items under a budget
budget = 150
print("4. Items <= 150:", [item for item, price in menu.items() if price <= budget])

# 5. Display cart
print("5. Cart:", cart)

# 6. Calculate item totals
item_totals = {item: menu[item] * quantity for item, quantity in cart.items()}
print("6. Item totals:", item_totals)

# 7. Calculate subtotal
subtotal = sum(item_totals.values())
print("7. Subtotal:", subtotal)

# 8. Apply discount
discount_rate = 10
discount = subtotal * discount_rate / 100
after_discount = subtotal - discount
print("8. Discounted total:", round(after_discount, 2))

# 9. Add delivery charge and tax
delivery = 40
tax = after_discount * 5 / 100
grand_total = after_discount + delivery + tax
print("9. Grand total:", round(grand_total, 2))

# 10. Generate order summary
print("10. Order summary:")
print("Items:", sum(cart.values()))
print("Subtotal:", subtotal)
print("Discount:", round(discount, 2))
print("Tax:", round(tax, 2))
print("Delivery:", delivery)
print("Grand Total:", round(grand_total, 2))
