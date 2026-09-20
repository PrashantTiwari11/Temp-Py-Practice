# 77_python_web_scraping_basics.py
# Web Scraping Basics - 10 practical programs/features
from html.parser import HTMLParser
from urllib.parse import urlparse, urljoin

html='''<html><head><title>Python Demo</title></head><body><h1>Learning Python</h1><a href="/courses">Courses</a><a href="https://example.com/about">About</a><p>Python is useful for automation.</p></body></html>'''

class TextParser(HTMLParser):
    def __init__(self): super().__init__(); self.text=[]
    def handle_data(self,data):
        if data.strip(): self.text.append(data.strip())

p=TextParser(); p.feed(html); print('1. Page text:',p.text)

class LinkParser(HTMLParser):
    def __init__(self): super().__init__(); self.links=[]
    def handle_starttag(self,tag,attrs):
        if tag=='a':
            href=dict(attrs).get('href')
            if href: self.links.append(href)

lp=LinkParser(); lp.feed(html); print('2. Links:',lp.links)

class TitleParser(HTMLParser):
    def __init__(self): super().__init__(); self.in_title=False; self.title=''
    def handle_starttag(self,tag,attrs): self.in_title=(tag=='title')
    def handle_endtag(self,tag):
        if tag=='title': self.in_title=False
    def handle_data(self,data):
        if self.in_title: self.title+=data

tp=TitleParser(); tp.feed(html); print('3. Page title:',tp.title)
base='https://example.com/blog/'
print('4. Absolute URL:',urljoin(base,'/courses'))
parsed=urlparse('https://example.com:443/products?id=10')
print('5. URL host:',parsed.netloc)
print('6. URL scheme:',parsed.scheme)

class ParagraphParser(HTMLParser):
    def __init__(self): super().__init__(); self.paragraphs=[]; self.in_p=False
    def handle_starttag(self,tag,attrs):
        if tag=='p': self.in_p=True
    def handle_endtag(self,tag):
        if tag=='p': self.in_p=False
    def handle_data(self,data):
        if self.in_p and data.strip(): self.paragraphs.append(data.strip())

pp=ParagraphParser(); pp.feed(html); print('7. Paragraphs:',pp.paragraphs)
print('8. Link count:',len(lp.links))
print('9. HTTPS links:',[x for x in lp.links if x.startswith('https://')])
print('10. Summary:',{'title':tp.title,'links':len(lp.links)})
