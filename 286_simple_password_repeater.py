"""Project 286: Password Re-entry Checker"""
def main():
    password = input("Create a password: ")
    confirmation = input("Enter the password again: ")
    if not password:
        print("Password cannot be empty.")
    elif password == confirmation:
        print("Password entries match.")
    else:
        print("Passwords do not match. Please try again.")

if __name__ == "__main__":
    main()
