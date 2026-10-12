"""159 Movie Watchlist: 10 features."""
movies=[]
def add(title,genre,year=None,watched=False,rating=None): movies.append({"title":title,"genre":genre,"year":year,"watched":watched,"rating":rating})
def all_movies(): return movies.copy()
def unwatched(): return [m for m in movies if not m["watched"]]
def watched(): return [m for m in movies if m["watched"]]
def by_genre(g): return [m for m in movies if m["genre"].lower()==g.lower()]
def search(q): return [m for m in movies if q.lower() in m["title"].lower()]
def mark_watched(title,rating=None):
    for m in movies:
        if m["title"].lower()==title.lower():
            m["watched"]=True
            if rating is not None: m["rating"]=rating
            return True
    return False
def average_rating():
    rs=[m["rating"] for m in movies if isinstance(m["rating"],(int,float))]
    return round(sum(rs)/len(rs),2) if rs else None
def remove(title):
    for i,m in enumerate(movies):
        if m["title"].lower()==title.lower(): return movies.pop(i)
    return None
def export_csv(path="movie_watchlist.csv"):
    import csv
    with open(path,"w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=["title","genre","year","watched","rating"]); w.writeheader(); w.writerows(movies)
if __name__=="__main__":
    add("Interstellar","Sci-Fi",2014); add("3 Idiots","Comedy",2009,True,4.8); add("The Martian","Sci-Fi",2015)
    print("1 All:",all_movies()); print("2 Unwatched:",unwatched()); print("3 Watched:",watched())
    print("4 Sci-Fi:",by_genre("Sci-Fi")); print("5 Search:",search("martian"))
    print("6 Mark watched:",mark_watched("Interstellar",4.9)); print("7 Average rating:",average_rating())
    print("8 Remove with remove(title)"); print("9 Export CSV with export_csv()")
    print("10 Add with add(title, genre, year, watched, rating)")
