# Day 12 - 48: Password Generator & Validator
import random
import string

password = "Python@123"

# 1. Minimum length
print("1. Length >= 8:", len(password) >= 8)

# 2. Uppercase check
print("2. Uppercase:", any(c.isupper() for c in password))

# 3. Lowercase check
print("3. Lowercase:", any(c.islower() for c in password))

# 4. Digit check
print("4. Digit:", any(c.isdigit() for c in password))

# 5. Special character check
print("5. Special:", any(c in string.punctuation for c in password))

# 6. Password strength
score = sum([
    len(password) >= 8,
    any(c.isupper() for c in password),
    any(c.islower() for c in password),
    any(c.isdigit() for c in password),
    any(c in string.punctuation for c in password)
])
levels = ["Very Weak", "Weak", "Fair", "Good", "Strong", "Very Strong"]
print("6. Strength:", levels[score])

# 7. Random password
chars = string.ascii_letters + string.digits + string.punctuation
generated = "".join(random.choice(chars) for _ in range(12))
print("7. Generated:", generated)

# 8. Strong password with required categories
generated = (
    random.choice(string.ascii_uppercase)
    + random.choice(string.ascii_lowercase)
    + random.choice(string.digits)
    + random.choice(string.punctuation)
    + "".join(random.choice(chars) for _ in range(8))
)
generated = "".join(random.sample(generated, len(generated)))
print("8. Strong generated:", generated)

# 9. Mask password
print("9. Masked:", "*" * len(password))

# 10. Reusable validator
def validate_password(pwd):
    return (
        len(pwd) >= 8
        and any(c.isupper() for c in pwd)
        and any(c.islower() for c in pwd)
        and any(c.isdigit() for c in pwd)
        and any(c in string.punctuation for c in pwd)
    )

print("10. Valid:", validate_password("Secure@123"))
