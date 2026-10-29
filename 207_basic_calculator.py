def calculate(a, op, b):
    if op=="+": return a+b
    if op=="-": return a-b
    if op=="*": return a*b
    if op=="/":
        if b==0: raise ZeroDivisionError("Cannot divide by zero.")
        return a/b
    raise ValueError("Use +, -, *, or /.")

def main():
    while True:
        first=input("First number (q to quit): ").strip()
        if first.lower()=="q": break
        op=input("Operator (+, -, *, /): ").strip(); second=input("Second number: ").strip()
        try: print("Result:",calculate(float(first),op,float(second)))
        except (ValueError,ZeroDivisionError) as e: print("Error:",e)

if __name__ == "__main__": main()
