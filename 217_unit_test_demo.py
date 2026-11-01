"""217 - Unit Test Demo. Run: python 217_unit_test_demo.py"""
import unittest

def calculate_discount(price, discount_percent):
    if price < 0 or not 0 <= discount_percent <= 100:
        raise ValueError("Invalid price or discount percentage.")
    return price * (1 - discount_percent / 100)

class DiscountTests(unittest.TestCase):
    def test_no_discount(self):
        self.assertEqual(calculate_discount(100, 0), 100)
    def test_discount(self):
        self.assertEqual(calculate_discount(200, 25), 150)
    def test_full_discount(self):
        self.assertEqual(calculate_discount(80, 100), 0)
    def test_invalid_values(self):
        with self.assertRaises(ValueError):
            calculate_discount(-1, 10)
        with self.assertRaises(ValueError):
            calculate_discount(100, 101)

if __name__ == "__main__":
    unittest.main()
