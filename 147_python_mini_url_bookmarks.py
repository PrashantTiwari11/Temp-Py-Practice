# 147 - Mini URL Bookmark Manager: 10 practical features
from urllib.parse import urlparse
bookmarks = [
 {"title":"Python Docs","url":"https://docs.python.org/3/","category":"Learning"},
 {"title":"GitHub","url":"https://github.com/","category":"Development"},
 {"title":"MDN Web Docs","url":"https://developer.mozilla.org/","category":"Learning"}]
# 1. Validate URL
def is_valid_url(url):
    parsed = urlparse(url)
    return parsed.scheme in {"http","https"} and bool(parsed.netloc)
# 2. List bookmarks
def list_bookmarks(): return list(bookmarks)
# 3. Search titles
def search_title(query): return [b for b in bookmarks if query.lower() in b["title"].lower()]
# 4. Filter category
def by_category(category): return [b for b in bookmarks if b["category"].lower() == category.lower()]
# 5. Add bookmark
def add_bookmark(title, url, category="General"):
    if not is_valid_url(url): raise ValueError("Enter a valid http or https URL.")
    bookmarks.append({"title":title,"url":url,"category":category})
# 6. Remove bookmark
def remove_bookmark(title):
    for b in bookmarks:
        if b["title"].lower() == title.lower(): bookmarks.remove(b); return True
    return False
# 7. List categories
def categories(): return sorted({b["category"] for b in bookmarks})
# 8. Count bookmarks
def bookmark_count(): return len(bookmarks)
# 9. Search by domain
def by_domain(domain): return [b for b in bookmarks if urlparse(b["url"]).netloc.lower().endswith(domain.lower())]
# 10. Export bookmarks to CSV
def export_csv(filename="bookmarks.csv"):
    import csv
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title","url","category"])
        writer.writeheader()
        writer.writerows(bookmarks)
    return filename
if __name__ == "__main__":
    for b in list_bookmarks(): print(f"{b['title']} [{b['category']}] - {b['url']}")
    print("Categories:", categories(), "| Count:", bookmark_count())
