"""183 — Flashcard study app with quiz mode and JSON storage."""
import json,random
from pathlib import Path
DB=Path("flashcards.json")
def load():
 try: return json.loads(DB.read_text(encoding="utf-8"))
 except (OSError,json.JSONDecodeError): return []
def save(cards): DB.write_text(json.dumps(cards,indent=2,ensure_ascii=False),encoding="utf-8")
def main():
 cards=load()
 while True:
  print("\nFLASHCARDS\n1 List 2 Add 3 Study 4 Delete 0 Exit")
  c=input("Choose: ").strip()
  if c=="1":
   for i,x in enumerate(cards,1): print(f'{i}. Q: {x["question"]}\n   A: {x["answer"]}')
   if not cards: print("No cards.")
  elif c=="2":
   q=input("Question: ").strip(); a=input("Answer: ").strip()
   if not q or not a: print("Both required."); continue
   cards.append({"question":q,"answer":a}); save(cards); print("Saved.")
  elif c=="3":
   if not cards: print("Add cards first."); continue
   order=cards[:]; random.shuffle(order); score=0
   for x in order:
    print("\nQ:",x["question"]); input("Press Enter to reveal answer...")
    print("A:",x["answer"])
    if input("Did you know it? y/n: ").strip().lower() in {"y","yes"}: score+=1
   print(f"Self-score: {score}/{len(order)} ({100*score/len(order):.1f}%)")
  elif c=="4":
   try: i=int(input("Card number: "))
   except ValueError: print("Invalid number."); continue
   if 1<=i<=len(cards): cards.pop(i-1); save(cards); print("Deleted.")
   else: print("Not found.")
  elif c=="0": save(cards); break
  else: print("Invalid choice.")
if __name__=="__main__": main()
