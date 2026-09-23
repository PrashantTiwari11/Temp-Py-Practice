# 96_python_mini_contact_manager.py
# Mini Contact Manager - 10 practical features

class ContactManager:
    def __init__(self):
        self.contacts = {}

    # 1. Add contact
    def add(self, name, phone, email=""):
        self.contacts[name.lower()] = {
            "name": name,
            "phone": phone,
            "email": email
        }

    # 2. Find contact
    def find(self, name):
        return self.contacts.get(name.lower())

    # 3. Update phone
    def update_phone(self, name, phone):
        contact = self.find(name)
        if contact:
            contact["phone"] = phone
            return True
        return False

    # 4. Delete contact
    def delete(self, name):
        return self.contacts.pop(name.lower(), None)

    # 5. Search contacts
    def search(self, keyword):
        return [
            c for c in self.contacts.values()
            if keyword.lower() in c["name"].lower()
        ]

    # 6. Count contacts
    def count(self):
        return len(self.contacts)

    # 7. Sort contacts
    def sorted_contacts(self):
        return sorted(self.contacts.values(), key=lambda c: c["name"].lower())

    # 8. Validate phone
    def valid_phone(self, phone):
        digits = ''.join(c for c in phone if c.isdigit())
        return len(digits) >= 10

    # 9. Display contacts
    def display(self):
        for contact in self.sorted_contacts():
            print(contact)

    # 10. Export as simple text
    def export_text(self):
        return "\n".join(
            f'{c["name"]}: {c["phone"]} | {c["email"]}'
            for c in self.sorted_contacts()
        )


manager = ContactManager()
manager.add("Prashant", "9876543210", "prashant@example.com")
manager.add("Riya", "9123456780", "riya@example.com")
manager.add("Aman", "9988776655", "aman@example.com")
manager.add("Neha", "9012345678", "neha@example.com")

print("1. Contacts:")
manager.display()

print("2. Find:", manager.find("Prashant"))
manager.update_phone("Aman", "9999999999")
print("3. Updated Aman:", manager.find("Aman"))

print("4. Search 'ri':", manager.search("ri"))
print("5. Count:", manager.count())

print("6. Valid phone:", manager.valid_phone("9876543210"))
print("7. Invalid phone:", manager.valid_phone("12345"))

print("8. Sorted:", manager.sorted_contacts())

removed = manager.delete("Neha")
print("9. Deleted:", removed)

print("10. Text export:\n" + manager.export_text())
