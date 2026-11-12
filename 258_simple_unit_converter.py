"""Convert distances between kilometres and miles."""
def main():
    print("1. Kilometres to miles")
    print("2. Miles to kilometres")
    choice = input("Choose 1 or 2: ").strip()
    try:
        value = float(input("Enter distance: "))
        if value < 0:
            print("Distance cannot be negative.")
        elif choice == "1":
            print(f"{value:g} km = {value * 0.621371:.3f} miles")
        elif choice == "2":
            print(f"{value:g} miles = {value / 0.621371:.3f} km")
        else:
            print("Invalid option.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
