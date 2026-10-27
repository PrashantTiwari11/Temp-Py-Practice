"""203 Text statistics from a UTF-8 text file."""
import re
from collections import Counter
from pathlib import Path
def main():
 p=Path(input("Text file path: ").strip().strip('"')).expanduser()
 if not p.is_file(): print("File not found."); return
 try: text=p.read_text(encoding="utf-8")
 except (OSError,UnicodeError) as e: print("Read error:",e); return
 words=re.findall(r"\b[\w']+\b",text.casefold()); counts=Counter(words)
 print(f"Characters: {len(text)}")
 print(f"Non-whitespace characters: {sum(not c.isspace() for c in text)}")
 print(f"Words: {len(words)} | Unique words: {len(counts)} | Lines: {len(text.splitlines())}")
 print("Top 10 words:")
 for word,n in counts.most_common(10): print(f"{word}: {n}")
if __name__=="__main__": main()
