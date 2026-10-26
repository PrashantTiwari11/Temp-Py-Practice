"""199 Multiplication practice quiz."""
import random
def main():
 try: rounds=int(input("Number of questions (1–100): "))
 except ValueError: print("Enter a whole number."); return
 if not 1<=rounds<=100: print("Choose 1–100."); return
 score=0
 for i in range(1,rounds+1):
  a,b=random.randint(2,12),random.randint(2,12)
  try: ans=int(input(f"Q{i}: {a} × {b} = "))
  except ValueError: print(f"Invalid answer. Correct: {a*b}"); continue
  if ans==a*b: score+=1; print("Correct!")
  else: print("Correct answer:",a*b)
 print(f"Score: {score}/{rounds} ({score/rounds*100:.1f}%)")
if __name__=="__main__": main()
