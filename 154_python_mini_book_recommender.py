"""154 Book Recommender — 10 features."""
books=[]
def add_book(title,author,genre,rating=0): books.append({"title":title,"author":author,"genre":genre,"rating":float(rating)})
def search_title(q): return [b for b in books if q.lower() in b["title"].lower()]
def by_author(a): return [b for b in books if b["author"].lower()==a.lower()]
def by_genre(g): return [b for b in books if b["genre"].lower()==g.lower()]
def top_rated(limit=5): return sorted(books,key=lambda b:b["rating"],reverse=True)[:limit]
def recommend(genre=None,min_rating=0):
    found=[b for b in books if b["rating"]>=min_rating and (genre is None or b["genre"].lower()==genre.lower())]
    return sorted(found,key=lambda b:b["rating"],reverse=True)
def average_rating(): return round(sum(b["rating"] for b in books)/len(books),2) if books else 0
def update_rating(title,rating):
    for b in books:
        if b["title"].lower()==title.lower(): b["rating"]=float(rating); return True
    return False
def remove_book(title):
    for i,b in enumerate(books):
        if b["title"].lower()==title.lower(): return books.pop(i)
    return None
def export_csv(path="books.csv"):
    import csv
    with open(path,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["title","author","genre","rating"]); w.writeheader(); w.writerows(books)
if __name__=="__main__":
    add_book("Atomic Habits","James Clear","Self-help",4.8); add_book("The Hobbit","J.R.R. Tolkien","Fantasy",4.7); add_book("Deep Work","Cal Newport","Productivity",4.5)
    print("1 Search title:",search_title("atomic")); print("2 Author:",by_author("James Clear"))
    print("3 Genre:",by_genre("Fantasy")); print("4 Top rated:",top_rated())
    print("5 Recommend:",recommend(min_rating=4.6)); print("6 Genre recommend:",recommend("Fantasy"))
    print("7 Average rating:",average_rating()); print("8 Update rating:",update_rating("Deep Work",4.6))
    print("9 Remove with remove_book(title)"); print("10 Export CSV with export_csv()")
