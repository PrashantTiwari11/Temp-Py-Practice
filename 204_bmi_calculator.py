"""204 Adult BMI calculator; BMI is a screening measure, not a diagnosis."""
def main():
 try:
  weight=float(input("Weight in kilograms: ")); height=float(input("Height in metres (e.g. 1.70): "))
  if weight<=0 or height<=0: raise ValueError
 except ValueError: print("Enter positive numeric weight and height."); return
 bmi=weight/(height*height)
 category="Underweight" if bmi<18.5 else "Healthy weight range" if bmi<25 else "Overweight" if bmi<30 else "Obesity range"
 print(f"BMI: {bmi:.1f}\nAdult screening category: {category}")
 print("BMI is a rough screening tool and does not assess health on its own.")
if __name__=="__main__": main()
