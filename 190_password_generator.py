"""190 Password Generator using cryptographically secure randomness."""
import secrets,string
def main():
 try: n=int(input("Password length (4-256): "))
 except ValueError: print("Enter a whole number."); return
 if not 4<=n<=256: print("Length must be 4-256."); return
 groups=[]
 for prompt,chars in [("Lowercase",string.ascii_lowercase),("Uppercase",string.ascii_uppercase),("Digits",string.digits),("Symbols","!@#$%^&*()-_=+?")]:
  if input(f"Include {prompt}? (y/n): ").strip().lower() in {"y","yes"}: groups.append(chars)
 if not groups: print("Select at least one group."); return
 if n<len(groups): print("Length too short for selected groups."); return
 chars=[secrets.choice(g) for g in groups]; pool="".join(groups)
 chars += [secrets.choice(pool) for _ in range(n-len(chars))]
 secrets.SystemRandom().shuffle(chars)
 print("Generated password:", "".join(chars))
 print("Use a unique password and store it in a trusted password manager.")
if __name__=="__main__": main()
