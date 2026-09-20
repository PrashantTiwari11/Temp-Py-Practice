# 78_python_encryption_hashing.py
# Hashing and Security Concepts - 10 practical programs/features
import hashlib, hmac, secrets, base64
message='Hello Python'
print('1. SHA-256:',hashlib.sha256(message.encode()).hexdigest())
print('2. SHA-512:',hashlib.sha512(message.encode()).hexdigest())
print('3. MD5:',hashlib.md5(message.encode()).hexdigest())
password='Python@123'; salt=secrets.token_bytes(16)
password_hash=hashlib.pbkdf2_hmac('sha256',password.encode(),salt,100_000)
print('4. PBKDF2 hash:',password_hash.hex())
print('5. Salt:',salt.hex())
check=hashlib.pbkdf2_hmac('sha256',password.encode(),salt,100_000)
print('6. Password verified:',hmac.compare_digest(password_hash,check))
print('7. Secure token:',secrets.token_urlsafe(24))
print('8. Secure OTP:',f'{secrets.randbelow(1_000_000):06d}')
encoded=base64.b64encode(message.encode()).decode(); print('9. Base64 encoded:',encoded)
print('10. Base64 decoded:',base64.b64decode(encoded).decode())
