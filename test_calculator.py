# https://github.com/LSKing28/lab10-MH-AW
# Partner 1: Mattias Hird
# Partner 2: Andy Weisenborn

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(1000, 30000), 31000)
        self.assertEqual(add(-1, -4), -5)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(1, 3), -2)
        self.assertEqual(subtract(100, -100), 200)
        self.assertEqual(subtract(0, 0), 0)

    ######## Partner 1
    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-2, 4), -8)

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
        divide(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(3, 81), 4)
        self.assertEqual(logarithm(10, 10), 1)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-1, 5)

    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(-1, 10)
        with self.assertRaises(ValueError):
            logarithm(1, 10)
        with self.assertRaises(ValueError):
            logarithm(10, -1)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(25), 5.0)
        with self.assertRaises(ValueError):
            square_root(-9)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
