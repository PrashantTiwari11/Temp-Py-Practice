# 74_python_datetime_calculator.py
# Date, Time and Calculator Utilities - 10 practical programs/features
from datetime import date, datetime, timedelta

today = date.today()
print("1. Current date:", today)

now = datetime.now()
print("2. Current datetime:", now.strftime("%Y-%m-%d %H:%M:%S"))

print("3. Formatted date:", today.strftime("%d/%m/%Y"))

exam_date = datetime.strptime("25-12-2026", "%d-%m-%Y").date()
print("4. Parsed date:", exam_date)

future = today + timedelta(days=30)
print("5. Date after 30 days:", future)

birth_date = date(2005, 1, 15)
print("6. Days since birth date:", (today - birth_date).days)

print("7. Weekday:", today.strftime("%A"))

def calculator(a, b, operator):
    if operator == "+": return a + b
    if operator == "-": return a - b
    if operator == "*": return a * b
    if operator == "/": return "Cannot divide by zero" if b == 0 else a / b
    return "Invalid operator"

print("8. Calculator:", calculator(20, 5, "*"))

def percentage(obtained, total):
    return obtained / total * 100

print("9. Percentage:", percentage(425, 500), "%")

def compound_interest(principal, rate, years):
    amount = principal * (1 + rate / 100) ** years
    return amount, amount - principal

amount, interest = compound_interest(10000, 8, 2)
print("10. Compound interest:", round(interest, 2))
