# Simple List Duplicate Remover
items = input("Enter items separated by commas: ").split(",")
items = [item.strip() for item in items]
unique_items = []
for item in items:
    if item not in unique_items:
        unique_items.append(item)
print("Original list:", items)
print("List without duplicates:", unique_items)
