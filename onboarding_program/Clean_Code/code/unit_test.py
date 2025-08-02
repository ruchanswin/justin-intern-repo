DISCOUNT_RATE = 0.2
def calculate_discount_price(price):
    return price * (1 - DISCOUNT_RATE)

import unittest

class TestCodeSmells(unittest.TestCase):
    def test_calculate_discount(self):
        self.assertAlmostEqual(calculate_discount_price(100), 80)
        self.assertAlmostEqual(calculate_discount_price(50), 40)

if __name__ == '__main__':
    unittest.main()
