import re

def check_strength(password):
    checks = {
        "At least 8 characters": len(password) >= 8,
        "Uppercase letter": bool(re.search(r"[A-Z]", password)),
        "Lowercase letter": bool(re.search(r"[a-z]", password)),
        "Number": bool(re.search(r"\d", password)),
        "Special character": bool(re.search(r"[^A-Za-z0-9]", password)),
    }
    score = sum(checks.values())
    for label, passed in checks.items():
        print(f"{'✓' if passed else '✗'} {label}")
    rating = "Strong" if score == 5 else "Medium" if score >= 3 else "Weak"
    print(f"\nStrength: {rating} ({score}/5 checks)")

if __name__ == "__main__":
    value = input("Enter password to check: ")
    if value:
        check_strength(value)
    else:
        print("Password cannot be empty.")
