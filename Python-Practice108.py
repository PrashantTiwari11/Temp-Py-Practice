# 106_python_password_validator.py
# Password Validation and Security Rules - 10 practical features
import string
import hashlib

passwords = ["abc", "Python123", "Python@123", "StrongPass@2026"]

def validate_password(password):
    return {
        "length": len(password) >= 8,
        "lowercase": any(c.islower() for c in password),
        "uppercase": any(c.isupper() for c in password),
        "digit": any(c.isdigit() for c in password),
        "special": any(c in string.punctuation for c in password)
    }

for password in passwords:
    rules = validate_password(password)
    score = sum(rules.values())
    strength = "Strong" if score == 5 else "Medium" if score >= 3 else "Weak"

    print("\nPassword:", password)
    print("1. Minimum length:", rules["length"])
    print("2. Lowercase:", rules["lowercase"])
    print("3. Uppercase:", rules["uppercase"])
    print("4. Digit:", rules["digit"])
    print("5. Special character:", rules["special"])
    print("6. Rule score:", score, "/ 5")
    print("7. Strength:", strength)
    print("8. Valid:", all(rules.values()))

    digest = hashlib.sha256(password.encode()).hexdigest()
    print("9. SHA-256 preview:", digest[:16] + "...")
    print("10. Password length:", len(password))
