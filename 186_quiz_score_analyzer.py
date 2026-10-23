"""186 — Quiz score analyzer: ranking, summary, record deletion, CSV export."""
import json,csv
DB="quiz_scores.json"
def load():
 try:
  with open(DB,encoding="utf-8") as f: d=json.load(f)
  return d if isinstance(d,list) else []
 except (OSError,json.JSONDecodeError): return []
def save(d):
 with open(DB,"w",encoding="utf-8") as f: json.dump(d,f,indent=2)
def main():
 records=load()
 while True:
  print("\nQUIZ SCORE ANALYZER\n1 Add score 2 Ranking 3 Summary 4 Export CSV 5 Delete record 0 Exit")
  c=input("Choose: ").strip()
  if c=="1":
   name=input("Learner name: ").strip()
   try: score,total=float(input("Score: ")),float(input("Maximum: "))
   except ValueError: print("Enter numeric scores."); continue
   if not name or total<=0 or score<0 or score>total: print("Invalid score range."); continue
   records.append({"name":name,"score":score,"total":total,"percent":round(score/total*100,2)}); save(records); print("Saved.")
  elif c=="2":
   for rank,r in enumerate(sorted(records,key=lambda x:x["percent"],reverse=True),1): print(f'{rank}. {r["name"]}: {r["score"]:g}/{r["total"]:g} ({r["percent"]:.2f}%)')
   if not records: print("No scores.")
  elif c=="3":
   if not records: print("No scores."); continue
   p=[r["percent"] for r in records]; print(f"Records {len(p)} | Average {sum(p)/len(p):.2f}% | Highest {max(p):.2f}% | Lowest {min(p):.2f}%")
  elif c=="4":
   with open("quiz_scores_export.csv","w",newline="",encoding="utf-8") as f:
    w=csv.DictWriter(f,fieldnames=["name","score","total","percent"]); w.writeheader(); w.writerows(records)
   print("Exported quiz_scores_export.csv")
  elif c=="5":
   try: i=int(input("Record number in insertion order: "))
   except ValueError: print("Invalid number."); continue
   if 1<=i<=len(records): records.pop(i-1); save(records); print("Deleted.")
   else: print("Not found.")
  elif c=="0": break
  else: print("Invalid choice.")
if __name__=="__main__": main()
