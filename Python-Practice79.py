# 73_python_decorators_generators.py
# Decorators and Generators - 10 practical programs/features
import time

def log_call(func):
    def wrapper(*args, **kwargs):
        print("Calling:", func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log_call
def greet(name):
    return f"Hello, {name}"

print("1. Decorator:", greet("Prashant"))

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"Time taken: {time.perf_counter() - start:.6f}s")
        return result
    return wrapper

@timer
def calculate_sum(n):
    return sum(range(n + 1))

print("2. Timed sum:", calculate_sum(10000))

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return [func(*args, **kwargs) for _ in range(times)]
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    return "Hi"

print("3. Repeated function:", say_hi())

def number_generator(n):
    for i in range(1, n + 1):
        yield i

print("4. Generator:", list(number_generator(5)))

def even_generator(n):
    for i in range(2, n + 1, 2):
        yield i

print("5. Even generator:", list(even_generator(10)))

squares = (x * x for x in range(5))
print("6. Generator expression:", list(squares))

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("7. Fibonacci:", list(fibonacci(8)))

def countdown(n):
    while n > 0:
        yield n
        n -= 1

print("8. Countdown:", list(countdown(5)))

def positive_numbers(values):
    for value in values:
        if value > 0:
            yield value

print("9. Positive values:", list(positive_numbers([-2, 4, -1, 7, 0, 3])))

def pipeline(values):
    for value in values:
        if value % 2 == 0:
            yield value * value

print("10. Pipeline:", list(pipeline(range(1, 7))))
