# 134 - Mini Book Recommender: 10 practical features
books = [
    {"title": "Atomic Habits", "author": "James Clear", "genre": "Self-help", "rating": 4.7, "pages": 320},
    {"title": "The Hobbit", "author": "J. R. R. Tolkien", "genre": "Fantasy", "rating": 4.8, "pages": 310},
    {"title": "Deep Work", "author": "Cal Newport", "genre": "Productivity", "rating": 4.5, "pages": 304},
    {"title": "Dune", "author": "Frank Herbert", "genre": "Science fiction", "rating": 4.6, "pages": 688},
    {"title": "Ikigai", "author": "Hector Garcia", "genre": "Self-help", "rating": 4.2, "pages": 208},
]

# 1. List all books
def list_books():
    return [f"{b['title']} — {b['author']}" for b in books]

# 2. Search titles
def search_title(query):
    return [b for b in books if query.lower() in b["title"].lower()]

# 3. Filter by genre
def by_genre(genre):
    return [b for b in books if b["genre"].lower() == genre.lower()]

# 4. Recommend top-rated books
def top_rated(minimum=4.5):
    return sorted([b for b in books if b["rating"] >= minimum], key=lambda b: b["rating"], reverse=True)

# 5. Find short reads
def short_reads(max_pages=300):
    return [b for b in books if b["pages"] <= max_pages]

# 6. Search by author
def by_author(author):
    return [b for b in books if author.lower() in b["author"].lower()]

# 7. Sort by page count
def sort_by_pages():
    return sorted(books, key=lambda b: b["pages"])

# 8. Add a book
def add_book(title, author, genre, rating, pages):
    if not 0 <= rating <= 5 or pages <= 0:
        raise ValueError("Rating must be 0–5 and pages must be positive.")
    books.append({"title": title, "author": author, "genre": genre, "rating": rating, "pages": pages})

# 9. Average rating
def average_rating():
    return round(sum(b["rating"] for b in books) / len(books), 2) if books else 0

# 10. Print recommendations
def report():
    print("BOOK RECOMMENDATIONS")
    for b in top_rated():
        print(f"{b['title']} — {b['rating']}/5 ({b['genre']})")
    print("Average rating:", average_rating())

if __name__ == "__main__":
    print("\n".join(list_books()))
    report()
