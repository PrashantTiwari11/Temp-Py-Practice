"""Project 290: Find Leap Years in a Range"""
def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def main():
    try:
        start = int(input("Enter starting year: "))
        end = int(input("Enter ending year: "))
    except ValueError:
        print("Please enter valid whole years.")
        return
    if start < 1 or end < 1 or start > end:
        print("Enter positive years with start no later than end.")
        return
    leap_years = [y for y in range(start, end + 1) if is_leap_year(y)]
    print("Leap years:", leap_years if leap_years else "None found")
    print("Total:", len(leap_years))

if __name__ == "__main__":
    main()
