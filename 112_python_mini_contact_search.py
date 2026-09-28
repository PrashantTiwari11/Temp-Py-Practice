# 112_python_mini_contact_search.py
# Contact Search and Filtering - 10 practical features

contacts = [
    {"name": "Prashant", "phone": "9876543210", "city": "Rajkot"},
    {"name": "Aman", "phone": "9988776655", "city": "Ahmedabad"},
    {"name": "Riya", "phone": "9123456780", "city": "Rajkot"},
    {"name": "Neha", "phone": "9012345678", "city": "Delhi"},
]

# 1. Display contacts
print("1. Contacts:", contacts)

# 2. Count contacts
print("2. Contact count:", len(contacts))

# 3. Search by name
name = "riya"
print("3. Name search:", [c for c in contacts if name.lower() in c["name"].lower()])

# 4. Search by city
city = "Rajkot"
print("4. City search:", [c for c in contacts if c["city"].lower() == city.lower()])

# 5. Search by phone
phone = "9876543210"
print("5. Phone search:", next((c for c in contacts if c["phone"] == phone), None))

# 6. Sort by name
print("6. Sorted names:", [c["name"] for c in sorted(contacts, key=lambda x: x["name"])])

# 7. Group by city
grouped = {}
for c in contacts:
    grouped.setdefault(c["city"], []).append(c["name"])
print("7. Grouped by city:", grouped)

# 8. Validate phone numbers
valid = [c["name"] for c in contacts if c["phone"].isdigit() and len(c["phone"]) == 10]
print("8. Valid phones:", valid)

# 9. Add contact
contacts.append({"name": "Karan", "phone": "9090909090", "city": "Mumbai"})
print("9. Added contact:", contacts[-1])

# 10. Summary
print("10. Summary:", {
    "total": len(contacts),
    "cities": sorted({c["city"] for c in contacts}),
    "valid_phones": sum(c["phone"].isdigit() and len(c["phone"]) == 10 for c in contacts)
})
