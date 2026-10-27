"""201 Random name picker; each entered name can win only once."""
import random
def main():
 names=[]
 print("Enter one name per line; blank line finishes.")
 while True:
  name=input("Name: ").strip()
  if not name: break
  names.append(name)
 if not names: print("No names entered."); return
 try: count=int(input(f"Number of winners (1–{len(names)}): "))
 except ValueError: print("Enter a whole number."); return
 if not 1<=count<=len(names): print("Winner count out of range."); return
 for i,name in enumerate(random.SystemRandom().sample(names,count),1): print(f"{i}. {name}")
if __name__=="__main__": main()
