"""158 Password Strength Checker: 10 features."""
import string
COMMON={"password","123456","qwerty","admin","letmein"}
def length_score(p): return min(len(p)*2,30)
def has_lower(p): return any(c.islower() for c in p)
def has_upper(p): return any(c.isupper() for c in p)
def has_digit(p): return any(c.isdigit() for c in p)
def has_symbol(p): return any(c in string.punctuation for c in p)
def is_common(p): return p.lower() in COMMON
def missing_checks(p):
    checks={"12+ characters":len(p)>=12,"lowercase":has_lower(p),"uppercase":has_upper(p),"number":has_digit(p),"symbol":has_symbol(p)}
    return [k for k,v in checks.items() if not v]
def score(p):
    n=length_score(p)+15*has_lower(p)+15*has_upper(p)+20*has_digit(p)+20*has_symbol(p)
    return 0 if is_common(p) else min(n,100)
def rating(p):
    n=score(p)
    return "Weak" if n<40 else "Fair" if n<65 else "Strong" if n<85 else "Very strong"
def report(p): return {"score":score(p),"rating":rating(p),"missing":missing_checks(p),"common":is_common(p)}
if __name__=="__main__":
    for sample in ("123456","helloWorld7","Practical#Code2026"): print(sample,report(sample))
    print("1 Length score:",length_score("Example123!")); print("2 Lowercase:",has_lower("ABCd"))
    print("3 Uppercase:",has_upper("abcD")); print("4 Digit:",has_digit("abc3"))
    print("5 Symbol:",has_symbol("abc!")); print("6 Common:",is_common("qwerty"))
    print("7 Missing checks:",missing_checks("hello")); print("8 Score:",score("Example123!"))
    print("9 Rating:",rating("Example123!")); print("10 Full report:",report("Example123!"))
