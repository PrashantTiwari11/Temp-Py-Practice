# 117_python_mini_library_manager.py
# Mini Library Manager - 10 practical features
books=[{"title":"Python Basics","author":"John","available":True},{"title":"Data Structures","author":"Alice","available":False},{"title":"IoT Fundamentals","author":"David","available":True},{"title":"Cloud Computing","author":"Sara","available":True}]
print("1. Books:",books)
print("2. Total books:",len(books))
keyword="python"; print("3. Title search:",[b for b in books if keyword.lower() in b["title"].lower()])
author="alice"; print("4. Author search:",[b for b in books if b["author"].lower()==author])
print("5. Available:",[b["title"] for b in books if b["available"]])
print("6. Borrowed:",[b["title"] for b in books if not b["available"]])
books[0]["available"]=False; print("7. Borrowed:",books[0]["title"])
books[1]["available"]=True; print("8. Returned:",books[1]["title"])
books.append({"title":"Machine Learning","author":"Robert","available":True}); print("9. Added:",books[-1])
available=sum(b["available"] for b in books); print("10. Summary:",{"total":len(books),"available":available,"borrowed":len(books)-available})
