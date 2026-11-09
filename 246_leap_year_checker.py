def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def main():
    try:
        year = int(input("Enter a year: "))
        if year <= 0:
            raise ValueError
    except ValueError:
        print("Enter a positive whole-number year.")
        return
    result = "a leap year" if is_leap_year(year) else "not a leap year"
    print(f"{year} is {result}.")

if __name__ == "__main__":
    main()
