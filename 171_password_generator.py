"""171 Password Generator: secure local password generation using secrets."""
import secrets, string

SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?"
def generate(length, lower, upper, digits, symbols):
    groups = []
    if lower: groups.append(string.ascii_lowercase)
    if upper: groups.append(string.ascii_uppercase)
    if digits: groups.append(string.digits)
    if symbols: groups.append(SYMBOLS)
    if not groups: raise ValueError("Choose at least one character type.")
    if length < len(groups): raise ValueError("Length is too short for selected character types.")
    chars = [secrets.choice(g) for g in groups]
    alphabet = "".join(groups)
    chars.extend(secrets.choice(alphabet) for _ in range(length-len(chars)))
    for i in range(len(chars)-1, 0, -1):
        j = secrets.randbelow(i+1); chars[i], chars[j] = chars[j], chars[i]
    return "".join(chars)

def yes(prompt, default=True):
    ans = input(prompt + (" [Y/n]: " if default else " [y/N]: ")).strip().lower()
    return default if not ans else ans in ("y","yes")

def main():
    print("PASSWORD GENERATOR")
    try:
        length = int(input("Length (8-128): "))
        count = int(input("Number of passwords (1-20): "))
        if not 8 <= length <= 128 or not 1 <= count <= 20:
            print("Length must be 8-128 and count 1-20."); return
        options = [yes("Include lowercase?"), yes("Include uppercase?"),
                   yes("Include digits?"), yes("Include symbols?")]
        for i in range(count):
            print(f"{i+1}. {generate(length, *options)}")
    except ValueError as exc: print("Error:", exc)
    print("Passwords are not saved. Use a unique password per account and store it securely.")
if __name__ == "__main__": main()
