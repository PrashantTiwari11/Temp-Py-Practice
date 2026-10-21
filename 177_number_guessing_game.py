import random
def main():
 while True:
  print("Difficulty: 1 Easy (1-20), 2 Medium (1-50), 3 Hard (1-100)")
  c=input("Choose: ").strip()
  if c not in {"1","2","3"}: print("Invalid."); continue
  low,high,tries={"1":(1,20,8),"2":(1,50,7),"3":(1,100,7)}[c]; secret=random.randint(low,high)
  print(f"Guess {low}-{high}; attempts: {tries}")
  for n in range(1,tries+1):
   try: g=int(input(f"{n}/{tries}: "))
   except ValueError: print("Enter a whole number."); continue
   if g==secret: print(f"Correct in {n} attempt(s)!"); break
   print("Too low." if g<secret else "Too high.")
  else: print("Out of attempts. Number was",secret)
  if input("Play again? y/n: ").lower().strip() not in {"y","yes"}: break
if __name__=="__main__": main()
