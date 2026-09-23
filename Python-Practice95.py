# 93_python_password_generator.py
# Password Generator and Security Utilities - 10 practical features
import secrets
import string
import hashlib

def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

# 1. Random secure password
password = generate_password(16)
print("1. Secure password:", password)

# 2. Password length
print("2. Password length:", len(password))

# 3. Generate numeric OTP
otp = ''.join(secrets.choice(string.digits) for _ in range(6))
print("3. Six-digit OTP:", otp)

# 4. Generate hexadecimal token
token = secrets.token_hex(16)
print("4. Hex token:", token)

# 5. Generate URL-safe token
print("5. URL-safe token:", secrets.token_urlsafe(16))

# 6. Password strength check
def strength(pwd):
    score = sum([
        len(pwd) >= 12,
        any(c.islower() for c in pwd),
        any(c.isupper() for c in pwd),
        any(c.isdigit() for c in pwd),
        any(c in string.punctuation for c in pwd)
    ])
    return score

print("6. Strength score:", strength(password), "/ 5")

# 7. SHA-256 hash demonstration
digest = hashlib.sha256(b"example-password").hexdigest()
print("7. SHA-256:", digest)

# 8. SHA-512 hash demonstration
print("8. SHA-512:", hashlib.sha512(b"example-password").hexdigest())

# 9. Secure random number
print("9. Secure random number:", secrets.randbelow(1000))

# 10. Token comparison
a = secrets.token_hex(8)
b = a
print("10. Token equality:", secrets.compare_digest(a, b))
