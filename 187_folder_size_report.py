"""187 — Folder size report by file extension; files are never modified."""
from pathlib import Path
from collections import defaultdict
def main():
 folder=Path(input("Folder path: ").strip().strip('"')).expanduser()
 if not folder.is_dir(): print("Folder not found."); return
 sizes=defaultdict(int); counts=defaultdict(int); total=errors=0
 for p in folder.rglob("*"):
  if p.is_file():
   try:
    size=p.stat().st_size; ext=p.suffix.lower() or "[no extension]"
    sizes[ext]+=size; counts[ext]+=1; total+=size
   except OSError: errors+=1
 print("Folder:",folder.resolve())
 print(f"Total {total:,} bytes ({total/1048576:.2f} MiB); files {sum(counts.values())}; unreadable {errors}")
 for ext in sorted(sizes,key=sizes.get,reverse=True): print(f"{ext:18} {counts[ext]:6} file(s) {sizes[ext]:12,} bytes")
if __name__=="__main__": main()
