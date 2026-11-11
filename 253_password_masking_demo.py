"""Demonstrate hidden password input using getpass."""
import getpass

def main():
    password = getpass.getpass("Enter a password (input is hidden): ")
    if password:
        print(f"Password received. Length: {len(password)} characters.")
        print("The password itself will not be displayed.")
    else:
        print("No password was entered.")

if __name__ == "__main__":
    main()
