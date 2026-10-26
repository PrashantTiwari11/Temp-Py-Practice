"""200 Basic Markdown-to-HTML converter: headings, lists, paragraphs, bold, italic, code."""
import html,re
from pathlib import Path
def inline(s):
 s=html.escape(s)
 s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
 s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s)
 s=re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)',r'<em>\1</em>',s)
 return s
def convert(text):
 out=[]; listing=False; para=[]
 def flush():
  if para: out.append("<p>"+" ".join(inline(x) for x in para)+"</p>"); para.clear()
 for line in text.splitlines():
  s=line.strip(); m=re.match(r'^(#{1,6})\s+(.+)$',s)
  if m:
   flush()
   if listing: out.append("</ul>"); listing=False
   n=len(m.group(1)); out.append(f"<h{n}>{inline(m.group(2))}</h{n}>")
  elif s.startswith(("- ","* ")):
   flush()
   if not listing: out.append("<ul>"); listing=True
   out.append("<li>"+inline(s[2:])+"</li>")
  else:
   if listing: out.append("</ul>"); listing=False
   if s: para.append(s)
   else: flush()
 flush()
 if listing: out.append("</ul>")
 return "\n".join(out)
def main():
 p=Path(input("Markdown file path: ").strip().strip('"')).expanduser()
 if not p.is_file(): print("File not found."); return
 try: source=p.read_text(encoding="utf-8")
 except (OSError,UnicodeError) as e: print("Read error:",e); return
 doc='<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><title>'+html.escape(p.stem)+'</title></head><body>\n'+convert(source)+'\n</body></html>'
 out=p.with_suffix(".html")
 try: out.write_text(doc,encoding="utf-8"); print("Saved:",out)
 except OSError as e: print("Write error:",e)
if __name__=="__main__": main()
