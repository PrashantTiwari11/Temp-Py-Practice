def celsius_to_fahrenheit(value):
    return value * 9 / 5 + 32

def fahrenheit_to_celsius(value):
    return (value - 32) * 5 / 9

def main():
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    choice = input("Choose 1 or 2: ").strip()
    try:
        value = float(input("Enter temperature: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    if choice == "1":
        print(f"{value:.2f}°C = {celsius_to_fahrenheit(value):.2f}°F")
    elif choice == "2":
        print(f"{value:.2f}°F = {fahrenheit_to_celsius(value):.2f}°C")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
