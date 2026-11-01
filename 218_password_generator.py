"""218 - Secure Random Password Generator"""
import secrets
import string

def generate_password(length=16, use_symbols=True):
    if length < 4:
        raise ValueError("Password length must be at least 4.")
    symbols = "!@#$%&*+-_?"
    alphabet = string.ascii_letters + string.digits
    if use_symbols:
        alphabet += symbols
    chars = [secrets.choice(string.ascii_lowercase),
             secrets.choice(string.ascii_uppercase),
             secrets.choice(string.digits)]
    if use_symbols:
        chars.append(secrets.choice(symbols))
    chars.extend(secrets.choice(alphabet) for _ in range(length - len(chars)))
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)

def main():
    try:
        length = int(input("Password length (minimum 4): "))
        symbols = input("Include symbols? (y/n): ").strip().lower() == "y"
        print("Generated password:", generate_password(length, symbols))
    except ValueError as error:
        print("Error:", error)

if __name__ == "__main__":
    main()
