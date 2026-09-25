# 97_python_url_utilities.py
# URL Utilities - 10 practical features
from urllib.parse import urlparse, urljoin, urlencode, parse_qs, quote, unquote

url = "https://example.com/products/item?id=101&name=python"
parsed = urlparse(url)

print("1. Parsed URL:", parsed)
print("2. Scheme:", parsed.scheme)
print("3. Domain:", parsed.netloc)
print("4. Path:", parsed.path)
print("5. Query:", parsed.query)
print("6. Parameters:", parse_qs(parsed.query))
print("7. New query:", urlencode({"page": 2, "limit": 10}))
print("8. Joined URL:", urljoin("https://example.com/docs/", "python.html"))

encoded = quote("Python programming & projects")
print("9. Encoded:", encoded)
print("10. Decoded:", unquote(encoded))
