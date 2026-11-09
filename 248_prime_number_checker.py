def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    divisor = 3
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 2
    return True

def main():
    try:
        number = int(input("Enter a whole number: "))
    except ValueError:
        print("Please enter a valid whole number.")
        return
    print(f"{number} is " + ("a prime number." if is_prime(number) else "not a prime number."))

if __name__ == "__main__":
    main()
