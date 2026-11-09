import re

PATTERN = re.compile(r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9-]+(?:\\.[A-Za-z0-9-]+)+$")

def is_valid_email(email):
    return len(email) <= 254 and ".." not in email and bool(PATTERN.fullmatch(email))

def main():
    email = input("Enter an email address: ").strip()
    if is_valid_email(email):
        print("The email address has a valid basic format.")
    else:
        print("The email address format appears invalid.")

if __name__ == "__main__":
    main()
