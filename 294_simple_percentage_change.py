"""Project 294: Percentage Increase or Decrease Calculator"""
def main():
    try:
        old_value = float(input("Enter the original value: "))
        new_value = float(input("Enter the new value: "))
    except ValueError:
        print("Please enter valid numbers.")
        return
    if old_value == 0:
        print("Cannot calculate percentage change from an original value of zero.")
        return
    change = (new_value - old_value) / abs(old_value) * 100
    if change > 0:
        print(f"Increase: {change:.2f}%")
    elif change < 0:
        print(f"Decrease: {abs(change):.2f}%")
    else:
        print("There is no change (0.00%).")

if __name__ == "__main__":
    main()
