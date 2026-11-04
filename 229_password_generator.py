import secrets
import string

def generate_password(length, use_digits=True, use_symbols=True):
    if length < 4:
        raise ValueError("Choose a length of at least 4.")
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += "!@#$%^&*()-_=+"
    return "".join(secrets.choice(chars) for _ in range(length))

def main():
    try:
        length = int(input("Password length (minimum 4): "))
        digits = input("Include digits? (y/n): ").strip().lower() != "n"
        symbols = input("Include symbols? (y/n): ").strip().lower() != "n"
        print("Generated password:", generate_password(length, digits, symbols))
    except ValueError as error:
        print("Invalid input:", error)

if __name__ == "__main__":
    main()
