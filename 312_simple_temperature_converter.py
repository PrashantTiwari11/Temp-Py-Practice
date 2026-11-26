# Simple Temperature Converter

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose an option (1 or 2): ")

try:
    temperature = float(input("Enter the temperature: "))

    if choice == "1":
        converted = (temperature * 9 / 5) + 32
        print(f"{temperature:.2f}°C = {converted:.2f}°F")
    elif choice == "2":
        converted = (temperature - 32) * 5 / 9
        print(f"{temperature:.2f}°F = {converted:.2f}°C")
    else:
        print("Invalid choice. Please select 1 or 2.")
except ValueError:
    print("Please enter a valid numeric temperature.")
