"""
The testing framework that I used is unittest because it is part of Python's standard library, it has a rich set of 
assert methods and support for subtests via `subTest`, a simple CLI runner and easy CI integration.

For this code, I uncovered a floating-point rounding bug when calculating discounted prices. An earlier implementation 
rounded using `round(price * (1 - rate), 2)`, which produced 79.99 instead of 79.992 for 99.99 with a 20% discount. 
The test using `assertAlmostEqual` (with appropriate precision) notice the error, and after that I removed early rounding 
from core logic and only round at the presentation boundary.
"""

DISCOUNT_RATE = 0.2
def calculate_discount_price(price):
    return price * (1 - DISCOUNT_RATE)

import unittest

class TestCodeSmells(unittest.TestCase):
    def test_normal_input(self):
        self.assertAlmostEqual(calculate_discount_price(100), 80)
    
    def test_zero_input(self):
        self.assertAlmostEqual(calculate_discount_price(0), 0)

    def test_float_input(self):
        # 99.99 * 0.8 = 79.992
        self.assertAlmostEqual(calculate_discount_price(99.99), 79.992, places=3)

    def test_negative_input(self):
        # Negative values should be discounted mathematically as well
        self.assertAlmostEqual(calculate_discount_price(-50), -40)

    def test_large_input(self):
        self.assertAlmostEqual(calculate_discount_price(1_000_000_000), 800_000_000)

    def test_invalid_input_types(self):
        for invalid in ["100", None, [], {}]:
            with self.subTest(invalid=invalid):
                with self.assertRaises(TypeError):
                    calculate_discount_price(invalid)

if __name__ == '__main__':
    unittest.main()
