# 138 - Password Strength Checker: 10 practical features
import string
# This demo evaluates locally and does not save passwords.
# 1. Check minimum length
def has_minimum_length(password, minimum=12): return len(password) >= minimum
# 2. Check lowercase
def has_lowercase(password): return any(c.islower() for c in password)
# 3. Check uppercase
def has_uppercase(password): return any(c.isupper() for c in password)
# 4. Check digits
def has_digit(password): return any(c.isdigit() for c in password)
# 5. Check special characters
def has_special(password): return any(c in string.punctuation for c in password)
# 6. Score five basic criteria
def score(password):
    return sum([has_minimum_length(password), has_lowercase(password), has_uppercase(password), has_digit(password), has_special(password)])
# 7. Label strength
def strength_label(password):
    points = score(password)
    return "Weak" if points <= 2 else "Moderate" if points <= 4 else "Strong"
# 8. Suggest improvements
def suggestions(password):
    tips = []
    if not has_minimum_length(password): tips.append("Use at least 12 characters.")
    if not has_lowercase(password): tips.append("Add a lowercase letter.")
    if not has_uppercase(password): tips.append("Add an uppercase letter.")
    if not has_digit(password): tips.append("Add a number.")
    if not has_special(password): tips.append("Add a special character.")
    return tips
# 9. Detect common weak patterns
def has_simple_pattern(password):
    return any(p in password.lower() for p in ("password", "123456", "qwerty", "admin"))
# 10. Print a report without displaying the password
def report(password):
    print("Strength:", strength_label(password), "| Criteria:", f"{score(password)}/5")
    if has_simple_pattern(password): print("Warning: avoid common words or sequences.")
    print("Suggestions:", suggestions(password) or "Basic criteria met.")
if __name__ == "__main__": report(input("Enter a password to evaluate (it will not be printed): "))
