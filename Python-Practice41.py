# Day 9 - 35: HTML Parsing Basics
from html.parser import HTMLParser
from urllib.parse import urlparse, urljoin

# 1. Parse a URL
def parse_url(url):
    p = urlparse(url)
    return p.scheme, p.netloc, p.path

# 2. Make an absolute URL
def absolute_url(base, link):
    return urljoin(base, link)

class LinkParser(HTMLParser):
    # 3. Extract links
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for key, value in attrs:
                if key == "href":
                    self.links.append(value)

class TextParser(HTMLParser):
    # 4. Extract text
    def __init__(self):
        super().__init__()
        self.parts = []
    def handle_data(self, data):
        if data.strip():
            self.parts.append(data.strip())

class TagCounter(HTMLParser):
    # 5. Count tags
    def __init__(self):
        super().__init__()
        self.counts = {}
    def handle_starttag(self, tag, attrs):
        self.counts[tag] = self.counts.get(tag, 0) + 1

class HeadingParser(HTMLParser):
    # 6. Extract headings
    def __init__(self):
        super().__init__()
        self.headings = []
        self.current = None
    def handle_starttag(self, tag, attrs):
        if tag in ("h1","h2","h3"):
            self.current = tag
    def handle_data(self, data):
        if self.current and data.strip():
            self.headings.append((self.current, data.strip()))
    def handle_endtag(self, tag):
        if tag == self.current:
            self.current = None

# 7. Clean HTML text
def clean_text(html):
    parser = TextParser()
    parser.feed(html)
    return " ".join(parser.parts)

# 8. Get links
def links(html):
    parser = LinkParser()
    parser.feed(html)
    return parser.links

# 9. Count tags
def tag_counts(html):
    parser = TagCounter()
    parser.feed(html)
    return parser.counts

# 10. Analyze a page
def analyze(html):
    parser = HeadingParser()
    parser.feed(html)
    return {"text": clean_text(html), "links": links(html),
            "tags": tag_counts(html), "headings": parser.headings}

if __name__ == "__main__":
    html = '<h1>Python</h1><p>Learn Python.</p><a href="/lesson">Lesson</a>'
    print(parse_url("https://example.com/python"))
    print(absolute_url("https://example.com/python/", "lesson"))
    print(links(html))
    print(clean_text(html))
    print(tag_counts(html))
    print(analyze(html))
