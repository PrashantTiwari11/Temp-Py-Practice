# 71_python_regex_validation.py
# Regular Expressions and Validation - 10 practical programs/features
import re

text = "My scores are 85, 92 and 78."
print("1. Numbers:", re.findall(r"\d+", text))

text = "Python is Powerful and Practical"
print("2. P words:", re.findall(r"\bP\w*", text))

email = "student@example.com"
email_pattern = r"^[\w.-]+@[\w.-]+\.[A-Za-z]{2,}$"
print("3. Valid email:", bool(re.fullmatch(email_pattern, email)))

mobile = "9876543210"
print("4. Valid mobile:", bool(re.fullmatch(r"[6-9]\d{9}", mobile)))

password = "Python@123"
strong = (
    len(password) >= 8
    and bool(re.search(r"[A-Z]", password))
    and bool(re.search(r"[a-z]", password))
    and bool(re.search(r"\d", password))
    and bool(re.search(r"[^A-Za-z0-9]", password))
)
print("5. Strong password:", strong)

sentence = "Python    is   easy   to   learn"
print("6. Normalized spaces:", re.sub(r"\s+", " ", sentence))

post = "Learning #Python and #Programming today"
print("7. Hashtags:", re.findall(r"#\w+", post))

text = "Events: 17-09-2026, 20-09-2026"
print("8. Dates:", re.findall(r"\b\d{2}-\d{2}-\d{4}\b", text))

username = "prashant_97"
print("9. Valid username:", bool(re.fullmatch(r"[A-Za-z0-9_]{3,20}", username)))

card = "1234567890123456"
print("10. Masked card:", re.sub(r"\d(?=\d{4})", "*", card))
