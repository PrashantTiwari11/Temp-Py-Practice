"""185 — Text file toolkit: summary, search, preview, and save edited copy."""
from pathlib import Path
def main():
 path=Path(input("Text file path: ").strip().strip('"')).expanduser()
 if not path.is_file(): print("File not found."); return
 try: text=path.read_text(encoding="utf-8")
 except (OSError,UnicodeError) as e: print("Read error:",e); return
 while True:
  print("\nTEXT TOOLKIT\n1 Summary 2 Search 3 Replace and save copy 4 First 20 lines 0 Exit")
  c=input("Choose: ").strip()
  if c=="1": print(f"Characters {len(text)} | Words {len(text.split())} | Lines {len(text.splitlines())}")
  elif c=="2":
   term=input("Search phrase: ")
   if not term: print("Phrase required."); continue
   found=[(i,line) for i,line in enumerate(text.splitlines(),1) if term.casefold() in line.casefold()]
   for i,line in found: print(f"{i}: {line}")
   print("Matching lines:",len(found))
  elif c=="3":
   old=input("Text to replace: "); new=input("Replacement: ")
   if not old: print("Search text required."); continue
   updated=text.replace(old,new)
   if updated==text: print("No matches."); continue
   out=path.with_name(path.stem+"_edited"+path.suffix)
   try: out.write_text(updated,encoding="utf-8"); print("Saved copy:",out)
   except OSError as e: print("Write error:",e)
  elif c=="4": print("\n".join(text.splitlines()[:20]))
  elif c=="0": break
  else: print("Invalid choice.")
if __name__=="__main__": main()
