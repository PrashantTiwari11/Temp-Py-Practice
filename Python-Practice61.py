# 56 - Contact Manager Project: 10 practical features

class ContactManager:
    def __init__(self):
        self.contacts = {}

    # 1. Add contact
    def add(self, name, phone, email=""):
        self.contacts[name.lower()] = {"name":name, "phone":phone, "email":email}

    # 2. Find contact
    def find(self, name): return self.contacts.get(name.lower())

    # 3. Update phone
    def update_phone(self, name, phone):
        c = self.find(name)
        if not c: return False
        c["phone"] = phone
        return True

    # 4. Update email
    def update_email(self, name, email):
        c = self.find(name)
        if not c: return False
        c["email"] = email
        return True

    # 5. Delete contact
    def delete(self, name): return self.contacts.pop(name.lower(), None) is not None

    # 6. Search by keyword
    def search(self, keyword):
        return [c for c in self.contacts.values() if keyword.lower() in c["name"].lower()]

    # 7. List alphabetically
    def all_contacts(self):
        return sorted(self.contacts.values(), key=lambda c:c["name"].lower())

    # 8. Count contacts
    def count(self): return len(self.contacts)

    # 9. Export CSV text
    def export_csv(self):
        lines = ["Name,Phone,Email"]
        for c in self.all_contacts():
            lines.append(f'{c["name"]},{c["phone"]},{c["email"]}')
        return "\n".join(lines)

    # 10. Import CSV text
    def import_csv(self, text):
        for line in text.strip().splitlines()[1:]:
            name, phone, email = line.split(",", 2)
            self.add(name, phone, email)

if __name__ == "__main__":
    cm = ContactManager()
    cm.add("Aman", "9876543210", "aman@mail.com")
    cm.add("Riya", "9123456780", "riya@mail.com")
    cm.add("Rahul", "9988776655", "rahul@mail.com")

    print("1. All:", cm.all_contacts())
    print("2. Find Riya:", cm.find("Riya"))
    print("3. Update phone:", cm.update_phone("Riya","9000000000"))
    print("4. Updated Riya:", cm.find("Riya"))
    print("5. Update email:", cm.update_email("Aman","newaman@mail.com"))
    print("6. Search 'ra':", cm.search("ra"))
    print("7. Count:", cm.count())
    print("8. Delete Rahul:", cm.delete("Rahul"))
    print("9. CSV:\n", cm.export_csv())
    cm.import_csv("Name,Phone,Email\nNeha,9111111111,neha@mail.com")
    print("10. Final count:", cm.count())
