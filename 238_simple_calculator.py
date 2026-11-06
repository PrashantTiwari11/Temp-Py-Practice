def calculate(a, operator, b):
    if operator == "+": return a + b
    if operator == "-": return a - b
    if operator == "*": return a * b
    if operator == "/":
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
    raise ValueError("Unsupported operator.")

def main():
    print("Simple Calculator (+, -, *, /)")
    try:
        a = float(input("First number: "))
        op = input("Operator: ").strip()
        b = float(input("Second number: "))
        print("Result:", calculate(a, op, b))
    except (ValueError, ZeroDivisionError) as error:
        print("Error:", error)

if __name__ == "__main__":
    main()
