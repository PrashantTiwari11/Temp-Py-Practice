# 139 - Movie Watchlist: 10 practical features
movies = [
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.7, "watched": True},
    {"title": "The Martian", "genre": "Sci-Fi", "rating": 8.0, "watched": False},
    {"title": "3 Idiots", "genre": "Comedy", "rating": 8.4, "watched": True},
    {"title": "Dangal", "genre": "Drama", "rating": 8.3, "watched": False},
]
# 1. Display watchlist
def show_movies():
    for m in movies: print(f"{m['title']} | {m['genre']} | {m['rating']}/10 | {'Watched' if m['watched'] else 'To watch'}")
# 2. Count movies
def movie_count(): return len(movies)
# 3. Search titles
def search_title(query): return [m for m in movies if query.lower() in m["title"].lower()]
# 4. Filter by genre
def filter_genre(genre): return [m for m in movies if m["genre"].lower() == genre.lower()]
# 5. List unwatched movies
def unwatched_movies(): return [m for m in movies if not m["watched"]]
# 6. List watched movies
def watched_movies(): return [m for m in movies if m["watched"]]
# 7. Sort by rating
def top_movies(): return sorted(movies, key=lambda m: m["rating"], reverse=True)
# 8. Add a movie
def add_movie(title, genre, rating=0, watched=False):
    if not 0 <= rating <= 10: raise ValueError("Rating must be from 0 to 10.")
    movies.append({"title": title, "genre": genre, "rating": float(rating), "watched": bool(watched)})
# 9. Mark a movie watched
def mark_watched(title):
    for m in movies:
        if m["title"].lower() == title.lower():
            m["watched"] = True
            return True
    return False
# 10. Print statistics
def report():
    print("MOVIE WATCHLIST")
    show_movies()
    print("Total:", movie_count(), "| Watched:", len(watched_movies()), "| To watch:", len(unwatched_movies()))
    print("Top rated:", top_movies()[0]["title"] if movies else "No movies")
if __name__ == "__main__": report()
