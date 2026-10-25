"""195 File Extension Report: count file types in a folder."""
from pathlib import Path
from collections import Counter
def main():
 folder=Path(input("Folder path: ").strip().strip('"')).expanduser()
 if not folder.is_dir(): print("Folder not found."); return
 counts=Counter(); errors=0
 for p in folder.rglob("*"):
  try:
   if p.is_file(): counts[p.suffix.lower() or "[no extension]"]+=1
  except OSError: errors+=1
 print(f"Folder: {folder.resolve()}\nFiles: {sum(counts.values())}; inaccessible entries: {errors}")
 for ext,n in counts.most_common(): print(f"{ext:20} {n:6}")
if __name__=="__main__": main()
