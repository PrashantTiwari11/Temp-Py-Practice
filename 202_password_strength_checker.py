"""202 Simple local password strength estimate; input is not saved or transmitted."""
import string
def main():
 p=input("Password to check (not saved): ")
 if not p: print("No password entered."); return
 score=0; tips=[]
 if len(p)>=12: score+=2
 elif len(p)>=8: score+=1
 else: tips.append("Consider at least 12 characters.")
 for ok,tip in [(any(c.islower() for c in p),"Consider lowercase letters."),(any(c.isupper() for c in p),"Consider uppercase letters."),(any(c.isdigit() for c in p),"Consider digits."),(any(c in string.punctuation for c in p),"Consider symbols.")]:
  if ok: score+=1
  else: tips.append(tip)
 level="Weak" if score<=2 else "Moderate" if score<=4 else "Stronger"
 print(f"Estimated strength: {level} ({score}/6)")
 for t in tips: print("-",t)
 print("This simple check cannot identify breached passwords. Use a trusted password manager.")
if __name__=="__main__": main()
