# https://github.com/LSKing28/lab10-MH-AW
# Partner 1: Mattias Hird
# Partner 2: Andy Weisenborn

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(1000,30000), 31000)
        self.assertEqual(add(-1,-4), -5)
        self.assertEqual(add(0,0), 0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(1, 3), -2)
        self.assertEqual(subtract(100, -100), 200)
        self.assertEqual(subtract(0, 0), 0)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(logarithm(2, 8), 3)
        self.assertEqual(logarithm(3, 81), 4)
        self.assertEqual(logarithm(10, 10), 1)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            log(-1, 5)
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()