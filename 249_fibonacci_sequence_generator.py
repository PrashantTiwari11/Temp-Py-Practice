"""Generate the Fibonacci sequence for a requested number of terms."""
def fibonacci(count):
    result = []
    a, b = 0, 1
    for _ in range(count):
        result.append(a)
        a, b = b, a + b
    return result

def main():
    try:
        count = int(input("How many Fibonacci terms? "))
        if count < 1:
            print("Enter a positive whole number.")
            return
        print(*fibonacci(count), sep=", ")
    except ValueError:
        print("Please enter a valid whole number.")

if __name__ == "__main__":
    main()
