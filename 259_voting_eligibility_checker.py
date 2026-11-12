"""Check eligibility using an example minimum age of 18."""
def main():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Age cannot be negative.")
        elif age >= 18:
            print("You meet the example age requirement of 18.")
        else:
            print(f"You need {18 - age} more year(s) to meet the example requirement.")
    except ValueError:
        print("Please enter your age as a whole number.")

if __name__ == "__main__":
    main()
