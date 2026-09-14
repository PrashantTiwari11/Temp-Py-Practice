# 60_password_manager_project.py
# Password Manager Project - 10 practical features
#
# IMPORTANT:
# This is an educational local project. For real password management,
# use a professionally audited password manager and secure key storage.
# Passwords are encrypted at rest using Fernet when the cryptography package
# is installed: pip install cryptography

import base64
import hashlib
import json
import os
import secrets
import string
from getpass import getpass
from pathlib import Path

try:
    from cryptography.fernet import Fernet
except ImportError:
    Fernet = None

VAULT_FILE = Path("password_vault.json")
KEY_FILE = Path("password_vault.key")

def derive_key(master_password):
    # Educational deterministic key derivation.
    digest = hashlib.sha256(master_password.encode()).digest()
    return base64.urlsafe_b64encode(digest)

def load_vault():
    if not VAULT_FILE.exists():
        return {}
    with VAULT_FILE.open("r", encoding="utf-8") as f:
        return json.load(f)

def save_vault(vault):
    with VAULT_FILE.open("w", encoding="utf-8") as f:
        json.dump(vault, f, indent=2)

def encrypt_text(text, master):
    if Fernet is None:
        raise RuntimeError("Install cryptography: pip install cryptography")
    return Fernet(derive_key(master)).encrypt(text.encode()).decode()

def decrypt_text(token, master):
    if Fernet is None:
        raise RuntimeError("Install cryptography: pip install cryptography")
    return Fernet(derive_key(master)).decrypt(token.encode()).decode()

def generate_password(length=16):
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(secrets.choice(alphabet) for _ in range(length))

def password_strength(password):
    score = sum([
        len(password) >= 12,
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(c in "!@#$%^&*" for c in password),
    ])
    return ["Very weak", "Weak", "Fair", "Good", "Strong", "Very strong"][score]

def add_entry(vault, site, username, password, master):
    vault[site] = {
        "username": username,
        "password": encrypt_text(password, master)
    }

def get_entry(vault, site, master):
    entry = vault.get(site)
    if not entry:
        return None
    return {
        "username": entry["username"],
        "password": decrypt_text(entry["password"], master)
    }

def delete_entry(vault, site):
    return vault.pop(site, None) is not None

# 1. Create an empty vault
vault = {}
print("1. Empty vault created.")

# 2. Generate a strong password
generated = generate_password(20)
print("2. Generated password:", generated)

# 3. Check password strength
print("3. Password strength:", password_strength(generated))

# 4. Add an encrypted entry (demo master password)
master = "DemoMasterPassword!"
add_entry(vault, "example.com", "student@example.com", generated, master)
print("4. Entry added and encrypted.")

# 5. Save encrypted vault to disk
save_vault(vault)
print("5. Vault saved:", VAULT_FILE)

# 6. Load vault back
loaded = load_vault()
print("6. Vault loaded. Sites:", list(loaded))

# 7. Retrieve/decrypt an entry
entry = get_entry(loaded, "example.com", master)
print("7. Retrieved username:", entry["username"])
print("   Retrieved password:", entry["password"])

# 8. Search entries by site keyword
keyword = "example"
matches = [site for site in loaded if keyword.lower() in site.lower()]
print("8. Search matches:", matches)

# 9. Delete an entry
deleted = delete_entry(loaded, "example.com")
print("9. Entry deleted:", deleted)

# 10. Security reminders
print("10. Security: use a unique master password, protect the key/vault files,")
print("    never print real passwords, and use audited password-management software.")
