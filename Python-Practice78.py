# 72_python_testing_logging.py
# Testing and Logging - 10 practical programs/features
import logging
import unittest

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def factorial(n):
    if n < 0:
        raise ValueError("Negative number")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

logging.info("Program started")
print("1. Add:", add(10, 5))

value = -5
if value < 0:
    logging.warning("Negative value detected")
print("2. Subtract:", subtract(10, 5))

try:
    print("3. Divide:", divide(10, 2))
except ValueError as e:
    logging.error(e)

class TestMath(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    def test_subtract(self):
        self.assertEqual(subtract(8, 3), 5)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

assert add(1, 2) == 3
assert factorial(4) == 24
print("4. Manual assertions: passed")

suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestMath)
result = unittest.TextTestRunner(verbosity=0).run(suite)
print("5. Unit tests passed:", result.wasSuccessful())

print("6. Factorial:", factorial(5))
print("7. Division error handled:", end=" ")
try:
    divide(5, 0)
except ValueError:
    print("yes")

print("8. Add test:", add(20, 30) == 50)
print("9. Factorial test:", factorial(3) == 6)
print("10. Testing and logging demo completed.")
