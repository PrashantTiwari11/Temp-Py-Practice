"""Calculate BMI using height in centimetres and weight in kilograms."""
def main():
    try:
        weight = float(input("Weight in kilograms: "))
        height_cm = float(input("Height in centimetres: "))
        if weight <= 0 or height_cm <= 0:
            print("Height and weight must be greater than zero.")
            return
        bmi = weight / ((height_cm / 100) ** 2)
        print(f"Your BMI is {bmi:.1f}")
        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal range"
        elif bmi < 30:
            category = "Overweight"
        else:
            category = "Obesity range"
        print(f"Category: {category}")
        print("BMI is a general screening measure, not a diagnosis.")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
