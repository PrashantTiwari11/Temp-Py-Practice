"""Generate a random password with letters, digits, and symbols."""
import secrets
import string

def main():
    try:
        length = int(input("Password length (minimum 4): "))
        if length < 4:
            print("Choose a length of at least 4.")
            return
    except ValueError:
        print("Please enter a whole number.")
        return
    alphabet = string.ascii_letters + string.digits + "!@#$%&*?"
    password = "".join(secrets.choice(alphabet) for _ in range(length))
    print("Generated password:", password)
    print("Store it securely and do not share it.")

if __name__ == "__main__":
    main()
