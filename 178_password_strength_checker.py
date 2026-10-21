"""Local heuristic only; password is not stored or transmitted."""
import getpass,re
COMMON={"password","password123","12345678","qwerty123","admin123","letmein"}
def evaluate(p):
 score=2 if len(p)>=12 else 1 if len(p)>=8 else 0; tips=[]
 if len(p)<12: tips.append("Use at least 12 characters.")
 for ok,msg in [(any(c.islower() for c in p),"Add lowercase letters."),(any(c.isupper() for c in p),"Add uppercase letters."),(any(c.isdigit() for c in p),"Add digits."),(any(not c.isalnum() for c in p),"Add symbols.")]:
  score+=int(ok)
  if not ok: tips.append(msg)
 if p.casefold() in COMMON: score=0; tips.append("Avoid common passwords.")
 if re.search(r"(.)\\1\\1",p): score=max(0,score-1); tips.append("Avoid repeated characters.")
 rating="Very weak" if score<=1 else "Weak" if score<=2 else "Fair" if score<=3 else "Good" if score<=4 else "Strong"
 return rating,tips
def main():
 p=getpass.getpass("Password (hidden; checked locally): "); rating,tips=evaluate(p); print("Estimated strength:",rating)
 for t in tips: print("-",t)
 if not tips: print("Good mix. Use a unique password for every account.")
if __name__=="__main__": main()
