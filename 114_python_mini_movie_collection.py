# 114_python_mini_movie_collection.py
# Mini Movie Collection - 10 practical features

movies = [
    {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8, "year": 2010},
    {"title": "3 Idiots", "genre": "Drama", "rating": 8.4, "year": 2009},
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.7, "year": 2014},
    {"title": "Dangal", "genre": "Sports", "rating": 8.3, "year": 2016},
]

# 1. Display movies
print("1. Movies:", movies)

# 2. Count movies
print("2. Movie count:", len(movies))

# 3. Search by title
keyword = "inter"
print("3. Title search:", [m for m in movies if keyword.lower() in m["title"].lower()])

# 4. Filter by genre
genre = "Sci-Fi"
print("4. Sci-Fi movies:", [m["title"] for m in movies if m["genre"] == genre])

# 5. Movies above rating 8.5
print("5. Rating above 8.5:", [m["title"] for m in movies if m["rating"] > 8.5])

# 6. Sort by rating
sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
print("6. Sorted by rating:", [(m["title"], m["rating"]) for m in sorted_movies])

# 7. Highest-rated movie
best = max(movies, key=lambda m: m["rating"])
print("7. Highest rated:", best["title"])

# 8. Newest movie
newest = max(movies, key=lambda m: m["year"])
print("8. Newest movie:", newest["title"])

# 9. Add a movie
movies.append({"title": "Taare Zameen Par", "genre": "Drama", "rating": 8.3, "year": 2007})
print("9. Added movie:", movies[-1])

# 10. Collection summary
genres = sorted({m["genre"] for m in movies})
average_rating = sum(m["rating"] for m in movies) / len(movies)
print("10. Summary:", {
    "total_movies": len(movies),
    "genres": genres,
    "average_rating": round(average_rating, 2)
})
