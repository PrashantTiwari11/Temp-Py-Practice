"""Calculate the days between today and a chosen date."""
from datetime import date

def main():
    text = input("Enter a date (YYYY-MM-DD): ").strip()
    try:
        target = date.fromisoformat(text)
        days = (target - date.today()).days
        if days > 0:
            print(f"{days} day(s) remaining until {target}.")
        elif days < 0:
            print(f"That date was {-days} day(s) ago.")
        else:
            print("That date is today!")
    except ValueError:
        print("Invalid date. Use YYYY-MM-DD.")

if __name__ == "__main__":
    main()
