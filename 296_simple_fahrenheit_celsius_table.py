"""Project 296: Fahrenheit and Celsius Conversion Table"""
def main():
    try:
        start = float(input("Enter starting Fahrenheit temperature: "))
        end = float(input("Enter ending Fahrenheit temperature: "))
        step = float(input("Enter step size: "))
    except ValueError:
        print("Please enter valid numbers.")
        return
    if step <= 0:
        print("Step size must be greater than zero.")
        return
    if start > end:
        print("Starting temperature must not exceed ending temperature.")
        return
    print("\nFahrenheit   Celsius")
    print("--------------------")
    value = start
    while value <= end + 1e-9:
        print(f"{value:10.1f}   {(value - 32) * 5 / 9:7.2f}")
        value += step

if __name__ == "__main__":
    main()
