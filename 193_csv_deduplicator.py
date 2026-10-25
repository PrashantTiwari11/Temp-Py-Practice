"""193 CSV Deduplicator: preserves the first occurrence of each data row."""
import csv
from pathlib import Path
def main():
 p=Path(input("CSV path: ").strip().strip('"')).expanduser()
 if not p.is_file(): print("File not found."); return
 try:
  with p.open("r",newline="",encoding="utf-8-sig") as f: rows=list(csv.reader(f))
 except (OSError,UnicodeError,csv.Error) as e: print("Read error:",e); return
 if not rows: print("CSV is empty."); return
 seen=set(); unique=[]
 for row in rows[1:]:
  key=tuple(row)
  if key not in seen: seen.add(key); unique.append(row)
 out=p.with_name(p.stem+"_deduplicated"+p.suffix)
 try:
  with out.open("w",newline="",encoding="utf-8") as f:
   w=csv.writer(f); w.writerow(rows[0]); w.writerows(unique)
 except OSError as e: print("Write error:",e); return
 print(f"Rows before: {len(rows)-1}\nRows after: {len(unique)}\nDuplicates removed: {len(rows)-1-len(unique)}\nSaved: {out}")
if __name__=="__main__": main()
