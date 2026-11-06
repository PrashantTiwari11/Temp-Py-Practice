import json
from pathlib import Path

DATA_FILE = Path("library_books.json")

def load_books():
    if not DATA_FILE.exists():
        return []
    try:
        data = json.loads(DATA_FILE.read_text(encoding="utf-8"))
        return data if isinstance(data, list) else []
    except (json.JSONDecodeError, OSError):
        print("Could not read saved book data.")
        return []

def save_books(books):
    DATA_FILE.write_text(json.dumps(books, indent=2), encoding="utf-8")

def main():
    books = load_books()
    while True:
        print("\\n1. Add book  2. List books  3. Search  4. Delete  5. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            title = input("Book title: ").strip()
            author = input("Author: ").strip()
            if title and author:
                books.append({"title": title, "author": author})
                save_books(books)
                print("Book added.")
            else:
                print("Title and author are required.")
        elif choice == "2":
            if not books:
                print("No books in library.")
            for i, book in enumerate(books, 1):
                print(f"{i}. {book['title']} — {book['author']}")
        elif choice == "3":
            term = input("Search title or author: ").strip().lower()
            found = [b for b in books if term in b["title"].lower()
                     or term in b["author"].lower()]
            for book in found:
                print(f"{book['title']} — {book['author']}")
            if not found:
                print("No matching books.")
        elif choice == "4":
            try:
                number = int(input("Book number to delete: "))
                if 1 <= number <= len(books):
                    removed = books.pop(number - 1)
                    save_books(books)
                    print("Deleted:", removed["title"])
                else:
                    print("Invalid book number.")
            except ValueError:
                print("Enter a valid whole number.")
        elif choice == "5":
            print("Library manager closed.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
